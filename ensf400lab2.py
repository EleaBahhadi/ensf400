from github import Github

# or using an access token
g = Github("your_access_token")
repo = g.get_repo("username/repo")

## Complete your tasks from herefrom github import Github

# Replace "your_access_token" with your GitHub access token
g = Github("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")

# Replace "username/repo" with your GitHub username and repository name
repo = g.get_repo("EleaBahhadi/ensf400")

# Get all branches
branches = repo.get_branches()

# Print branch names
for branch in branches:
    print(branch.name)
