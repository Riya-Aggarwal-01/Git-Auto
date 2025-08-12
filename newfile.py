import subprocess
import datetime
import os
import time
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# ---- LOAD CONFIG ---- #
load_dotenv()
repo_path = os.getenv("REPO_PATH")
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
smtp_port = int(os.getenv("SMTP_PORT", 587))

log_file = os.path.join(repo_path, "git_auto_log.txt")
os.chdir(repo_path)

# ---- FUNCTIONS ---- #
def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}: {message}\n")
    print(f"{timestamp}: {message}")

def send_email(subject, body):
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        log("Email sent successfully.")
    except Exception as e:
        log(f"Failed to send email: {e}")

def has_changes():
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    return bool(result.stdout.strip())

def get_changed_files():
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    files = []
    for line in result.stdout.strip().split("\n"):
        if line:
            filename = line[3:]  # Handles spaces in filenames
            files.append(filename)
    return files

def git_push_with_retry(max_retries=3, delay_seconds=30):
    for attempt in range(1, max_retries + 1):
        try:
            subprocess.run(["git", "push"], check=True)
            log("Push successful.")
            return True
        except subprocess.CalledProcessError as e:
            error_msg = str(e).lower()
            if any(kw in error_msg for kw in ["network", "connection", "resolve", "timeout"]):
                log(f"Network error on attempt {attempt}. Retrying in {delay_seconds} seconds...")
                time.sleep(delay_seconds)
            else:
                log(f"Push failed (not network error): {e}")
                return False
    return False

# ---- MAIN ---- #
try:
    if has_changes():
        changed_files = get_changed_files()
        files_list = ", ".join(changed_files[:5])
        if len(changed_files) > 5:
            files_list += ", ..."
        commit_msg = f"Auto commit: updated {files_list}"

        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        log(f"Changes committed with message: '{commit_msg}'")

        success = git_push_with_retry()
        if not success:
            send_email(
                subject="Git Push Failed",
                body="Git push failed after retries."
            )
    else:
        log("No changes to commit or push.")

except subprocess.CalledProcessError as e:
    log(f"Git error: {e}")
    send_email("Git Automation Error", f"Git error occurred:\n\n{e}")

except Exception as e:
    log(f"Unexpected error: {e}")
    send_email("Git Automation Unexpected Error", f"Unexpected error:\n\n{e}")
