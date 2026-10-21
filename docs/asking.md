# 構造化された知識に問う

kcai の構造（タグ、関係、出典の引用、時点）は、整った知識を並べるためではなく、**問いを立てて、予想外の発見を得る**ためにあります。人も、人が操る AI も、同じ道具で問えます。

## 道具

```
python3 scripts/build_index.py                  # build/index.json（全踏み跡の索引）と build/tags.md を作る
python3 scripts/build_index.py --stats          # タグ・関係・出典の使われ方
python3 scripts/build_index.py --tag freshness=high
python3 scripts/build_index.py --rel contrasts
python3 scripts/build_index.py --cites <出典id> # その出典を、どの踏み跡が、どの箇所で引いているか
python3 scripts/build_index.py --links <id>     # リンク元とリンク先
python3 scripts/build_index.py --orphans        # どこともつながっていない踏み跡
python3 scripts/build_index.py --grep <語>      # 本文に語を含む踏み跡
```

`build/index.json` は、AI にそのまま渡して、自由な問いを立てられます。

## 問いの例

- **同じ出典の、別の箇所を引いている踏み跡どうしは、食い違っていないか。**（`--cites`）
- **更新が速い出典に依拠していて、確認日が古い踏み跡は何か。**（`--tag freshness=high`、`SOURCES.md` の確認日）
- **ある踏み跡が変わったら、見直すべき踏み跡はどれか。**（`impacts`、`--links`）
- **どこからもリンクされていない踏み跡は、本当に独立した主題か、つなぎ忘れか。**（`--orphans`）
- **版が違う 2 つの出典を比べると、何が新しく、何が食い違うか。**（`review-` の型）
- **似た構造が、別の分野・別の技術にも繰り返し現れていないか。**（`pattern` タグ）

## 発見の残し方

1. 発見を、短い識別子の `finding` タグとして、関係する踏み跡に付ける。
2. 根拠が複数の出典にまたがる場合は、`review-` の踏み跡として、比べたもの、食い違う点、確かめられなかったことを書く。
3. 発見が既存の踏み跡の記述に影響するときは、その踏み跡を直し、`impacts` で結ぶ。
4. **人による確認の前は、`status: draft` のままにする。** 発見は仮説として扱う。
