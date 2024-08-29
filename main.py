import subprocess

# مسیرهای فایل‌های پایتون که می‌خواهید اجرا کنید
scripts = [
    "get-telegram.py",
    "translate.py",
    "send-eita.py"
    "clear.py"
]

# اجرای فایل‌ها به صورت همزمان و باز کردن هر کدام در یک پنجره‌ی ترمینال جداگانه
processes = []
for script in scripts:
    process = subprocess.Popen(["start", "cmd", "/k", "python", script], shell=True)
    processes.append(process)
