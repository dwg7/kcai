# kcai

kcai（Knowledge Co-creation AI / 知識共創 AI）は、**AIそのものは共有せず、AIと人が共創したドメイン知識を Markdown として共有し、それぞれが自分の AI で鍛えていく**ためのコンセプトです。

このリポジトリ `dwg7/kcai` は、知識そのものを置く場所ではなく、次を定義するためのリポジトリです。

- 原則（何を守るか）
- 知識の塊の形式（どう書くか）
- 提案と審査の流れ（どう育てるか）
- インスタンスの作り方（どう展開するか）

## 背景

出発点は、技術継承 AI に関する問題提起です。

kcai では、この考え方を次のように運用します。

- 共有するもの: 知識の塊（Markdown）
- 共有しないもの: AI モデル、契約、計算費用

これにより、共有地（commons）側の維持費を抑えつつ、利用者は自分が得る価値に応じて自分の AI 利用費を負担できます。

## なぜ持続できるのか

| 共有するもの | 共有しないもの |
|---|---|
| 知識の塊（Markdown のテキスト） | AI のモデル、契約、計算の費用 |
| 置き場所は Git のリポジトリ。費用はほぼかからない | 使う人が、自分の AI の費用を、自分が得る価値のために払う |
| どの AI でも読める | 特定の AI 製品に縛られない |

- 共有地を維持する費用（テキストの保管と提案の審査）は小さく保てます。
- 全員分の AI の費用を誰かが負う構造がありません。
- 知識はテキストなので、AI の製品が入れ替わっても残ります。

## 鍛える循環

1. 利用者が、自分の AI にインスタンスのリポジトリを読ませて仕事をする
2. 足りない知識、まちがった知識、古くなった知識に気づく
3. 利用者の AI が修正案を書き、利用者が確かめる
4. プルリクエストとして共有地に返す
5. 管理者（人と、管理を補助する AI）が原則に照らして審査し、取り込む

## 人の役割: 読む力から問う力へ

AI が資料を読み、要約し、塊の下書きを作れるようになると、技術者に求められる能力の重心は「読む力」から「問う力」に移ります。

- 何を知るべきか、その知識はどんな構造か、どこで手に入るか、何が新しく何が更新を要するか、を**問う**こと。
- AI が出した答えを、出典に照らして**確かめ、問い返す**こと。
- 確かめた度合いを記録に残し、次の問いにつなげること。

kcai の形式（出典、確認の記録、`status`）は、この問いと確認の往復を残すための仕組みでもあります。

## 二層構造

- `dwg7/kcai`: コンセプトと運用ルール
- 各インスタンス（別リポジトリ）: 分野ごとの知識の塊

`dwg7/kcai` は、インスタンスが守るべき約束を提供します。

## 文書一覧

- `PRINCIPLES.md`: 原則
- `docs/knowledge-format.md`: 知識の塊の形式
- `docs/instance.md`: インスタンスの作り方
- `docs/conformance.md`: インスタンスが満たすべき制約（適合基準）
- `CONTRIBUTING.md`: 提案方法と審査の流れ
- `AGENTS.md`: AI 向け案内の本体
- `CLAUDE.md`: `AGENTS.md` への薄い入口
- `docs/triage.md`: 審査手順
- `DECISIONS.md`: 決定と理由
- `scripts/validate_knowledge.py`: 知識の塊の形式検査
- `templates/instance/`: インスタンス開始用ひな形（検査スクリプトと CI 設定を含む）

## 謝辞

本コンセプトは、大伴さんの「技術継承 AI」による問題提起を出発点としています。正式な書誌情報および謝辞の表記は、hfu の確認後に確定します（追跡先: `DECISIONS.md` の未確定事項）。

---

## English summary

kcai is a concept for sharing domain knowledge co-created by humans and AI as plain Markdown, while not sharing AI models, contracts, or compute costs. This repository defines principles, formats, and governance for such knowledge commons, and separate instance repositories hold domain-specific knowledge.
