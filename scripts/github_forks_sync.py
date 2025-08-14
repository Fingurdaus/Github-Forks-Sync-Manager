import os
import asyncio
import aiohttp

# Use environment variables for secrets and inputs
username = os.environ['GH_ACCOUNT']
token = os.environ.get('GH_TOKEN')
if not token:
    raise RuntimeError('GH_TOKEN environment variable not set. Please add your Personal Access Token as a secret named GH_PAT.')

headers = {
    'Authorization': f"token {token}",
    'Accept': 'application/vnd.github+json'
}

# Limit concurrency to avoid hitting GitHub API rate limits
CONCURRENCY_LIMIT = 5  # Adjust as needed (5-10 recommended)

async def fetch_all_forked_repos(session):
    """Fetch all forked repositories for the user asynchronously."""
    repos = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{username}/repos?type=forks&per_page=100&page={page}'
        async with session.get(url, headers=headers) as resp:
            if resp.status != 200:
                print(f"Error fetching repos: {await resp.text()}")
                break
            data = await resp.json()
            if not data:
                break
            repos.extend(data)
            page += 1
    return repos

async def update_forked_repo(repo, session, semaphore):
    """
    Update a single forked repository by merging upstream changes.
    Uses a semaphore to limit concurrency.
    """
    async with semaphore:
        owner = repo['owner']['login']
        name = repo['name']
        print(f"Processing {owner}/{name}")
        # Fetch full repo details
        repo_url = f"https://api.github.com/repos/{owner}/{name}"
        async with session.get(repo_url, headers=headers) as repo_resp:
            if repo_resp.status != 200:
                print(f"Error fetching repo details for {name}: {await repo_resp.text()}")
                return
            repo_details = await repo_resp.json()
        if not repo_details.get('parent'):
            print(f"Repo {name} has no upstream parent, skipping.")
            return
        # Merge upstream default branch
        merge_url = f"https://api.github.com/repos/{owner}/{name}/merge-upstream"
        payload = {"branch": repo_details['default_branch']}
        async with session.post(merge_url, headers=headers, json=payload) as merge_resp:
            if merge_resp.status == 200:
                print(f"Updated {name} to upstream.")
            else:
                print(f"Failed to update {name}: {await merge_resp.text()}")

async def main():
    """
    Main async entry point.
    - Creates an aiohttp session.
    - Fetches all forked repos.
    - Updates each fork concurrently, limited by a semaphore.
    """
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    async with aiohttp.ClientSession() as session:
        repos = await fetch_all_forked_repos(session)
        print(f"Found {len(repos)} forked repos for {username}")
        # Schedule all repo updates concurrently, but limit active tasks
        tasks = [
            update_forked_repo(repo, session, semaphore)
            for repo in repos
        ]
        await asyncio.gather(*tasks)
    print("Workflow completed. See above for details.")

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())

# In-text citation: [GitHub Docs, 2024]
