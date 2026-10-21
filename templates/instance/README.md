# 測量分野のインスタンス（ひな形）

このリポジトリは、kcai の原則に基づく「測量分野の踏み跡」を管理するための雛形です。

## 目的

- 測量分野で再利用できる知識を Markdown で管理する
- AI と人が共同で改善し、出典付きで更新する

## 構成

- `AGENTS.md`: AI 向け案内の本体
- `CLAUDE.md`: `@AGENTS.md` の入口
- `knowledge/`: 踏み跡
- `DECISIONS.md`: 分野固有の判断記録
- `scripts/validate_knowledge.py`: 形式検査（`python3 scripts/validate_knowledge.py knowledge`）
- `scripts/build_pdf.py`: README.md から辿れる踏み跡を 1 つの PDF にまとめる（`python3 scripts/build_pdf.py --pdf`）
- `.github/workflows/validate.yml`: PR ごとに形式検査を実行

## 知識の索引

（踏み跡を追加するたびに、ここからリンクする。リンクの順序が、まとめの PDF の並び順になる。例: `- [題名](knowledge/<id>.md)`）

## 管理責任者

（インスタンス作成時に記入する。承認とマージの権限者を 1 名以上明記）

## 準拠する kcai

`dwg7/kcai` の原則・形式・適合基準（`docs/conformance.md`）に従う。準拠バージョン: （作成時の kcai のコミットまたは日付を記入）

## ライセンス

CC0 1.0
