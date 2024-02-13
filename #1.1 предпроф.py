#1
fin=open('students.csv','r',encoding='utf-8')
title=fin.readline()
print(title)
students=[x.strip().split(',') for x in fin]
balsum={}
balcnt={}
cnt=0
#x[0]-номер ученика
#x[1]-ФИО
#x[2]-номер проекта
#x[3]-класс
#x[4]-оценка
for x in students :
    if x[4]!='None':
        if x[3]in balsum:
            balsum[x[3]]+=int(x[4])
            balcnt[x[3]]+=1
        else:
            balsum[x[3]]=int(x[4])
            balcnt[x[3]]=1
    fio=x[1].split()
    if fio[0]=='Хадаров' and fio[1]=='Владимир':
        print('Ты получил :',x[4],'за проект -',x[2])
fout=open('student_new1.csv','w',encoding='utf-8')
fout.write(title)
for x in students:
    if x[4]=='None':
        x[4]=f'{balsum[x[3]]/balcnt[x[3]]:.3f}'

for x in students:
    s=','.join(x)+'\n'
    fout.write(s)
fout.close()
    
