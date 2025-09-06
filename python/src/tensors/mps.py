
"""Tiny MPS toy implementation (numpy + optional torch)"""
import numpy as np
try:
    import torch
    TORCH = True
except Exception:
    TORCH = False

def random_mps(L, bond_dim=4, phys_dim=2, backend='numpy'):
    '''Return list of tensors representing an MPS.'''
    if backend == 'torch' and TORCH:
        import torch
        return [torch.randn(bond_dim, phys_dim, bond_dim) for _ in range(L)]
    else:
        return [np.random.randn(bond_dim, phys_dim, bond_dim) for _ in range(L)]

def contract_mps(mps, backend='numpy'):
    '''Simple left-to-right contraction producing a scalar expectation-like value.'''
    if backend == 'torch' and TORCH:
        import torch
        s = mps[0].sum(dim=(1,))  # simplified
        for t in mps[1:]:
            s = (s.unsqueeze(-1) * t.sum(dim=1)).sum(dim=1)
        return s.sum().item()
    else:
        s = mps[0].sum(axis=1)
        for t in mps[1:]:
            s = (s[...,None] * t.sum(axis=1)).sum(axis=1)
        return float(s.sum())
