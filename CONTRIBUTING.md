# Contributing Guide

## Git Workflow
This project uses GitFlow:
- `main` — production branch (protected)
- `develop` — integration branch
- `feature/xxx` — new features
- `fix/xxx` — bug fixes

## Steps to Contribute
1. Fork the repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Run tests: `python -m pytest tests/ -v`
5. Run linting: `python -m flake8 .`
6. Commit: `git commit -m "feat: add my feature"`
7. Push: `git push origin feature/my-feature`
8. Open a Pull Request to `develop`

## Commit Message Format