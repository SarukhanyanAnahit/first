def list_unnest(ml):
    while True:
        tmp = []
        flag = False
        for el in ml:
            if type(el)==int or type(el)==str:
                tmp.append(el)
            elif type(el)==list:
                tmp.extend(el)
                flag = True
        ml = tmp
        if not flag:
            break
    return tmp

print(list_unnest([4, 5, 'barev', [1, 2, 3, 'arev', [9,8, [6,[9, 8], 5]],6]]))
