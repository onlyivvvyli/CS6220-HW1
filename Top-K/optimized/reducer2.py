import sys
import heapq

heap = []

for line in sys.stdin:
    word, count = line.strip().split("\t", 1)
    count = int(count)
    if len(heap) < 30:
        heapq.heappush(heap, (count, word))
    else:
        if count > heap[0][0]:
            heapq.heapreplace(heap, (count, word))

for count, word in sorted(heap, reverse=True):
    print(f"{word}\t{count}")