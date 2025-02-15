import os

def read_file(path):
    if not path.startswith("/data/"):
        raise ValueError("Access denied.")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    if not path.startswith("/data/"):
        raise ValueError("Access denied.")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)