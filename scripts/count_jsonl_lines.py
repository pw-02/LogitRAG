from __future__ import annotations

import json

path = r"D:\RAG\data\wiki18_100w\wiki18_100w.jsonl"

# Count lines efficiently (doesn't load whole file)
n_lines = 0
with open(path, "r", encoding="utf-8") as f:
    for _ in f:
        n_lines += 1

print(f"Total lines: {n_lines:,}")

print("\nFirst 10 rows (parsed JSON):")
with open(path, "r", encoding="utf-8") as f:
    for i in range(10):
        line = f.readline()
        if not line:
            break
        obj = json.loads(line)
        print(f"\n--- row {i} ---")
        print(obj)

# Optional: show keys/structure summary for the first row
print("\nStructure (keys) of first row:")
with open(path, "r", encoding="utf-8") as f:
    first = json.loads(f.readline())
print(list(first.keys()))
