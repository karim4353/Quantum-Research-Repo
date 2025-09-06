
from python.src.tensors import mps
def test_mps_contract():
    m = mps.random_mps(4, bond_dim=3, phys_dim=2, backend='numpy')
    val = mps.contract_mps(m, backend='numpy')
    assert isinstance(val, float)
