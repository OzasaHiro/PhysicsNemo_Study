"""Load the public GeoPT checkpoint into PhysicsNeMo 2.1.1 Transolver."""

from pathlib import Path
from typing import Any

import torch


def _checkpoint_state(checkpoint: Any) -> dict[str, torch.Tensor]:
    if not isinstance(checkpoint, dict):
        raise TypeError("GeoPT checkpoint must contain a state dictionary")

    for key in ("state_dict", "model"):
        nested = checkpoint.get(key)
        if isinstance(nested, dict):
            checkpoint = nested
            break

    return {
        key.removeprefix("module."): value
        for key, value in checkpoint.items()
        if isinstance(key, str) and torch.is_tensor(value)
    }


def _physicsnemo_key(key: str) -> str:
    replacements = (
        ("preprocess.linear_pre.0.", "preprocess.layers.0."),
        ("preprocess.linear_post.", "preprocess.layers.2."),
        (".ln_2.", ".ln_mlp1.0."),
        (".mlp.linear_pre.0.", ".ln_mlp1.1.layers.0."),
        (".mlp.linear_post.", ".ln_mlp1.1.layers.2."),
        (".Attn.to_out.0.", ".Attn.out_linear."),
    )
    for old, new in replacements:
        key = key.replace(old, new)
    return key


def load_geopt_checkpoint(
    model: torch.nn.Module,
    checkpoint_path: str | Path,
) -> dict[str, object]:
    """Transfer compatible public GeoPT weights into a PhysicsNeMo Transolver.

    The public GeoPT checkpoint uses the original Transolver module names.
    PhysicsNeMo 2.1.1 uses equivalent layers with different state-dict keys and
    a fused QKV projection. Input and task-specific output layers are left at
    their PhysicsNeMo initialization when their shapes do not match.
    """

    source = _checkpoint_state(
        torch.load(checkpoint_path, map_location="cpu", weights_only=True)
    )
    target = model.state_dict()
    converted: dict[str, torch.Tensor] = {}

    for key, value in source.items():
        if ".Attn.to_q.weight" in key or ".Attn.to_k.weight" in key or ".Attn.to_v.weight" in key:
            continue
        if ".ln_3." in key or ".mlp2." in key or key == "placeholder":
            continue

        new_key = _physicsnemo_key(key)
        if new_key.endswith(".Attn.temperature") and value.ndim == 4:
            value = value.permute(0, 2, 1, 3).contiguous()

        if new_key in target and target[new_key].shape == value.shape:
            converted[new_key] = value

    for key in source:
        suffix = ".Attn.to_q.weight"
        if not key.endswith(suffix):
            continue

        prefix = key[: -len("to_q.weight")]
        qkv_key = f"{prefix}qkv_project.weight"
        qkv = torch.cat(
            (
                source[f"{prefix}to_q.weight"],
                source[f"{prefix}to_k.weight"],
                source[f"{prefix}to_v.weight"],
            ),
            dim=0,
        )
        if qkv_key in target and target[qkv_key].shape == qkv.shape:
            converted[qkv_key] = qkv

    if len(converted) < 100:
        raise RuntimeError(
            f"Only {len(converted)} tensors matched; check the PhysicsNeMo and GeoPT versions"
        )

    result = model.load_state_dict(converted, strict=False)
    return {
        "loaded_tensors": len(converted),
        "missing_keys": list(result.missing_keys),
        "unexpected_keys": list(result.unexpected_keys),
    }
