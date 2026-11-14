# 12-Week Study Plan (1 hour/day)

## Daily structure

- **Mon-Fri:** 30 min DSA (1 problem: understand, code in Java, test, commit) + 30 min GenAI topic.
- **Sat:** full hour building a GenAI mini-project.
- **Sun:** 30 min redo problems you got stuck on + 30 min ML fundamentals/reading. Update PROGRESS.md.

## Problem-solving routine (DSA, 30 min)

1. 5 min: restate the problem, write 2-3 test cases, think brute force.
2. 15 min: code the best approach you can.
3. 5 min: run tests, note time and space complexity in the class Javadoc.
4. 5 min: if stuck at the 15 min mark, read the hint or solution, then **re-solve from scratch the next Sunday**.

## Week-by-week

| Week | DSA (Java) | GenAI |
|------|-----------|-------|
| 1 | Revision of patterns you know: hashing, two pointers, sliding window (redo 1 problem each, add to your Java template cheat sheet) | LLM API basics, tokens, streaming |
| 2 | Strings, stack | Prompt engineering patterns |
| 3 | Queue, binary search | Structured output, function calling |
| 4 | Linked list | Embeddings and vector search |
| 5 | Trees (traversals, recursion) | RAG v1: chunking and retrieval |
| 6 | BST, heap / priority queue | RAG v2: reranking, citations, evaluation |
| 7 | Graphs: BFS, DFS | Agents: tool-use loop from scratch |
| 8 | Graphs: topological sort, union-find | Agents with LangGraph |
| 9 | Backtracking | Evals and observability |
| 10 | DP 1D | Capstone: design and build |
| 11 | DP 2D, greedy | Capstone: eval and polish |
| 12 | Mixed timed practice (45 min mocks) | Capstone: README, demo, writeup |

## Weekend ML fundamentals (Sundays, 30 min)

Weeks 1-4: linear/logistic regression, loss, gradient descent.
Weeks 5-8: metrics (precision/recall/F1), overfitting, train/val/test.
Weeks 9-12: neural nets, attention and transformers at intuition level.

## Capstone idea

A RAG + agent app over a document set you care about (for example, test automation
docs or your own notes) with an eval set that measures answer quality.
Track answer accuracy, retrieval hit rate, latency, and cost per query.

## Rules that keep the streak alive

- Minimum viable day is 20 minutes. Do not skip, shrink.
- One commit per solved problem or per AI experiment.
- Push every day. A green GitHub graph is the feedback loop.
