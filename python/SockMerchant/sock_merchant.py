def sockMerchant(n, ar):
    # create frequency map 
    freq_map = {}
    for a in ar:
        freq_map[a] = freq_map[a] + 1 if a in freq_map else 1
    pair_map = {a: freq_map[a] // 2 for a in freq_map}
    filtered = {k:v for (k,v) in pair_map.items() if v > 0}
    return sum(filtered.values())


if __name__ == "__main__":
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    pairs = sockMerchant(n, ar)
    print('John can make {} pair of socks'.format(pairs))
