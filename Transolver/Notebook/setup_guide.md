# Transolver Notebook Setup Guide

このメモは、`Transolver/Notebook/` にある日本語版 Notebook を読む・実行するための準備情報です。

このリポジトリには、Notebook を実行した結果を PDF 化した補助資料も同梱しています。勉強会参加者が必ず Notebook を実行する必要はありません。まず PDF で流れを確認し、実行環境がある場合だけ Notebook を動かす想定です。

## Notebook

| Notebook | 主題 | 実行難易度 |
|---|---|---|
| `01_transformer_bottleneck_ja.ipynb` | Transformer の Self-Attention と計算量ボトルネック | 低 |
| `02_physics_attention_transolver_ja.ipynb` | Transolver / Physics-Attention の NumPy 実装理解 | 低 |
| `03_training_transolver_shiftwing_caseb_ja_full200_executed.ipynb` | Shift-WING データを使った Transolver scratch 学習例 | 高 |

## 同梱PDF

| PDF | 内容 |
|---|---|
| `../01_transformer_bottleneck_ja_handout.pdf` | Notebook 1 の実行済み結果 |
| `../02_physics_attention_transolver_ja_handout.pdf` | Notebook 2 の実行済み結果 |
| `../03_training_transolver_shiftwing_caseb_ja_full200_executed_handout.pdf` | Notebook 3 の 200 epoch 学習済み結果を含む補助資料 |

## まず読む資料

概要を短時間で把握する場合は、次の順番を推奨します。

1. `../transformer_transolver_flow_infographic.html`
2. `../01_transformer_bottleneck_ja_handout.pdf`
3. `../02_physics_attention_transolver_ja_handout.pdf`
4. `../03_training_transolver_shiftwing_caseb_ja_full200_executed_handout.pdf`

## 推奨環境

Notebook 1/2 は CPU 環境でも実行できます。Notebook 3 の full training は GPU を推奨します。

確認済み環境の例:

```text
Python: 3.12.3
GPU: NVIDIA GeForce RTX 5070 Ti, 16 GB VRAM
CUDA: 12.8
PyTorch: 2.10.0+cu128
Notebook 3 の 200 epoch 学習時間: 約17分
Peak CUDA memory allocated: 約2.5 GB
```

厳密に同じ環境である必要はありませんが、Notebook 3 を実行する場合は CUDA 対応 PyTorch と十分な GPU メモリを確認してください。

## 最小セットアップ

リポジトリルートで作業する想定です。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install numpy matplotlib scipy einops
pip install jupyterlab notebook nbformat nbconvert ipykernel
```

Notebook 1/2 の 3D 表示まで試す場合は、環境に応じて次も追加します。

```bash
pip install pyvista vtk
```

Jupyter Lab を起動する例:

```bash
source .venv/bin/activate
jupyter lab Transolver/Notebook
```

## Notebook 1

```text
Transolver/Notebook/01_transformer_bottleneck_ja.ipynb
```

目的:

- 標準 Transformer の Self-Attention を理解する。
- 点数が増えると `O(N^2)` が重くなることを確認する。
- 物理場では全点を同じ密度で見る必要があるのかを考える。
- Transolver の「点から物理 token へ集約する」発想につなげる。

必要データ:

- なし。説明用の合成データで実行できます。

## Notebook 2

```text
Transolver/Notebook/02_physics_attention_transolver_ja.ipynb
```

目的:

- Physics-Attention の4段階を NumPy で理解する。
- Slice、Aggregate、Token Attention、Deslice の shape を追う。
- 標準 Attention の `N x N` と、Physics-Attention の `M x M` の違いを確認する。

必要データ:

- なし。Toy data を Notebook 内で生成します。

## Notebook 3

```text
Transolver/Notebook/03_training_transolver_shiftwing_caseb_ja_full200_executed.ipynb
```

目的:

- Shift-WING データを使った Transolver surrogate model 学習の流れを理解する。
- 入力特徴量、流入条件 prompt、出力4成分を確認する。
- 学習曲線、test 評価、Pressure 誤差分布を読む。

重要な注意:

- この Notebook は、実行済み結果を PDF で読むことを主な用途にしています。
- 現時点のリポジトリには、Shift-WING の大容量データ、学習済み重み、Transolver 参照実装、学習・評価スクリプトを同梱していません。
- Notebook 内には、作成時の実験環境で使っていた `Transolver_Learn/...` や `EXPERIMENT/GeoPT/...` の参照が残っています。公開配布前に、実行用パッケージとして切り出すか、外部データ取得手順を追加する必要があります。

Notebook 3 を完全に再実行する場合に必要になるもの:

```text
Shift-WING 元データまたは前処理済み .npy
Transolver 参照実装
Shift-WING 用 helper code
train_shift_wing_transolver.py
evaluate_shift_wing_transolver.py
prepare_shift_wing_npys.py
学習済み run または GPU での再学習環境
```

Shift-WING sample dataset は Luminary SHIFT の Hugging Face dataset から取得できます。

```text
https://huggingface.co/datasets/luminary-shift/Wing-sample
```

Hugging Face 側でのログイン、利用条件への同意、Git LFS、大容量データ用の空き容量が必要です。公開前に dataset の利用条件と再配布可否を確認してください。

## Notebook 3 のデータ形式メモ

前処理済みデータを使う場合の入力形式は次です。

```text
x_sample_*.npy     shape = (N, 7)
y_sample_*.npy     shape = (N, 4)
cond_sample_*.npy  shape = (3,)
```

7次元入力 `x`:

```text
[x, y, z, surface_flag, normal_x, normal_y, normal_z]
```

4次元の流入条件 prompt:

```text
[flow_dir_x, flow_dir_y, flow_dir_z, Mach/3]
```

Transolver へ渡す点特徴 `fx`:

```text
[x, y, z, surface_flag, normal_x, normal_y, normal_z,
 flow_dir_x, flow_dir_y, flow_dir_z, Mach/3]
```

出力4成分:

```text
[Pressure, Wall Shear Stress x, Wall Shear Stress y, Wall Shear Stress z]
```

補足:

- 表面法線は速度ではありません。翼表面の外側に垂直な向きを表す幾何ベクトルです。
- Mach 数は速度そのものではなく、流速を音速で割った無次元量です。
- Wall Shear Stress は、流体が壁面をこすることによる壁面せん断応力です。

## よくある問題

### `ModuleNotFoundError`

Notebook 3 は、現時点では未同梱の helper code と Transolver 参照実装を前提にしています。PDF で結果を確認するか、実行用コードを別途配置してください。

### `FileNotFoundError: history.json`

学習済み run がありません。次のいずれかが必要です。

- 学習済み run directory を配布する。
- Notebook 3 の full training を実行する。
- 評価セルを飛ばし、データ確認と forward 確認までを教材範囲にする。

### CUDA が使えない

次で確認してください。

```python
import torch
print(torch.cuda.is_available())
```

False の場合、Notebook 1/2 は問題ありません。Notebook 3 の full training は避けてください。

## 公開前TODO

- Notebook 3 をこのリポジトリ単体で実行できる構成にするか、読み取り専用教材として明示する。
- Shift-WING データの取得手順、利用条件、再配布可否を確認する。
- 学習済み run や checkpoint を配布する場合は、GitHub Releases や外部ストレージの利用を検討する。
- Notebook 3 内の `Transolver_Learn/...` 参照を、最終的な配布構成に合わせて更新する。
- PhysicsNeMo の Transolver / GeoTransolver 実装を使う版を追加するか検討する。
