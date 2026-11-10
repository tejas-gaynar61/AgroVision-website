# Task 2 – Git Branching and Pull Requests

## Branch strategy
- `main`: stable version for submission.
- `dev`: integration branch.
- `feature/homepage`: homepage and crop finder feature.

## Workflow
1. Create a feature branch from `dev`.
2. Make a focused change.
3. Run the website and test the change.
4. Commit and push the feature branch.
5. Open a pull request from feature branch to `dev`.
6. After integration testing, open a pull request from `dev` to `main`.

## Evidence to capture
- Git branch list (`git branch`)
- Commit history (`git log --oneline --graph --all`)
- GitHub pull request pages showing merged PRs
