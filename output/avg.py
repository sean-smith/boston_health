yices = open('yizces.txt', 'r')
lines = yices.readlines()

sum_not = 0
count_not = 0
sum_boston = 0
count_boston = 0

for i in range(len(lines) - 1):
    if '(' not in lines[i]:
        if 'Not' in lines[i]:
            temp = lines[i+1].split(' ')
            sum_not += float(temp[1])
            count_not += 1
        if 'Census' in lines[i]:
            temp = lines[i+1].split(' ')
            sum_boston += float(temp[1])
            count_boston += 1

yices_avg = open('yizces_avg.txt', 'w')
yices_avg.write("Average for point not in Boston: " + str(sum_not/count_not) + " seconds\n")
yices_avg.write("Average for point in Boston: " + str(sum_boston/count_boston) + " seconds\n")
yices_avg.write("Average for all points: " + str((sum_not + sum_boston)/(count_not + count_boston)) + " seconds")
yices.close()
yices_avg.close()

py = open('python.txt', 'r')
lines = py.readlines()

sum_not = 0
count_not = 0
sum_boston = 0
count_boston = 0

for i in range(len(lines) - 1):
    if '(' not in lines[i]:
        if 'Not' in lines[i]:
            temp = lines[i+1].split(' ')
            sum_not += float(temp[1])
            count_not += 1
        if 'Census' in lines[i]:
            temp = lines[i+1].split(' ')
            sum_boston += float(temp[1])
            count_boston += 1

python_avg = open('python_avg.txt', 'w')
python_avg.write("Average for point not in Boston: " + str(sum_not/count_not) + " seconds\n")
python_avg.write("Average for point in Boston: " + str(sum_boston/count_boston) + " seconds\n")
python_avg.write("Average for all points: " + str((sum_not + sum_boston)/(count_not + count_boston)) + " seconds")
py.close()
python_avg.close()

z3 = open('z3.txt', 'r')
lines = z3.readlines()

sum_not = 0
count_not = 0
sum_boston = 0
count_boston = 0

for i in range(len(lines) - 1):
    if '(' not in lines[i]:
        if 'Not' in lines[i]:
            temp = lines[i+1].split(' ')
            sum_not += float(temp[1])
            count_not += 1
        if 'Census' in lines[i]:
            temp = lines[i+1].split(' ')
            sum_boston += float(temp[1])
            count_boston += 1

z3_avg = open('z3_avg.txt', 'w')
z3_avg.write("Average for point not in Boston: " + str(sum_not/count_not) + " seconds\n")
z3_avg.write("Average for point in Boston: " + str(sum_boston/count_boston) + " seconds\n")
z3_avg.write("Average for all points: " + str((sum_not + sum_boston)/(count_not + count_boston)) + " seconds")
z3.close()
z3_avg.close()




