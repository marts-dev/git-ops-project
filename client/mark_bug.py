import os
from ghapi.core import GhApi

def make_comment():
  owner,repo = os.environ['REPO'].split('/')
  api = GhApi(owner=owner, repo=repo)
  api.issues.add_labels(issue_number=os.environ['NUMBER'], labels=['bug'])

if __name__ == '__main__':
    print(f'The comparison report can found at: {make_comment()}')
