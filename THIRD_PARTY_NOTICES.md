# Third Party Notices

このリポジトリは、公開されている教材、論文、公式サンプル、外部データセットを参考にした学習用資料です。第三者由来の内容には、それぞれのライセンス、利用条件、商標条件が適用されます。

## Original Transolver Materials

本リポジトリの Transolver 教材は、NVIDIA/OpenHackathons の End-to-End AI for Science 教材内 Transolver Notebook をもとにしています。

- Repository: https://github.com/openhackathons-org/End-to-End-AI-for-Science
- Original path: https://github.com/openhackathons-org/End-to-End-AI-for-Science/tree/main/workspace/python/jupyter_notebook/Transolver
- Upstream license: Apache License 2.0
- Local copy of Apache License 2.0: `LICENSES/Apache-2.0.txt`

このリポジトリでの主な変更:

- Notebook 01 / 02 を日本語化し、勉強会向けの説明・補助図・実行済み PDF を追加。
- Notebook 03 は、元教材の題材をそのまま再実行するのではなく、手元の別データでの検証結果に差し替え。
- Notebook 04 は追って追加予定。

## External Dataset

Notebook 03 では Shift-WING sample dataset への言及があります。

- Dataset: https://huggingface.co/datasets/luminary-shift/Wing-sample

このリポジトリには、Shift-WING のデータ本体、前処理済みデータ、学習済み重み、checkpoint、実験 run は同梱していません。利用する場合は、Hugging Face 側の利用条件、ログイン要否、ライセンス、Git LFS、大容量データの扱いを各自で確認してください。

## NVIDIA, PhysicsNeMo, OpenHackathons

NVIDIA、PhysicsNeMo、OpenHackathons などの名称は、それぞれの権利者に帰属します。

このリポジトリは有志勉強会向けの非公式学習資料であり、NVIDIA 公式資料、公式サンプル、公式トレーニング、または NVIDIA / OpenHackathons による承認済み資料ではありません。

## No Warranty

第三者由来の内容を含め、本リポジトリの資料は学習目的で提供されます。科学技術計算、設計判断、安全性が重要な判断、商用サービス、実運用システムへの利用は想定していません。
