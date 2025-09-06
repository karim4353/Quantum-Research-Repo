# Contributing to Quantum-Research-Repo

Thank you for your interest in contributing to the **Quantum-Research-Repo** project! This document outlines the guidelines for contributing to ensure a smooth and collaborative development process.

## Getting Started

1. **Fork the Repository**:
   Fork the repository on GitHub: [https://github.com/karim4353/Quantum-Research-Repo](https://github.com/karim4353/Quantum-Research-Repo).

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/<your-username>/Quantum-Research-Repo.git
   cd Quantum-Research-Repo
   ```

3. **Set Up the Development Environment**:
   Follow the setup instructions in the [README.md](README.md) to create a virtual environment and install dependencies.

4. **Create a Branch**:
   Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Contribution Guidelines

- **Code Style**:
  - Python code should follow PEP 8 guidelines. Use `flake8` to check style:
    ```bash
    flake8 python/
    ```
  - C++ code should follow the style enforced by the provided `.clang-format` file. Run `clang-format` before committing.
  - Ensure all tests pass:
    ```bash
    pytest tests/python_tests
    ./tests/cpp_tests/test_stub.sh
    ```

- **Commit Messages**:
  - Write clear, concise commit messages using the format:
    ```
    <type>(<scope>): <short description>
    ```
    Example: `feat(python): add new benchmark for tensor operations`
  - Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`.

- **Pull Requests**:
  - Submit a pull request (PR) to the `main` branch of the original repository.
  - Include a detailed description of your changes, referencing any related issues.
  - Ensure the CI pipeline (`.github/workflows/build-and-test.yml`) passes.
  - Address any feedback from code reviews promptly.

- **Testing**:
  - Add tests for new features or bug fixes in `tests/python_tests/` or `tests/cpp_tests/`.
  - Ensure tests cover both simulation mode (`--sim`) and full dependency mode (if applicable).

- **Documentation**:
  - Update `README.md` or `docs/` if your changes affect setup, usage, or design.
  - Add or update Jupyter notebook cells in `python/notebooks/` for new features, ensuring clear walkthroughs and rendered outputs.

## Development Focus Areas

We welcome contributions in the following areas:
- Expanding Jupyter notebooks with detailed walkthroughs and visualizations.
- Enhancing the C++ algebraic simplifier in `compiler/` to support more complex IR transformations.
- Adding new benchmarks or quantum-inspired algorithms in `python/src/bench/`.
- Improving the CI matrix to test additional Python versions or dependency configurations.
- Updating documentation, including architecture diagrams in `docs/design.md`.

## Reporting Issues

If you encounter bugs or have feature requests, please open an issue on the [GitHub repository](https://github.com/karim4353/Quantum-Research-Repo). Provide:
- A clear description of the issue or feature.
- Steps to reproduce (for bugs).
- Expected and actual behavior.

## Community

Join the discussion by opening issues or commenting on existing ones. For direct inquiries, contact the maintainer via GitHub.

Thank you for contributing to **Quantum-Research-Repo**!