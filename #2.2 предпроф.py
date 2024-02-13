#2
fin=open('students.csv','r',encoding='utf-8')
title=fin.readline()

students=[x.strip().split(',') for x in fin]

cnt=0
#x[0]-номер ученика
#x[1]-ФИО
#x[2]-номер проекта
#x[3]-класс
#x[4]-оценка
for i in range(1,len(students)):
    for j in range(i,0,-1):
        x=students[j]
        if students[j][4]<students[j-1][4]:
            students[j],students[j-1]=students[j],students[j-1]
        else:
            break
print(students)
cnt=0
print('10 класс:')
for x in students:
    fio=x[1].split()
    if x[4]=='5' and '10'in x[3]:
        cnt+=1
        print(cnt,'место: ',fio[1][0],'.',fio[0],sep='')
    if cnt==3:
        break
