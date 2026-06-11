import uuid
import re
import os


def hello(name: str) -> str:
    return f"Hello, {name}! Welcome to devtools-cli."


def generate_uuid() -> str:
    return str(uuid.uuid4())


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text


def wordcount(filepath: str) -> str:
    if not os.path.exists(filepath):
        return f"Error: file '{filepath}' not found."
    with open(filepath, "r") as f:
        content = f.read()
    words = len(content.split())
    lines = len(content.splitlines())
    chars = len(content)
    return f"{words} words, {lines} lines, {chars} characters"
