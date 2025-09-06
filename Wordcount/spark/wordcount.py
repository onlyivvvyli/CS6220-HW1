import sys
import time
from pyspark import SparkContext


def wordcount(input_path, output_path, num_reducers):
    sc = SparkContext(appName="wordcount")

    text_file = sc.textFile(input_path)

    counts = (
        text_file
        .flatMap(lambda line: line.split(' '))
        .map(lambda word: (word, 1))
        .reduceByKey(lambda a, b: a + b, numPartitions=num_reducers)
    )

    counts.saveAsTextFile(output_path)
    sc.stop()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: spark-submit wordcount.py <input_path> <output_path> <num_reducers>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    num_reducers = int(sys.argv[3])

    print(f"Running WordCount for {input_path} with {num_reducers} reducers...")
    start = time.time()
    wordcount(input_path, output_path, num_reducers)
    end = time.time()
    runtime = end - start
    minutes = int(runtime // 60)
    seconds = int(runtime % 60)
    print(f"Runtime for {input_path}: {minutes} m {seconds} s")
