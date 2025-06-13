def rec_unnest(ml):
    if not ml:
        return ml
    new=[]
    for el in ml:
        if type(el)==list:
            new.extend(rec_unnest(el))
        else:
            new.append(el)
    return new

print(rec_unnest([4, 5, 'barev', [1, 2, 3, 'arev', [9,8, [6,[9, 8], 5]],6]]))
