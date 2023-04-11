def ReverseComplement(text):
    s = ""
    for i in range(len(text)):
        if text[i] == "A":
            s += "T"
        elif text[i] == "T":
            s += "A"
        elif text[i] == "C":
            s += "G"
        elif text[i] == "G":
            s += "C"
    return s[::-1]