#!/usr/bin/env python3

import re
import random
from pathlib import Path

INPUT = Path("gallery_blocks.txt")
OUTPUT = Path("gallery_distributed.txt")


def extract_blocks(text):
    return re.findall(r"<a\b[\s\S]*?</a>", text)


def main():
    if not INPUT.exists():
        print("Missing gallery_blocks.txt")
        return

    text = INPUT.read_text(encoding="utf-8")
    blocks = extract_blocks(text)

    if not blocks:
        print("No <a> tags found")
        return

    # randomize order
    random.shuffle(blocks)

    # create 3 columns
    cols = [[], [], []]

    # evenly distribute
    for i, block in enumerate(blocks):
        cols[i % 3].append(block)

    # randomize inside each column
    for col in cols:
        random.shuffle(col)

    # build output
    output = ""
    for col in cols:
        output += '<div class="image-column">\n\n'
        output += "\n\n".join(col)
        output += "\n\n</div>\n\n"

    OUTPUT.write_text(output, encoding="utf-8")

    print(f"Saved to {OUTPUT}")
    for i, col in enumerate(cols, 1):
        print(f"Column {i}: {len(col)} items")


if __name__ == "__main__":
    main()