import time
import os

# فایل‌هایی که باید محتویات آن‌ها پاک شود
files_to_clear = ["messages.txt", "translated_messages.txt"]

def clear_file_contents(file_path):
    """پاک کردن محتویات یک فایل بدون حذف فایل"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("")  # نوشتن رشته خالی برای پاک کردن محتویات فایل

def clear_files_periodically(interval_hours=24):
    """پاک کردن محتویات فایل‌ها هر مدت معین (بر حسب ساعت)"""
    while True:
        for file in files_to_clear:
            if os.path.exists(file):
                clear_file_contents(file)
                print(f"Contents of {file} have been cleared.")
            else:
                print(f"{file} not found.")
        
        # خواباندن برنامه برای مدت معین (به ساعت تبدیل شده به ثانیه)
        time.sleep(interval_hours * 3600)

if __name__ == "__main__":
    clear_files_periodically()
