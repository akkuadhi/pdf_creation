import requests
import subprocess

SOURCE_USER = "source_username"
DEST_USER = "destination_username"
TOKEN = "your_personal_access_token"

def get_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    repositories = response.json()
    return [repo["name"] for repo in repositories]

def clone_branches(source_repo, dest_repo):
    branches = subprocess.check_output(["git", "ls-remote", f"https://github.com/{SOURCE_USER}/{source_repo}.git", "refs/heads/*"]).decode("utf-8").split("\n")
    for branch in branches:
        if branch:
            branch_name = branch.split("refs/heads/")[-1]
            subprocess.run(["git", "clone", f"--single-branch", f"--branch={branch_name}", f"https://github.com/{SOURCE_USER}/{source_repo}.git"])
            subprocess.run(["git", "remote", "set-url", "origin", f"https://github.com/{DEST_USER}/{dest_repo}.git"], cwd=source_repo)
            subprocess.run(["git", "push", "origin", f"refs/remotes/origin/{branch_name}:refs/heads/{branch_name}"], cwd=source_repo)
            subprocess.run(["rm", "-rf", source_repo])

def main():
    source_repositories = get_user_repositories(SOURCE_USER)
    for repo in source_repositories:
        dest_repo = f"{DEST_USER}/{repo}"
        subprocess.run(["git", "clone", f"https://github.com/{SOURCE_USER}/{repo}.git"])
        clone_branches(repo, dest_repo)

if __name__ == "__main__":
    main()
