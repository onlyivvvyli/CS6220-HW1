import sys
current = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if current == word:
        current_count += count
    else:
        if current:
            print ("%s\t%s" % (current, current_count))
        current_count = count
        current_word = word

if current == word:
    print ("%s\t%s" % (current, current_count))
