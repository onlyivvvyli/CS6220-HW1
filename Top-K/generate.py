import os
import random

# 设置目录
input_dir = "/hadoop/topdata/1000"
os.makedirs(input_dir, exist_ok=True)

num_files = 1000
vocab_size = 10000

all_words = [f"word{i}" for i in range(vocab_size)]

for i in range(num_files):
    file_path = f"{input_dir}/file_{i}.txt"
    with open(file_path, "w") as f:
        vocab = random.sample(all_words, random.randint(30, 50))
        for _ in range(random.randint(50, 100)):
            sentence = " ".join(
                random.choices(vocab, k=random.randint(5, 12))
            )
            f.write(sentence + "\n")

print(f"Done, {num_files} files, in{input_dir}")


