# インスタンスの作り方

この文書は、kcai コンセプトに準拠した分野別インスタンスを立ち上げる手順を示します。

## 1. 目的と範囲を定義する

- 対象分野（例: 測量）
- 想定利用者
- 最初に扱う知識領域

## 2. リポジトリを初期化する

最低限、次を配置します。

- `README.md`（分野と運用方針）
- `AGENTS.md`（AI 向け案内の本体）
- `CLAUDE.md`（`@AGENTS.md` の薄い入口）
- `knowledge/`（踏み跡）
- `DECISIONS.md`（分野固有の意思決定記録）
- `LICENSE`（CC0 1.0）
- `scripts/validate_knowledge.py` と `.github/workflows/validate.yml`（形式の機械検査）

初期構成は `templates/instance/` をそのまま流用できます。

## 3. 形式を固定する

適合基準は `docs/conformance.md` を参照。

- 踏み跡は `docs/knowledge-format.md` 準拠
- 原則は `PRINCIPLES.md` 準拠
- ライセンスは CC0 1.0

## 4. 審査フローを決める

- 提案の受付方法（Issue / PR）
- 形式チェックの自動化有無
- 承認者と承認条件

## 5. 最初の踏み跡を登録する

- 一次資料で検証できる内容を 1 つ追加
- `status: draft` で開始し、人が確認後に更新

## 6. 運用時の注意

- AI は共有しない。知識を共有する。
- 製品固有仕様に依存しない記述を優先する。
- 判断が割れる事項は `DECISIONS.md` に残す。
