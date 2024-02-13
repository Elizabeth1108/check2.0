#4
from random import choice
fin=open('students.csv','r',encoding='utf-8')
title=fin.readline()
students=[x.strip() for x in fin]
cnt=0
#x[0]-номер ученика
#x[1]-ФИО
#x[2]-номер проекта
#x[3]-класс
#x[4]-оценка
simbol='qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM'
for i in range(1,len(students)):
    x=students[i].split(',')
    fio=x[1].split()
    login=fio[0]+'_'+fio[1][0]+fio[2][0]
    password=''.join(choice(simbol) for _ in range(8))
    students[i]=students[i]+','+login+','+password
fout=open('students_password.csv','w',encoding='utf-8')
fout.write(title+',login,'+',password,')
for x in students:
    fout.write(x+'\n')
    print(x)
    
    
