import os 
import openai

from git import Repo

from pathlib import Path

PATH_TO_BLOG_REPO = Path("C:\\Users\\anais\\Documents\\Projects\\OpenAI\\OpenAI_Blog_Post_Creator\\anaiscmateus.github.io\\.git")
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent

PATH_TO_CONTENT = PATH_TO_BLOG/"content"

PATH_TO_CONTENT.mkdir(exist_ok=True,parents=True)

def update_blog(commit_message='Updatea blog'):
    # GitPython -- Repo Locations
    repo = Repo(PATH_TO_BLOG_REPO)

    # git add 
    repo.git.add(all=True)

    # git commit -m "updates blog"
    repo.index.commit(commit_message)

    # git push
    origin = repo.remote(name='origin')
    origin.push()

# random_text_string = 'asdgjslkgjlagkjsadkgljsdgjdas'

# with open(PATH_TO_BLOG/"index.html", 'w') as f:
#     f.write(random_text_string)

update_blog()