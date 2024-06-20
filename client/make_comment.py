import os
from ghapi.core import GhApi

assert os.getenv('REPORT_URL'), 'Report URL must exist'
assert os.getenv('PR_NUMBER'), 'PR number must exist'

def make_comment():
  api = GhApi(owner="marts-dev", repo="git-ops-project")
  api.issues.create_comment(os.getenv('PR_NUMBER'), f"Hi! your comparison report is ready: {os.getenv('REPORT_URL')}'.")
  return os.getenv('REPORT_URL')

if __name__ == '__main__':
    print(f'The comparison report can found at: {make_comment()}')