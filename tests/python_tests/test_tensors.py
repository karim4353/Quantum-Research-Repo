import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'python' / 'src'))

from tensors import mps

def test_mps_contract():
    m = mps.random_mps(4, bond_dim=3, phys_dim=2, backend='numpy')
    val = mps.contract_mps(m, backend='numpy')
    assert isinstance(val, float)
