🚀# **Auto Git Push with Logging, Retries & Email Alerts**

This project provides a Python-based Git automation tool that automatically commits and pushes changes to your repository.
It includes smart features like logging, retry mechanism for network failures, email alerts, and commit messages with changed filenames.

📌 # **Features**

✅ Detects changed files before committing

✅ Automatically stages files (git add .)

✅ Generates commit messages that include the changed file names

✅ Limits long commit messages (shows first 5 files + ... if more)

✅ Retries git push on network errors with configurable retry attempts & delay

✅ Logs all operations in git_auto_log.txt

✅ Sends email alerts if push fails or an unexpected error occurs

✅ Configurable via .env file (no hardcoding sensitive data)

✅ Can be automated with Task Scheduler for continuous background syncing

⚡# **Requirements**

Python: 3.8 or later

Git: Installed & configured (git remote -v must show your repo)

Email account with SMTP enabled (e.g., Gmail, Outlook, Yahoo)

.env file for storing sensitive credentials

🔒 Environment Variables (.env)

This project uses a .env file to keep configuration safe.

1️⃣ Create a .env file

In your project root:

#Absolute path to your Git repository
REPO_PATH=/absolute/path/to/your/repo

#Email configuration
SENDER_EMAIL=your_email@gmail.com
RECEIVER_EMAIL=receiver_email@example.com
EMAIL_PASSWORD=your_16_character_app_password

#SMTP server settings (Gmail default)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587


**⚠️ Use an App Password for Gmail accounts with 2FA.**

2️⃣ Ignore .env in Git

Ensure .env is not pushed to GitHub:

▶️ Usage

Run the script manually:

python auto_push.py

It will:

Stage files (git add .)

Commit with changed file names in the message

Push to GitHub

Retry if network fails

Log details in git_auto_log.txt

Send an email alert on failure

⚡# **Automating with Task Scheduler (Windows)**
To run automatically every day:

Open Task Scheduler → Create Task

Triggers → New → Repeat task every 1 hour

Actions → New → Start a program

Program/script:

C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python311\python.exe


Add arguments:

"C:\path\to\auto_push.py"


Start in:

C:\path\to\

Save → Right-click task → Run to test

Now it will auto-commit & push at intervals.

📝 # **Logging**

All events are logged in git_auto_log.txt.

Includes commit messages, retries, and error details.

Useful for debugging issues.

🛠️ # **Troubleshooting**

Git not found → Add Git to PATH (git --version should work in terminal).

Email not sending → Check App Password or SMTP settings.

.env not loading → Ensure it’s in the same folder as auto_push.py.

Task Scheduler doesn’t run → Verify Python path & “Start in” directory.

🔐 # **Security Notes**

Never commit .env to GitHub.

Use App Passwords for email (not your main password).

Restrict access to your .env file.

✅ With this setup, your codebase will automatically stay in sync with GitHub with retries, logging, and safety mechanisms built-in.
