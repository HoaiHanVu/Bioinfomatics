def PatternCount(text, pattern):
    count = 0
    length = len(pattern)
    for i in range(0, len(text) - length + 1):
        if text[i: i + length] == pattern:
            count += 1
    return count