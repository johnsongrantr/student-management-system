GitHub Games: Trivia Site Build
Participant Handout & Rubric — Practicing Git Collaboration, Conflict Resolution, History Rewriting, and
Rebase Workflows
Project Overview
In teams (or solo), build a small static trivia website hosted on GitHub Pages. The project is structured in five phases
that mirror real collaboration: building features through pull requests, resolving merge conflicts, hunting a bug with git
bisect, practicing safe and unsafe undo operations, and cleaning up history with rebase before a final merge.
Setup
1. Fork the shared starter repo (or run git init for a solo build).
2. Add the original repo as upstream; keep your own fork as origin.
3. Enable GitHub Pages on your repo (Settings fi Pages) so the site is live from day one.
4. Confirm the starter files exist: index.html, questions.json, style.css.
Participant Checklist
Phase 1 — Building Features
[  ]  Create a feature branch for one enhancement (score counter, timer, dark mode, etc.)
[  ]  Use git add -p at least once to stage hunks selectively
[  ]  Review your own diff with git diff / git diff --staged before committing
[  ]  Push the branch and open a real pull request
[  ]  Get a peer code review comment before merging
[  ]  Merge the PR, then update local main and delete the merged branch (local + remote)
[  ]  Set up at least 3 personal Git aliases
Phase 2 — Deliberate Conflicts
[  ]  Pair up and edit the same line of questions.json on two branches
[  ]  Merge both branches and resolve the resulting conflict by hand
[  ]  Resolve at least one conflict using a configured merge tool
[  ]  Simulate and resolve a remote conflict (both partners push near-simultaneously)
Phase 3 — Bug Hunt
[  ]  Receive (or plant, if you're the "saboteur") a bug hidden several commits back
[  ]  Use git bisect start / good / bad to isolate the exact commit
[  ]  Optional: automate the search with git bisect run
Phase 4 — Undo Practice
[  ]  Fix a bad commit message or missing file with git commit --amend
[  ]  Undo an already-pushed commit safely with git revert
[  ]  Squash three messy local commits using git reset --soft
[  ]  Recover a commit lost to git reset --hard using git reflog
Phase 5 — Clean History
[  ]  Rebase your feature branch onto the latest main before the final PR
[  ]  Resolve any conflicts that surface during the rebase
[  ]  Merge with --ff-only for a clean, linear history
[  ]  Compare git log --graph output for a --no-ff merge vs. a rebase
