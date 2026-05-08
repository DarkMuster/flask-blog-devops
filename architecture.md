                ┌─────────────────┐
                │   GitHub Repo   │
                │  (main/develop) │
                └────────┬────────┘
                         │ push
                ┌────────▼────────┐
                │  GitHub Actions │
                │   CI Pipeline   │
                │  lint/test/sec  │
                └────────┬────────┘
                         │ success
                ┌────────▼────────┐
                │  Docker Image   │
                │    ghcr.io      │
                └────────┬────────┘
                         │ deploy
                ┌────────▼────────┐
                │    Railway      │
                │ Staging Server  │
                └─────────────────┘