🚀 Auto Git Push with Logging, Retries & Email Alerts

This project provides a Python-based Git automation tool that automatically commits and pushes changes to your repository.
It includes smart features like logging, retry mechanism for network failures, email alerts, and commit messages with changed filenames.

📌 Features

✅ Detects changed files before committing

✅ Automatically stages files (git add .)

✅ Generates commit messages that include the changed file names

✅ Limits long commit messages (shows first 5 files + ... if more)

✅ Retries git push on network errors with configurable retry attempts & delay

✅ Logs all operations in git_auto_log.txt

✅ Sends email alerts if push fails or an unexpected error occurs

✅ Configurable via .env file (no hardcoding sensitive data)

⚡ Requirements

Python 3.8+

Git installed & configured (git remote -v)

SMTP-enabled email account (e.g., Gmail, Outlook)

.env file for storing sensitive credentials
