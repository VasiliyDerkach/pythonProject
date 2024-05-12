grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=sorted(list(students))
grades_avg=[]
for grades_itm in grades:
    grades_avg.append(sum(grades_itm)/len(grades_itm))
tabel=dict(zip(students,grades_avg))
#print(grades_avg)
print(tabel)
