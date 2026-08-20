# PhysicsNeMo / SimJEB Study

空力・構造設計エンジニア向けに、PhysicsNeMo上のTransolver / GeoTransolverをGoogle Colabから利用する流れを説明する資料です。SimJEBのダウンロード後データを使用する前提で、データ読込、学習、保存、推論までを扱います。

## Files

| File | Description |
|---|---|
| [PhysicsNeMo_Transolver_SimJEB_Study.pptx](PhysicsNeMo_Transolver_SimJEB_Study.pptx) | 勉強会用スライド |
| [geopt_checkpoint.py](geopt_checkpoint.py) | GeoPT公開重みをPhysicsNeMo 2.1.1のTransolverへ移す変換関数 |
| [requirements.txt](requirements.txt) | スライド内コードの確認に使用したPhysicsNeMo固定版 |

## Verified API Scope

- `nvidia-physicsnemo==2.1.1`
- `from physicsnemo.models.transolver import Transolver`
- `from physicsnemo.experimental.models.geotransolver import GeoTransolver`
- GeoPT公開ファイル `GeoPT_8layers.pt`

GeoTransolverはPhysicsNeMo 2.1.1ではexperimental APIです。将来のPhysicsNeMoでimport先や引数が変わる可能性があるため、教材Notebookも上記バージョンに固定します。

GeoPT公開重みはオリジナルTransolverのstate-dict名を使用しており、PhysicsNeMo 2.1.1へ単純な`load_state_dict`だけでは読み込めません。同梱の`load_geopt_checkpoint`がキー名、QKV結合、temperature軸を変換し、入力層とタスク固有出力層を除く互換重みを読み込みます。
