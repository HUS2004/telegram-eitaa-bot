from googletrans import Translator
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

# تعریف مسیر فایل
input_file = "messages.txt"
output_file = "translated_messages.txt"

# ایجاد نمونه از مترجم
translator = Translator()

# تعریف تابع ترجمه
def translate_file():
    # بررسی وجود فایل
    if not os.path.exists(input_file):
        print(f"{input_file} not found.")
        return
    
    # باز کردن فایل برای خواندن و نوشتن
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "a", encoding="utf-8") as outfile:
        # خواندن خطوط جدید
        lines = infile.readlines()
        
        # ترجمه هر خط
        for line in lines:
            if line.strip():  # بررسی خالی بودن خط
                try:
                    translated_text = translator.translate(line, src='ar', dest='fa').text
                    outfile.write(translated_text + "\n")
                except Exception as e:
                    print(f"Error translating line: {line}. Error: {e}")

# تعریف Event Handler برای نظارت بر تغییرات فایل
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == os.path.abspath(input_file):
            print(f"{input_file} has been modified. Translating...")
            translate_file()

# تنظیمات نظارت بر فایل
event_handler = FileChangeHandler()
observer = Observer()
observer.schedule(event_handler, path=os.path.dirname(os.path.abspath(input_file)), recursive=False)
observer.start()

try:
    print("Watching for changes...")
    while True:
        time.sleep(1)  # نظارت پیوسته به مدت 1 ثانیه
except KeyboardInterrupt:
    print("Stopped.")
    observer.stop()
observer.join()

