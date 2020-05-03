import smtplib, ssl
import random
numplayers=5
valuelist=[]
book={''
'Мерлин -':'-',
'Убиец -':'-',
'Пърсивал -':'-',
'Мордред -':'-',
'Добър селянин -':'-',
"Оберон -":"-",
"Добър селянин 2 -":"-",
"Моргана -":"-",
"Добър селянин 3 -":"-"
}
players=["Ради","Ина","Денис","Димо","Деси","Веско","Ани"]
counter=0
random.shuffle(players)
for role in book:
    book[role]=players[counter]
    print(role,book[role])
    counter=counter+1
    if counter==len(players):break
