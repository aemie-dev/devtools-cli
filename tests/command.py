from devtools.commands import hello, generate_uuid, slugify, wordcount
import tempfile
import os


def test_hello_with_name():
    result = hello("Ame")
    assert "Ame" in result


def test_hello_default():
    result = hello("World")
    assert "World" in result


def test_uuid_format():
    result = generate_uuid()
    parts = result.split("-")
    assert len(parts) == 5


def test_uuid_unique():
    assert generate_uuid() != generate_uuid()


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_special_chars():
    assert slugify("Hello, World! 2024") == "hello-world-2024"


def test_slugify_extra_spaces():
    assert slugify("  too   many   spaces  ") == "too-many-spaces"


def test_wordcount_counts_correctly():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("one two three\nfour five")
        tmpfile = f.name
    result = wordcount(tmpfile)
    os.unlink(tmpfile)
    assert "5 words" in result
    assert "2 lines" in result


def test_wordcount_missing_file():
    result = wordcount("nonexistent.txt")
    assert "Error" in result