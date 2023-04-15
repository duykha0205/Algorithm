from collections import Counter


def all_substrs(s):
    return [[s[j:j+i] for j in range(len(s) - i + 1)] for i in range(1, len(s))]

def sherlockAndAnagrams(s):
    # Write your code here
    substring_counts = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = ''.join(sorted(s[i:j]))  # sort the substring to make anagrams identical
            if substring not in substring_counts:
                substring_counts[substring] = 1
            else:
                substring_counts[substring] += 1

    # Next, we count the number of anagramic pairs of substrings
    num_anagramic_pairs = 0
    for count in substring_counts.values():
        # Count the number of pairs that can be formed from count substrings
        num_anagramic_pairs += count * (count-1) // 2

    return num_anagramic_pairs

def j(ll):
    c = Counter()
    s = 0
    for lst in ll:
        for e in lst:
            q = ''.join(sorted(e))
            c[q] += 1
    for e in c:
        s += int(c[e]*(c[e]-1)/2)
    return s

s = "abbba"
print(j(all_substrs(s)))