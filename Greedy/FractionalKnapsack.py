def fractionalknapsack(self, W,Items,n):
    for item in Items:
        item.value /= item.weight
    Items.sort(key = lambda x: x.value, reverse = True)
    res = 0
    i = 0
    while W > 0 and i < n:
        m = min(W,Items[i].weight)
        W -= m
        res += (Items[i].value * m)
        i += 1
    return res 
