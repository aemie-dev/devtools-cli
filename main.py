import sys
from devtools.commands import hello, generate_uuid, slugify, wordcount


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python main.py <command> [args]")
        print("Commands: hello, uuid, slugify, wordcount")
        return

    command = args[0]

    if command == "hello":
        name = args[1] if len(args) > 1 else "World"
        print(hello(name))

    elif command == "uuid":
        print(generate_uuid())

    elif command == "slugify":
        if len(args) < 2:
            print("Usage: python main.py slugify <text>")
            return
        text = " ".join(args[1:])
        print(slugify(text))

    elif command == "wordcount":
        if len(args) < 2:
            print("Usage: python main.py wordcount <filepath>")
            return
        print(wordcount(args[1]))

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
