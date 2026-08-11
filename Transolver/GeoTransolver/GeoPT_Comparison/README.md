# GeoPT / GeoTransolver Performance Comparison

SHIFT-Wing を用いた簡易検証により、GeoPT の事前学習効果と GeoTransolver のアーキテクチャ効果を比較した学習資料です。

## Files

| File | Description |
|---|---|
| [GeoPT_GeoTransolver_Performance_Study.pptx](GeoPT_GeoTransolver_Performance_Study.pptx) | 実験条件、結果、考察、GeoPT と GeoTransolver のメリット・デメリットを整理したプレゼン資料 |
| [GeoPT_実験報告書.pdf](GeoPT_実験報告書.pdf) | 簡易検証実験の詳細レポート（PDF版） |

## Experiment Outline

| Model | Training |
|---|---|
| A: GeoPT | GeoPT 事前学習済み Transolver を fine-tune |
| B: Transolver | Transolver を scratch から学習 |
| C: GeoTransolver | GeoTransolver を scratch から学習 |

- Dataset: SHIFT-Wing 100ケース（train 80 / validation 10 / test 10）
- Targets: Pressure、Wall Shear Stress（WSS）
- Test selection: 迎角・マッハ数などのパラメータ空間の端部を含む10ケース

## How to Read the Comparison

- A と B の比較は、同じ Transolver 系アーキテクチャに対する GeoPT 事前学習の効果を確認するものです。
- B と C の比較は、scratch 学習条件で Transolver と GeoTransolver のアーキテクチャ差を確認するものです。
- A と C は事前学習の有無とアーキテクチャが同時に異なるため、単一要因の比較ではありません。

## References

- [GeoPT: Scaling Physics Foundation Models via Synthetic Pre-Training](https://arxiv.org/abs/2602.20399)
- [GeoTransolver: Learning Physics on Irregular Domains Using Multi-scale Geometry Aware Physics Attention Transformer](https://arxiv.org/abs/2512.20399)

## Notes

- 本資料は勉強会向けの簡易検証結果であり、各手法の一般的な優劣を保証するものではありません。
- 利用条件は [../../../LICENSE](../../../LICENSE)、第三者由来の論文・実装・商標に関する注意は [../../../THIRD_PARTY_NOTICES.md](../../../THIRD_PARTY_NOTICES.md) を参照してください。
