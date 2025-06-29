import subprocess
import datetime
import os

# 1. Change to your Git project directory
repo_path = r"D:\Git-Auto"  # 🔁 Replace with your actual repo path
os.chdir(repo_path)

# 2. Generate dynamic commit message with current date/time
commit_msg = f"Auto commit on {datetime.datetime.now()}"

# 3. Run Git commands safely using subprocess
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push"], check=True)

    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print("Git Status Output:\n", result.stdout)

except subprocess.CalledProcessError as e:
    print("Error occurred while running Git command:")
    print(e)
except FileNotFoundError:
    print("Command not found!")
except Exception as e:
    print("Some other error:",e)