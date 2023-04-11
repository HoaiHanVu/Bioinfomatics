def FrequencyMap(text, k):
    freq = {}
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        if pattern in freq:
            freq[pattern] += 1
        else:
            freq[pattern] = 1
    return freq