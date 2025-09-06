import sys
import os

seen = set()
for line in sys.stdin:
    words = line.strip().split()
    for w in words:
        w = ''.join(w).lower()
        if w and w not in seen:
            print(f"{w}\t1")
            seen.add(w)

