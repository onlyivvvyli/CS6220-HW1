import sys

current = None
files = set()

for line in sys.stdin:
    word, filename = line.strip().split("\t", 1)

    if current == word:
        files.add(filename)
    else:
        if current:
            print(f"{current}\t{len(files)}")
        current_word = word
        files = {filename}

if current:
    print(f"{current}\t{len(files)}")

