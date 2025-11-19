from collections import Counter

def word_frequency(sentence):
    return Counter(sentence.lower().split())

# example
print(word_frequency("the cat and the hat"))  # -> Counter({'the':2, 'cat':1, ...})
def transpose(matrix):
    if not matrix: return []
    return [list(row) for row in zip(*matrix)]

# example
print(transpose([[1,2],[3,4],[5,6]]))  # -> [[1,3,5],[2,4,6]]
def common_elements(a, b):
    seen = set()
    bset = set(b)
    out = []
    for x in a:
        if x in bset and x not in seen:
            seen.add(x)
            out.append(x)
    return out

# example
print(common_elements([1,2,3,4],[3,4,5,6]))  # -> [3, 4]
def reverse_words(s):
    return " ".join(s.split()[::-1])

# example
print(reverse_words("hello world python"))  # -> "python world hello"
def remove_duplicates_preserve_order(lst):
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

# example
print(remove_duplicates_preserve_order([4,2,4,5,2,3,5,1]))  # -> [4,2,5,3,1]
from collections import Counter

def pairs_with_sum(nums, target):
    cnt = Counter(nums)
    seen = set()
    out = []
    for x in list(cnt):  # iterate unique numbers
        y = target - x
        if y not in cnt:
            continue
        pair = (min(x,y), max(x,y))
        if pair in seen:
            continue
        # if same number, need at least two occurrences
        if x == y and cnt[x] < 2:
            continue
        seen.add(pair)
        out.append(pair)
    return out

# example
print(pairs_with_sum([2,4,3,5,7,8,-1], 6))  # -> [(2,4), (3,3), (-1,7)] (order may vary)
%history -f main.py
