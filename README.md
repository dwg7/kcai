# kcai

kcai（Knowledge Co-creation AI / 知識共創 AI）は、**AIそのものは共有せず、AIと人が共創したドメイン知識を Markdown として共有し、それぞれが自分の AI で鍛えていく**ためのコンセプトです。

このリポジトリ `dwg7/kcai` は、知識そのものを置く場所ではなく、次を定義するためのリポジトリです。

- 原則（何を守るか）
- 知識の塊の形式（どう書くか）
- 提案と審査の流れ（どう育てるか）
- インスタンスの作り方（どう展開するか）

## 背景

出発点は、大伴さんによる技術継承 AI に関する問題提起です。正確な書誌情報は藤村の確認後に追記します。

kcai では、この考え方を次のように運用します。

- 共有するもの: 知識の塊（Markdown）
- 共有しないもの: AI モデル、契約、計算費用

これにより、共有地（commons）側の維持費を抑えつつ、利用者は自分が得る価値に応じて自分の AI 利用費を負担できます。

## 二層構造

- `dwg7/kcai`: コンセプトと運用ルール
- 各インスタンス（別リポジトリ）: 分野ごとの知識の塊

`dwg7/kcai` は、インスタンスが守るべき約束を提供します。

## 文書一覧

- `PRINCIPLES.md`: 原則
- `docs/knowledge-format.md`: 知識の塊の形式
- `docs/instance.md`: インスタンスの作り方
- `CONTRIBUTING.md`: 提案方法と審査の流れ
- `AGENTS.md`: AI 向け案内の本体
- `CLAUDE.md`: `AGENTS.md` への薄い入口
- `docs/triage.md`: 審査手順
- `DECISIONS.md`: 決定と理由
- `templates/instance/`: インスタンス開始用ひな形

## 謝辞

本コンセプトは、大伴さんの「技術継承 AI」による問題提起を出発点としています。正式な書誌情報および謝辞の表記は、藤村の確認後に確定します。

---

## English summary

kcai is a concept for sharing domain knowledge co-created by humans and AI as plain Markdown, while not sharing AI models, contracts, or compute costs. This repository defines principles, formats, and governance for such knowledge commons, and separate instance repositories hold domain-specific knowledge.
