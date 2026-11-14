# Git Workflow

## First-time push to GitHub

1. Create an empty repo on GitHub (no README, no .gitignore).
2. Run:

```
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

## Daily loop

```
git add -A
git commit -m "dsa(arrays): add TwoSum (hashmap, O(n))"
git push
```

## Commit message convention

```
dsa(<topic>): <problem> (<approach>, <complexity>)
ai(<topic>): <what you built or learned>
docs: <change>
chore: <tooling>
```

Examples:

- `dsa(slidingwindow): longest substring without repeats (O(n))`
- `ai(rag): add chunking experiments and retrieval hit-rate eval`

## Branching (optional, good practice for AI projects)

Use short-lived branches for bigger AI experiments:

```
git switch -c ai/rag-reranking
# work, commit
git switch main
git merge ai/rag-reranking
git branch -d ai/rag-reranking
```

## Handy commands

```
git status
git log --oneline --graph --decorate -15
git diff --staged
git restore --staged <file>      # unstage
git stash / git stash pop        # park work in progress
git commit --amend --no-edit     # fix the last commit (before pushing)
```

## Never commit

API keys, `.env`, downloaded datasets, vector store files. The .gitignore covers these;
use `.env.example` to document required variables.
