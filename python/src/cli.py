
"""Small CLI to export a toy IR (JSON) to be consumed by compiler pass stub."""
import json, argparse, random
from pathlib import Path

def make_toy_ir(n=5):
    ops = []
    for i in range(n):
        ops.append({'op': 'matmul', 'id': i, 'inputs': [i-1 if i>0 else None]})
    return {'ops': ops}

def main():
    p = Path(__file__).resolve().parents[2] / 'examples' / 'example_mps.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p,'w') as f:
        json.dump(make_toy_ir(8), f, indent=2)
    print('Wrote', p)

if __name__ == '__main__':
    main()
