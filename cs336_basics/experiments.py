import regex as re
from tests.adapters import *
PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""

# Use re.finditer to avoid storing the pre-tokenized words
res = re.findall(PAT, "some text that i'll pre-tokenize")

# print(res)

# from utils import *
# file_path = "../data/TinyStoriesV2-GPT4-valid.txt"
# with open(file_path, "rb") as f:
#     num_processes = 4
#     boundaries = find_chunk_boundaries(f, num_processes, b"<|endoftext|>")

#     # The following is a serial implementation, but you can parallelize this
#     # by sending each start/end pair to a set of processes.
#     # for start, end in zip(boundaries[:-1], boundaries[1:]):
#     start = boundaries[0]
#     end = boundaries[1]
#     f.seek(start)
#     chunk = f.read(end - start).decode("utf-8", errors="ignore")
#     chunk = re.findall(PAT, chunk)
    # print(chunk)
    # Run pre-tokenization on your chunk and store the counts for each pre-token