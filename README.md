# DSA + GenAI Learning Repo

My daily 1 hour practice: **DSA in Java** and **GenAI / LLM apps in Python**.

- Study plan: [docs/STUDY_PLAN.md](docs/STUDY_PLAN.md)
- Progress tracker: [PROGRESS.md](PROGRESS.md)
- Git workflow: [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md)

## Layout

```
dsa/                 Java 17 + Maven + JUnit 5
  src/main/java/dsa/<topic>/   one class per problem
  src/test/java/dsa/<topic>/   tests for the solutions
ai/                  Python projects, one folder per topic
  01-llm-basics ... 08-ml-fundamentals
docs/                study plan, git workflow
scripts/new_problem.py   scaffold a new Java problem + test
```

## Quick start

DSA (Java):

```
cd dsa
mvn test
python ../scripts/new_problem.py arrays ContainsDuplicate
```

AI (Python):

```
cd ai
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then add your API key
```

## Daily rhythm (1 hour)

| Day | 30 min | 30 min |
|-----|--------|--------|
| Mon-Fri | DSA problem (Java) | GenAI topic of the week |
| Sat | GenAI mini-project build (full hour) | |
| Sun | Redo failed DSA problems | ML fundamentals / reading + update PROGRESS.md |
