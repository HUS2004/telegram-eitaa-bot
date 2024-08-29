import subprocess
import concurrent.futures

# مسیرهای فایل‌های پایتون که می‌خواهید اجرا کنید
scripts = [
    "get-telegram.py",
    "translate.py",
    "send-eita.py",
    "clear.py"
]

def run_script(script):
    subprocess.run(["python", script], check=True)

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_script, script) for script in scripts]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # بررسی نتیجه و استثناء
            except Exception as e:
                print(f"Script generated an exception: {e}")

if __name__ == "__main__":
    main()
