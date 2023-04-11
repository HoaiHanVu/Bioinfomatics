def HammingDistance(p, q):
    diff = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            diff += 1
    return diff