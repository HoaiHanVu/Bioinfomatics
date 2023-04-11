def FrequencyMap(text, k):
    freq = {}
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        if pattern in freq:
            freq[pattern] += 1
        else:
            freq[pattern] = 1
    return freq

def FrequentWord(text, k):
    words = []
    freq_map = FrequencyMap(text, k)
    max_val = max(freq_map.values())
    for key in freq_map:
        if freq_map[key] == max_val:
            words.append(key)
    return words