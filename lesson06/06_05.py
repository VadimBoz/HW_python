# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
#  взятых из трёх списков (по одному из каждого)

# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# in
# 10 True

# out
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий',
# 'автомобиль сегодня веселый', 'город позавчера утопичный']

# in
# 10 False

# out
# ['автомобиль ночью мягкий', 'огонь вчера веселый',
#  'автомобиль позавчера веселый', 'город вчера утопичный', 'лес сегодня зеленый',
# 'дом вчера яркий', 'автомобиль вчера зеленый', 'огонь позавчера яркий', 'огонь где-то утопичный',
#  'автомобиль где-то мягкий']

# st1 = 'время дело день  рука работа слово местовопрос лицо глаз страна друг дом голова система город  земля власть машина закон час'
# st1=st1.split()

from random import choices, sample
while True:
    n = int(input("Введите число шуток: "))
    if n < 1:
        print("введите число более 0")
    else:
        break

while True:
    flag = int(input("1 - уникальные слова,  0  - с  повторами: "))
    if  flag==0 or flag==1:
        break
    else:
        print("введите число 1  или 0")



def read_file(filename):  # чтение данных из файла--------------------------------------------------
    with open(filename, "r", encoding="utf-8") as my_f:
        data = [_.replace("\n", '') for _ in my_f.readlines()]
    return data
# end ------------------------------------------------------------------------------------------------


st = [read_file('words1.txt'), read_file(
    'words2.txt'), read_file('words3.txt')]
max_n = min(len(st[0]), len(st[1]), len(st[2]))
n = max_n if n >= max_n and flag == True else n

# res=[]
# for i in range(3):
#     if flag==False:
#        temp = choices(st[i], k=n) #не уникальные элемены
#     else:
#        temp = sample(st[i], k=n)  #уникальные элемены
#     res.append(temp)

res = [choices(st[i], k=n) if flag == False else sample(st[i], k=n)
       for i in range(3)]

fun = [res[0][x] + " " + res[1][x] + " " + res[2][x] for x in range(n)]
print(*enumerate(fun, start=1), sep="\n")
