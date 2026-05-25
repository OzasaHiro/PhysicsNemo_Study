# Transolver Study Materials

Transolver / Physics-Attention を日本語で学ぶための教材です。

HTML は概要説明資料です。PDF は Notebook を実行した結果を保存したもので、Notebook を手元で実行しなくても内容と結果を確認できる補助資料です。

## Files

| Path | Role |
|---|---|
| [transformer_transolver_flow_infographic.html](transformer_transolver_flow_infographic.html) | Transformer と Transolver の処理フローを図解する概要資料 |
| [01_transformer_bottleneck_ja_handout.pdf](01_transformer_bottleneck_ja_handout.pdf) | Notebook 1 の実行済みPDF。Self-Attention と `O(N^2)` ボトルネックを確認 |
| [02_physics_attention_transolver_ja_handout.pdf](02_physics_attention_transolver_ja_handout.pdf) | Notebook 2 の実行済みPDF。Physics-Attention の Slice / Aggregate / Attend / Deslice を確認 |
| [03_training_transolver_shiftwing_caseb_ja_full200_executed_handout.pdf](03_training_transolver_shiftwing_caseb_ja_full200_executed_handout.pdf) | Notebook 3 の実行済みPDF。Shift-WING を使った Transolver 学習例と評価結果を確認 |
| [Notebook/](Notebook/) | 元 Notebook と実行準備メモ |

## Recommended Reading Order

1. [transformer_transolver_flow_infographic.html](transformer_transolver_flow_infographic.html)
2. [01_transformer_bottleneck_ja_handout.pdf](01_transformer_bottleneck_ja_handout.pdf)
3. [02_physics_attention_transolver_ja_handout.pdf](02_physics_attention_transolver_ja_handout.pdf)
4. [03_training_transolver_shiftwing_caseb_ja_full200_executed_handout.pdf](03_training_transolver_shiftwing_caseb_ja_full200_executed_handout.pdf)

Notebook を実行する場合は、[Notebook/setup_guide.md](Notebook/setup_guide.md) を確認してください。

## Notebook Scope

- Notebook 1: Transformer の Self-Attention と物理メッシュ適用時の計算量問題を扱います。
- Notebook 2: Transolver の Physics-Attention を NumPy ベースの toy example で追います。
- Notebook 3: Shift-WING データを使った Transolver scratch 学習の流れを扱います。

Notebook 1/2 は概念理解用で、比較的軽い依存関係で実行できます。Notebook 3 は外部の Shift-WING データ、Transolver 参照実装、学習済み run を前提にするため、現時点では PDF を読む運用を主に想定しています。

## Notes

- この教材は NVIDIA 公式資料ではありません。
- Notebook 3 のデータ本体、学習済み重み、実行補助スクリプトは大きくなりやすいため、現時点ではこのリポジトリに同梱していません。
- 公開前に、必要な外部データの取得方法、ライセンス、配布可否を確認してください。
