from itertools import combinations


# first solution

def find_zero_sum_groups(arr, n):
    combos = sorted(sorted(c)
                    for c in combinations(set(arr), n) if sum(c) == 0)
    return combos if len(combos) > 1 else combos[0] if combos else "No combinations" if arr else "No elements to combine"


# pytonic solution

def find_zero_sum_groups(arr, n):
    if not arr:
        return "No elements to combine"
    res = {c for c in combinations(set(arr), n) if not sum(c)}
    if len(res) == 1:
        return sorted(res.pop())
    return sorted(map(sorted, res)) if res else "No combinations"
