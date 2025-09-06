#!/usr/bin/env python3
import argparse, time, csv, os, math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))

from tensors import mps
import numpy as np
import matplotlib.pyplot as plt
import psutil

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'results'
OUT.mkdir(parents=True, exist_ok=True)
LOG = OUT / 'logs'
LOG.mkdir(parents=True, exist_ok=True)
PLOT = OUT / 'plots'
PLOT.mkdir(parents=True, exist_ok=True)

try:
    import torch
    TORCH = True
except Exception:
    TORCH = False

def run_once(nsites, backend='numpy'):
    # Create a small mps and contract; measure time and memory
    t0 = time.time()
    proc = psutil.Process()
    mem0 = proc.memory_info().rss
    m = mps.random_mps(nsites, bond_dim=8, phys_dim=2, backend=backend)
    val = mps.contract_mps(m, backend=backend)
    mem1 = proc.memory_info().rss
    t1 = time.time()
    return {'nsites': nsites, 'time': t1-t0, 'mem': mem1-mem0, 'value': float(val)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sim', action='store_true', help='Use numpy sim mode')
    parser.add_argument('--out', default=str(OUT))
    args = parser.parse_args()
    backend = 'numpy' if args.sim or not TORCH else 'torch'
    sizes = [10, 20, 40, 80]
    rows = []
    for n in sizes:
        # run multiple iterations
        times = []
        mems = []
        for _ in range(3):
            r = run_once(n, backend=backend)
            times.append(r['time'])
            mems.append(r['mem'])
        rows.append({'nsites': n, 'time_mean': sum(times)/len(times), 'mem_mean': sum(mems)/len(mems)})
    csvp = Path(args.out)/'logs'/'bench.csv'
    with open(csvp,'w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['nsites','time_mean','mem_mean'])
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    # plot
    xs = [r['nsites'] for r in rows]
    ys = [r['time_mean'] for r in rows]
    plt.figure()
    plt.plot(xs, ys, marker='o')
    plt.xlabel('number of sites')
    plt.ylabel('seconds (mean of 3)')
    plt.title('Bench: naive contraction (sim mode)')
    plt.tight_layout()
    plt.savefig(Path(args.out)/'plots'/'bench.png')
    # simple html report
    with open(Path(args.out)/'report.html','w') as f:
        f.write(f"""<html><body><h1>Bench Report</h1><img src='plots/bench.png' /><pre>{rows}</pre></body></html>""")
    print('Wrote', csvp, 'and plot.')

if __name__ == '__main__':
    main()
