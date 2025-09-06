import sys

current = None
count = 0
threshold = 5

for line in sys.stdin:
    word, val = line.strip().split("\t", 1)
    val = int(val)

    if current == word:
        count += val
    else:
        if count >= threshold:
            print(f"{current}\t{count}")
        current = word
        count = val

if count >= threshold:
    print(f"{current}\t{count}")