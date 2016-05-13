ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']

if len(ivan) > len(maria):
    smallerList = maria
    biggerList = ivan
else:
    smallerList = ivan
    biggerList = maria

for i in smallerList:
    if i in biggerList:
        print(i, end=" ")

# make them sets and intersect them
