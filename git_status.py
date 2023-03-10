#Ardavan Sherafat
#January 14th 2023

import git
import datetime
import pytz


def git_status(git_dir):
    try:
        # Open the repository
        repo = git.Repo(git_dir)

        # Get the active branch
        active_branch = repo.active_branch
        print("active branch: ", active_branch)

        # Check if there are any modified files
        print("modified files: ", repo.is_dirty())

        # Get the current head commit
        head_commit = repo.head.commit

        # Check if the commit was authored in the last week
        time_now = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
        last_week = time_now - datetime.timedelta(days=7)
        print("recent commit: ", last_week < head_commit.committed_datetime)

        # Check if the commit was authored by Rufus
        print("authored by Rufus: ", head_commit.author.name == "Rufus")

    except git.exc.InvalidGitRepositoryError as e:
        print("Error: Not a valid git repository")
    except Exception as e:
        print("Error: ", e)


#Replace path with directory in which to assess git status
git_status("PATH")
