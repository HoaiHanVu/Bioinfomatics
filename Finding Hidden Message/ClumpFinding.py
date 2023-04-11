def ClumpFinding(text, k, L, t):
    words = []
    for i in range(0, len(text) - L + 1):
        tmp_text = text[i: i + L]
        freq_map = FrequencyMap(tmp_text, k)
        for key in freq_map:
            if freq_map[key] >= t:
                words.append(key)
    return set(words)

def FrequencyMap(text, k):
    freq = {}
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        if pattern in freq:
            freq[pattern] += 1
        else:
            freq[pattern] = 1
    return freq