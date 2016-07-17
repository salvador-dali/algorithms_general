def failure(pattern):
    """
    KMP failure function
    :param pattern:
    :return:
    """
    i, j = 1, 0
    f = [0] * len(pattern)

    while i < len(pattern):
        if pattern[j] == pattern[i]:
            f[i] = j + 1
            i += 1
            j += 1
        elif j != 0:
            j = f[j - 1]
        else:
            f[i] = 0
            i += 1
    return f