def median(values):
    values = sorted(values)
    size = len(values)
    if size%2 == 0:
        left = values[int(size/2 -1)]
        right = values[int(size/2-1)]
        return(left+right)/2
    else:
        return values[int(size/2)]
roots2 = lambda val: (val **.5, -(val **.5))
