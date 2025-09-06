import sys
import os

for line in sys.stdin:
    words = line.strip().split()
    filename = os.environ.get("map_input_file", "unknown")
    for w in words:
        w = ''.join(w).lower()
        if w:
            print(f"{w}\t{filename}")
