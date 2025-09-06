
#!/usr/bin/env bash
set -e
python3 python/src/cli.py
python3 python/src/bench/run_bench.py --sim
echo "To test compiler stub (sim):"
echo "  cd compiler && mkdir -p build && cd build && cmake .. && make && ./apply_pass --sim example_ir"
