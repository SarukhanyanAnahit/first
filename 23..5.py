def get_cont(fname):
    f = open(fname)
    return f.read()

def reverse(mstr):
    return mstr[::-1]

def each(mstr):
    tmp = ""
    for el in mstr.split():
        tmp += el[::-1] + " "
    return tmp.strip()

def title(mstr):
    return mstr.title()

def upper(mstr):
    return mstr.upper()

def up_low(mstr):
    d = {"vowels": "", "conson": ""}
    for k in mstr:
        if k.lower() in "aeiou":
            d["vowels"] += k
        elif k.isalpha():
            d["conson"] += k
    return "Vowels: " + d["vowels"] + "\nConsonants: " + d["conson"]

def write_into_file(fname, content):
    f = open(fname, 'a')
    f.write(content + '\n\n')

fil = get_cont("h.txt")

write_into_file("result1.txt", reverse(fil))
write_into_file("result1.txt", each(fil))
write_into_file("result1.txt", title(fil))
write_into_file("result1.txt", upper(fil))
write_into_file("result1.txt", up_low(fil))
