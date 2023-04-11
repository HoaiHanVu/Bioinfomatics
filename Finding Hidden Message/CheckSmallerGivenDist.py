def CheckSmallerGivenDist(a, b, d):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            if count > d:
                return False
    if count <= d:
        return True