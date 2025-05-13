# 1
# def msum(mstr):
#     m = mstr.split()
#     total = 0
#     for el in m:
#         if el.isdigit():
#             total += int(el)
#     return total
#
# print(msum("assghahsj 45 dsff9ds5 45566"))

# 2
# def strings(mstr):
#     m = mstr.split()
#     total = 0
#     for el in m:
#         if el.isalpha():
#             total +=1
#     return total
#
# print(strings("assghahsj 45 dsff9ds5 45566"))
#
# 3.
# def middle(*args):
#     count = 0
#     dsum = 0
#     for el in args:
#         if type(el) == int:
#             count += 1
#             dsum += el
#     if count == 0:
#         return 0
#     return dsum / count

# 4
# def middle(a, b):
#     return a + b, a - b, a * b, a / b if b != 0 else "division by zero"
#
# print(middle(42, 2))
# print(middle(6, 0))

# 5
# def up_st(mstr):
#     nmstr = ""
#     for el in mstr:
#         if 97 <= ord(el) <= 122:
#             nmstr += chr(ord(el) - 32)
#         else:
#             nmstr += el
#     return nmstr
#
# print(up_st("barev arevik 45, DG"))

# 6
# def low_st(mstr):
#     nmstr = ""
#     for el in mstr:
#         if 65 <= ord(el) <= 90:
#             nmstr += chr(ord(el) + 32)
#         else:
#             nmstr += el
#     return nmstr
#
# print(low_st("nothing is FOREVER DG"))
#
# 7
# def tit_st(nm):
#     sep = nm.split()
#     result = []
#     for el in sep:
#         if el:
#             first = el[0].upper()
#             rest = el[1:]
#             result.append(first + rest)
#     return " ".join(result)
#
# print(tit_st("andzrev u andzrev 79"))

# 8
# def rev(mstr):
#     return mstr[::-1]
# print(rev("anhayt, anmit"))

# 9
# def substring(text, start, end):
#     return text[start:end]
# print(substring("good bye", 2,4))

# 10
# def longest(mstr):
#     m=mstr.split()
#     a=""
#     for el in m:
#         if len(el)>len(a):
#             a=el
#     return a
#
# print(longest("storm wind luck another"))

# 11
# def most_used(mstr):
#     for el in mstr:
#         if count:
#             a=el
#     return m

# 12
# def longest(mstr):
#     m=mstr.split()
#     a=0
#     for el in m:
#         if len(el)>a:
#             a=el
#     return m

# 13
# def change(mstr, a):
#     return mstr[a], mstr[-a]
#
# print(change("liza hakobyan", 4))

# 14 chka
# 15.
# def is_palindrome(n):
#     x = str(n)
#     if x == x[::-1]:
#         return True
#     else:
#         return False

# print(is_palindrome(787))

# 16
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
#
# def nearest_palindrome(n):
#     if is_palindrome(n):
#         return n
#     lower = n - 1
#     upper = n + 1
#
#     while True:
#         if is_palindrome(lower):
#             return lower
#         if is_palindrome(upper):
#             return upper
#         lower -= 1
#         upper += 1
#
#
# print(nearest_palindrome(123))
# print(nearest_palindrome(787))
# print(nearest_palindrome(1000))

# 17
# def prod(n):
#     ms=str(n)
#     mult= int(ms[0])*int(ms[-1])
#     return mult

# print(prod(458))
# 18
# def s_count(l):
#     count=0
#     for st in l:
#         if type(st)==str:
#             count+=1
#     return count

# print(s_count(["adahs", 45, "dshfdhdjf54", 7899]))

# 19
# def nmax(n):
#     tmax=0
#     for num in n:
#         if type(num)==str:
#             continue
#         if type(num)==int and num>tmax:
#                 tmax=num
#     return tmax
# print(nmax([4, 78, 96, "barev", "okay", 65, (1, 8, 45), [45, 65]]))

# 20
# def evens(l):
#     ev_list=[]
#     for el in l:
#         if type(el)==int and el%2==0:
#             ev_list.append(el)
#     return ev_list
# print(evens([48, 12, 96, 3, 5, 9, "sdsdddd", [4, 8, 9], (1, 8)]))

# 21
# def mid(lis):
#     it = 0
#     num_sum = 0
#     for el in lis:
#         if type(el) == int or type(el) == float:
#             it += 1
#             num_sum += el
#     avg = num_sum / it
#     return avg

# print(mid([8, 2, 6, 3, "sdsdddd"]))

# 22
# def st_l(l):
#     lengths=[]
#     for el in l:
#         lengths.append(len(el))
#     return lengths
# print(st_l(["horse", "sunset", "and life", "is gorgeous"]))

# 23
# def desc_numb(l):
#     desc = []
#     for el in l:
#         if type(el) == int:
#             desc.append(el)
#     desc.sort(reverse=True)
#     return desc

# print(desc_numb([4, 98, 5, 6, "sdsd"]))

# 24
# def len_sort(l):
#     strings = [el for el in l if type(el) == str]
#     strings.sort(key=len, reverse=True)
#     return strings

# print(len_sort(["arev", 78, "gghvjh", "abb"]))

# 25
# def most_vowels(l):
#     max_count = 0
#     result = ""

#     for word in l:
#         count = 0
#         for letter in word.lower():
#             if letter in "aeiou":
#                 count += 1
#         if count > max_count:
#             max_count = count
#             result = word
#     return result

# print(most_vowels(["ashxet", "zambia", "vard", "ananas"]))

# 26
# def most_words(sentences):
#     max_count = 0
#     result = ""

#     for sentence in sentences:
#         word_count = len(sentence.split())
#         if word_count > max_count:
#             max_count = word_count
#             result = sentence
#     return result

# print(most_words(["We suffer more often in imagination than in reality.",
# "Ignorance is the cause of fear."]))

# 27
# def largest(sentence):
#     words = sentence.split()
#     numbers = []
#     for word in words:
#         if word.isdigit():
#             numbers.append(int(word))
#     if numbers:
#         return max(numbers)
# print(largest("anush 45 asjsjas 96 kdks 2"))

# 28
# def dict_list(l):
#     max_v = 0
#     max_person = None
#     for el in l:
#         if el['age'] > max_v:
#             max_v = el['age']
#             max_person = el
#     return max_person
#
# print(dict_list([
#     {'name': 'Lily', 'surname': 'Holmes', 'age': 58},
#     {'name': 'Ani', 'surname': 'Bakunc', 'age': 79},
#     {'name': 'Vard', 'surname': 'Caxkunc', 'age': 29}
# ]))

# 29
# def dict_list(l):
#     l.sort(key=lambda x: x['scores'])
#     return l
# print(dict_list([
#     {'name': 'Lily', 'surname': 'Holmes', 'age': 18, 'scores': 90},
#     {'name': 'Ani', 'surname': 'Bakunc', 'age': 19, 'scores': 92},
#     {'name': 'Vard', 'surname': 'Caxkunc', 'age': 20, 'scores': 85}
# ]))

# 30
# def university(dl):
#     tmp=0
#     anun=None
#     for un in dl:
#         if len(un['name'])>tmp:
#             tmp=len(un['name'])
#             anun=un
#     return anun['name']
#
# print(university([
#     {'name': 'HAPH GM', 'place': 'Erevan', 'was founded': 1933},
#     {'name': 'EPH', 'place': 'Erevan', 'was founded': 1999},
#     {'name': 'SHPH', 'place': 'Gyumri', 'was founded': 1933}]))