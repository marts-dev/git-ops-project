import os
from ghapi.core import GhApi

def make_comment():
  owner,repo = os.getenv('REPO').split('/')
  print(owner, repo)
  #api = GhApi(owner=owner, repo=repo, token=os.getenv('GITHUB_TOKEN'))
  #api.issues.add_labels(issue_number=os.environ['NUMBER'], labels=['bug'])

if __name__ == '__main__':
    print(f'The comparison report can found at: {make_comment()}')
