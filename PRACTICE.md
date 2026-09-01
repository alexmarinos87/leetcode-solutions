# Coding Practice Framework

This repository is the automated archive of my accepted LeetCode submissions. It is supporting evidence of regular problem-solving practice, not a substitute for production engineering projects or for explaining why an algorithm works.

Detailed explanation-first exercises live in the separate [DSA learning journal](https://github.com/alexmarinos87/dsa-practice-n-learn), where selected patterns are reimplemented across Python, TypeScript and Java with pseudocode and complexity analysis.

## Practice goals

1. Strengthen pattern recognition rather than memorising individual answers.
2. Improve the ability to derive a correct baseline before optimising it.
3. State time and space complexity confidently.
4. Reproduce important solutions without copying.
5. Maintain SQL fluency alongside core data structures and algorithms.
6. Promote useful problems into explanation-first lessons instead of leaving them only as submissions.

## Daily session

A sustainable session is **30–45 minutes**:

1. **Attempt — 20 minutes.** Restate the problem, write examples and implement a first solution before using hints.
2. **Review — 10 minutes.** Identify the reusable pattern, edge cases and complexity.
3. **Record — 5 minutes.** Note the pattern and schedule a revisit.
4. **Retype — 5–10 minutes when due.** Reproduce an earlier solution from memory rather than merely rereading it.

A day still counts when it is used to revisit one difficult problem properly. The goal is understanding and consistency, not inflating a streak.

## Weekly rotation

| Day | Primary focus |
| --- | --- |
| Monday | Arrays, strings and hash maps |
| Tuesday | Two pointers and sliding windows |
| Wednesday | Stacks, queues and linked lists |
| Thursday | Binary search, intervals and heaps |
| Friday | Trees, graphs and traversal |
| Saturday | SQL and data-oriented problems |
| Sunday | Review, retyping and one explanation-first write-up |

The rotation is a guide rather than a rigid quota. Weak patterns should receive additional revisits.

## Definition of done

A problem is not considered learned simply because it was accepted. For an important problem, I should be able to answer:

- What are the inputs, outputs and constraints?
- What is the simplest correct approach?
- Which reusable pattern improves it?
- Why does the algorithm terminate and remain correct?
- What are its time and space costs?
- Which edge cases could break a careless implementation?
- Could I reproduce it from memory several days later?

## Revisit schedule

Use spaced revisits for problems that introduce a new pattern or expose a gap:

```text
first solution → 1 day → 3 days → 7 days → 21 days
```

A revisit should normally be a fresh implementation with no copied code. When a problem still feels unclear after a revisit, it should become a full lesson in the [DSA learning journal](https://github.com/alexmarinos87/dsa-practice-n-learn).

## Progress record template

Progress should be measured by patterns understood and reproduced, not only by the number of accepted submissions.

| Date | Problem | Pattern | Result | Complexity stated | Revisit due | Promoted to lesson |
| --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | Problem name | e.g. sliding window | solved / reviewed | yes / no | YYYY-MM-DD | link / no |

## Repository roles

| Repository | Purpose |
| --- | --- |
| [`leetcode-solutions`](https://github.com/alexmarinos87/leetcode-solutions) | Automated archive of accepted submissions and generated topic indexes |
| [`dsa-practice-n-learn`](https://github.com/alexmarinos87/dsa-practice-n-learn) | Curated explanations, pseudocode, cross-language implementations and learning notes |

This separation keeps the archive useful while making the deeper learning process visible and reviewable.
