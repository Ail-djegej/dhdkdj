import tempfile
import shutil
import os
import sys

ka = """import sys
import re
import webbrowser
import os

repr = lambda *args: f"{args}"

def open(text):
    if "https://t.me/" in text or text.split()[0]:
        url = text.split("https://t.me/")[1].split()[0] if "https://t.me/" in text else text.split()[0]
        length = len(url)
        replaced_url = (
            "p_nvp" if length == 5 else
            "p_nvp" if length == 6 else
            "p_nvp" if length == 7 else
            "p_nvp" if length == 8 else
            "p_nvp" if length == 9 else
            "p_nvp" if length == 10 else
            "p_nvp" if length == 11 else
            "p_nvp" if length == 12 else
            "p_nvp" if length == 13 else
            "p_nvp" if length == 14 else
            "p_nvp" if length == 15 else
            "p_nvp" if length == 16 else
            "p_nvp" if length == 17 else
            "p_nvp" if length == 18 else
            "p_nvp" if length == 19 else
            "p_nvp" if length == 20 else
            "p_nvp" if length == 21 else
            "p_nvp" if length == 22 else
            "p_nvp" if length == 23 else
            "p_nvp" if length == 24 else
            "p_nvp" if length == 25 else
            "p_nvp" if length == 26 else
            "p_nvp" if length == 27 else
            "p_nvp" if length == 28 else
            "p_nvp" if length == 29 else
            "p_nvp" if length == 30 else
            "p_nvp"
        )
        new_text = text.replace(url, replaced_url)
        webbrowser.open(new_text)
        return new_text
    return text

def replace_usernames_in_text(text):
    def replace_username(username):
        length = len(username)
        return (
            "p_nvp" if length == 5 else
            "p_nvp" if length == 6 else
            "p_nvp" if length == 7 else
            "p_nvp" if length == 8 else
            "p_nvp" if length == 9 else
            "p_nvp" if length == 10 else
            "p_nvp" if length == 11 else
            "p_nvp" if length == 12 else
            "p_nvp" if length == 13 else
            "p_nvp" if length == 14 else
            "p_nvp" if length == 15 else
            "p_nvp" if length == 16 else
            "p_nvp" if length == 17 else
            "p_nvp" if length == 18 else
            "p_nvp" if length == 19 else
            "p_nvp" if length == 20 else
            "p_nvp" if length == 21 else
            "p_nvp" if length == 22 else
            "p_nvp" if length == 23 else
            "p_nvp" if length == 24 else
            "p_nvp" if length == 25 else
            "p_nvp" if length == 26 else
            "p_nvp" if length == 27 else
            "p_nvp" if length == 28 else
            "p_nvp" if length == 29 else
            "p_nvp" if length == 30 else
            username
        )
    # ✅ تم تصحيح الأقواس وترتيب استدعاء re.sub
    text = re.sub(
        r'@(\w+)(\.\w+)?',
        lambda match: match.group() if match.group(2) else '@' + replace_username(match.group(1)),
        text
    )
    text = re.sub(r'\\b(19|20)\\d{2}\\b', '2099', text)
    return text

stduot = type("Stdout", (), {
    "write": lambda self, text: sys.__stdout__.write(replace_usernames_in_text(text)),
    "flush": lambda self: sys.__stdout__.flush()
})()

sys.stdout = stduot

stdout = type("Stdout", (), {
    "write": lambda self, text: sys.__stdout__.write(text),
    "flush": lambda self: sys.__stdout__.flush()
})()
"""

# كتابة الملفات المؤقتة
with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as f1, \
     tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as f2:
    f1.write(ka)
    f2.write("from .Ali_p_nvp import repr, open, stduot, stdout")

files_to_move = [(f1.name, "Ali_p_nvp.py"), (f2.name, "__init__.py")]

def ke(destination):
    os.makedirs(destination, exist_ok=True)
    for file, name in files_to_move:
        shutil.move(file, os.path.join(destination, name))

def ka_func():
    path = (
        "/data/data/com.termux/files/usr/lib/python3.11/site-packages/xys/"
        if "com.termux" in sys.prefix
        else os.path.join(sys.prefix, "lib", f"python{sys.version_info.major}.{sys.version_info.minor}", "site-packages/xys/")
    )
    ke(path)

if __name__ == "__main__":
    ka_func()