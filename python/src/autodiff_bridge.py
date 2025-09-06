
"""Simple bridge to demonstrate autograd with PyTorch if available."""
import numpy as np
try:
    import torch
    TORCH = True
except Exception:
    TORCH = False

def grad_example_numpy(x):
    # numerical derivative of f(x)=x^2
    eps = 1e-6
    return ( (x+eps)**2 - (x-eps)**2 )/(2*eps)

def grad_example_torch(x_val=2.0):
    if not TORCH:
        raise RuntimeError('Torch not available')
    import torch
    x = torch.tensor(x_val, requires_grad=True)
    y = x*x + 3*x
    y.backward()
    return x.grad.item()
