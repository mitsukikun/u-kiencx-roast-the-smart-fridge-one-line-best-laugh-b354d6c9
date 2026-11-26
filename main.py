"""make.fun entry: Roast the Smart Fridge.

Writes the one-line roast to /output/entry.txt and nowhere else.
The grader mounts this repo read-only at /bot, so all writes are
guarded with try/except.
"""

import os

ENTRY = "My smart fridge locked the ice cream drawer and left a note: 'It's not you, it's your 2 a.m. snacking.'"


def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
