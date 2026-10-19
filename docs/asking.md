# 構造化された知識に問う

kcai の構造（タグ、関係、出典の引用、時点）は、整った知識を並べるためではなく、**問いを立てて、予想外の発見を得る**ためにあります。人も、人が操る AI も、同じ道具で問えます。

## 道具

```
python3 scripts/build_index.py                  # build/index.json（全塊の索引）と build/tags.md を作る
python3 scripts/build_index.py --stats          # タグ・関係・出典の使われ方
python3 scripts/build_index.py --tag freshness=high
python3 scripts/build_index.py --rel contrasts
python3 scripts/build_index.py --cites <出典id> # その出典を、どの塊が、どの箇所で引いているか
python3 scripts/build_index.py --links <id>     # リンク元とリンク先
python3 scripts/build_index.py --orphans        # どこともつながっていない塊
python3 scripts/build_index.py --grep <語>      # 本文に語を含む塊
```

`build/index.json` は、AI にそのまま渡して、自由な問いを立てられます。

## 問いの例

- **同じ出典の、別の箇所を引いている塊どうしは、食い違っていないか。**（`--cites`）
- **更新が速い出典に依拠していて、確認日が古い塊は何か。**（`--tag freshness=high`、`SOURCES.md` の確認日）
- **ある塊が変わったら、見直すべき塊はどれか。**（`impacts`、`--links`）
- **どこからもリンクされていない塊は、本当に独立した主題か、つなぎ忘れか。**（`--orphans`）
- **版が違う 2 つの出典を比べると、何が新しく、何が食い違うか。**（`review-` の型）
- **似た構造が、別の分野・別の技術にも繰り返し現れていないか。**（`pattern` タグ）

## 発見の残し方

1. 発見を、短い識別子の `finding` タグとして、関係する塊に付ける。
2. 根拠が複数の出典にまたがる場合は、`review-` の塊として、比べたもの、食い違う点、確かめられなかったことを書く。
3. 発見が既存の塊の記述に影響するときは、その塊を直し、`impacts` で結ぶ。
4. **人による確認の前は、`status: draft` のままにする。** 発見は仮説として扱う。
