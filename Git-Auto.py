import subprocess
import datetime
import os

repo_path = r"D:\Git-Auto"
os.chdir(repo_path)

commit_msg = f"Auto commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
log_file = os.path.join(repo_path, "git_auto_log.txt")

def log(message):
    with open(log_file, "a") as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push"], check=True)

    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    log("Git Status Output:\n" + result.stdout)

except subprocess.CalledProcessError as e:
    log("Error occurred while running Git command:\n" + str(e))
except FileNotFoundError:
    log("Command not found!")
except Exception as e:
    log("Some other error: " + str(e))