def char_frequencies(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

string = "data structures and algorithms"
print(char_frequencies(string))