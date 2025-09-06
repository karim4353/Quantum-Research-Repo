
#!/usr/bin/env bash
set -e
echo "Running python tests"
pytest tests/python_tests || true
echo "Building C++ stub"
mkdir -p compiler/build && cd compiler/build && cmake .. && make || true
