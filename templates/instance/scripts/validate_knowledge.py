#!/usr/bin/env python3
"""知識の塊が docs/knowledge-format.md に適合しているか検査する。

標準ライブラリのみで動作する。使い方:
    python3 scripts/validate_knowledge.py [knowledge ディレクトリ ...]
引数なしの場合は ./knowledge を検査する。違反があれば終了コード 1。
"""
import datetime
import re
import sys
from pathlib import Path

REQUIRED = ["id", "title", "status", "sources", "authors", "reviewed_by", "updated", "related"]
STATUSES = {"draft", "reviewed", "stable", "deprecated"}
HEADINGS = ["## 要点", "## 詳しく", "## よくあるまちがい", "## 出典"]
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
AI_RE = re.compile(r"AI\s*支援(あり|なし)")
REVIEWED_RE = re.compile(r".+\s\(\d{4}-\d{2}-\d{2}\)$")
MAX_BODY_LINES = 200


def parse_front_matter(text):
    """フロントマターを (dict, 本文) で返す。形式は単純な YAML の部分集合に限る。"""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("先頭が '---' ではない（フロントマターがない）")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        raise ValueError("フロントマターが '---' で閉じられていない")
    data, key = {}, None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", raw)
        if m and not raw.startswith(" "):
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                data[key] = []
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                data[key] = [v.strip() for v in inner.split(",")] if inner else []
            else:
                data[key] = val
        elif raw.lstrip().startswith("- ") and key is not None and isinstance(data.get(key), list):
            data[key].append(raw.lstrip()[2:].strip())
        else:
            raise ValueError(f"解釈できない行: {raw!r}")
    return data, "\n".join(lines[end + 1:])


def check_file(path, all_ids):
    errs = []
    try:
        fm, body = parse_front_matter(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        return [str(e)], None
    for k in REQUIRED:
        if k not in fm:
            errs.append(f"必須フィールド '{k}' がない")
    if errs:
        return errs, fm

    if not ID_RE.match(fm["id"]):
        errs.append(f"id が kebab-case ではない: {fm['id']}")
    if fm["id"] != path.stem:
        errs.append(f"id とファイル名が一致しない: {fm['id']} != {path.stem}")
    if fm["status"] not in STATUSES:
        errs.append(f"status が不正: {fm['status']}")
    try:
        datetime.date.fromisoformat(fm["updated"])
    except ValueError:
        errs.append(f"updated が YYYY-MM-DD ではない: {fm['updated']}")
    for k in ("sources", "authors", "reviewed_by", "related"):
        if not isinstance(fm[k], list):
            errs.append(f"{k} は配列でなければならない")
    if errs:
        return errs, fm

    if not fm["sources"]:
        errs.append("sources が空（出典のない断定は不可）")
    if not any(AI_RE.search(a) for a in fm["authors"]):
        errs.append("authors に『AI 支援あり／なし』の記載がない")
    if fm["status"] in ("reviewed", "stable") and not fm["reviewed_by"]:
        errs.append(f"status={fm['status']} だが reviewed_by が空")
    for r in fm["reviewed_by"]:
        if not REVIEWED_RE.match(r):
            errs.append(f"reviewed_by は '氏名 (YYYY-MM-DD)' 形式: {r}")
    for rel in fm["related"]:
        if rel not in all_ids:
            errs.append(f"related の id が存在しない: {rel}")
        if rel == fm["id"]:
            errs.append("related に自身の id を含めている")

    # 見出しが所定の順序で、各 1 回だけ現れること
    found = [l.strip() for l in body.splitlines() if l.startswith("## ")]
    if found != HEADINGS:
        errs.append(f"見出し構成が所定と異なる: {found}（期待: {HEADINGS}）")
    if len(body.splitlines()) > MAX_BODY_LINES:
        errs.append(f"本文が {MAX_BODY_LINES} 行を超えている（小さな塊に分ける）")
    return errs, fm


def main(argv):
    roots = [Path(a) for a in argv] or [Path("knowledge")]
    files = sorted(p for r in roots for p in (r.rglob("*.md") if r.is_dir() else [r]))
    files = [p for p in files if p.name.lower() != "readme.md"]

    ids, dup_errs = {}, []
    for p in files:
        try:
            fm, _ = parse_front_matter(p.read_text(encoding="utf-8"))
        except (ValueError, UnicodeDecodeError):
            continue
        i = fm.get("id")
        if i in ids:
            dup_errs.append(f"{p}: id '{i}' が {ids[i]} と重複")
        ids.setdefault(i, p)

    failed = bool(dup_errs)
    for e in dup_errs:
        print(f"NG {e}")
    for p in files:
        errs, _ = check_file(p, set(ids))
        for e in errs:
            print(f"NG {p}: {e}")
        failed = failed or bool(errs)
    print(f"{len(files)} 件を検査: {'失敗' if failed else '問題なし'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
