# ToDo
# [x] 1. Create a new folder in home directory
# [x] 2. Initalise git repository
# [x] 3. Create a new repo in GitHub and link

import sys
import os
from github import Github

home_path = "/home/kishj/OneDrive/development/"             # Path to store development work
access_token = "c98ac6c9b89bcf66dae21726efc8514d251304e7"   # Personal access token from GitHub
git_user = "kishjogia"

def project_init():
    if len(sys.argv) == 2:
        folderName = str(sys.argv[1])
        os.makedirs(home_path + folderName)             # Create a new directory

        # Create a git repository
        os.chdir(home_path + folderName)
        os.system('git init')

        # Create a readme file and do an Inital commit
        os.system('echo "# ' + folderName + '" >> README.md')
        os.system('git add .')
        os.system('git commit -m "Initial commit"')

        g_hub = Github(access_token).get_user()         # Login using Personal Access Token
        g_hub.create_repo(folderName)                   # Create repository in Github

        os.system('git remote add origin git@github.com:' + git_user +'/' + folderName + '.git')
        os.system('git push -u origin master')
    else:
        print("Need a name for the Project...Exiting")
        return

    return

if __name__ == "__main__":
    project_init()