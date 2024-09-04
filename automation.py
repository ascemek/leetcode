import os
import subprocess
from datetime import datetime

def run_git_command(command):
    """Run a Git command and return the output."""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

def has_changes():
    """Check if there are any changes in the repository."""
    status = run_git_command(['git', 'status', '--porcelain'])
    return bool(status)

def stage_changes():
    """Stage all changes."""
    run_git_command(['git', 'add', '.'])

def commit_changes():
    """Commit changes with a timestamped message."""
    commit_message = f"Daily LeetCode Question Done. Auto-commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run_git_command(['git', 'commit', '-m', commit_message])

def push_changes():
    """Push changes to the remote repository."""
    run_git_command(['git', 'push'])

def main():
    if has_changes():
        print("Changes detected. Pushing to GitHub...")
        stage_changes()
        commit_changes()
        push_changes()
        print("Changes pushed successfully.")
    else:
        print("No changes detected.")

if __name__ == "__main__":
    main()
