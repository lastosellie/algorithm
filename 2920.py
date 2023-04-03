'''
3
21 Junkyu
21 Dohyun
20 Sunyoung
'''
n = int(input())
customer = []
for i in range(n):
    age, name = list(input().split())
    customer.append([int(age), name])
print(customer)
def swap(i, j):
    tmp = customer[i]
    customer[i] = customer[j]
    customer[j] = tmp

for i in range(n - 1):
    for j in range(0, n - 1 - i):
        #print(j, j + 1)
        if customer[j + 1][0] < customer[j][0]:
            swap(j, j + 1)
        #elif customer[j + 1][0] == customer[j][0] and customer[j + 1][1] < customer[j][1]:
        #    swap(j, j + 1)

for age, name in customer:
    print(str(age) + ' ' + name)
'''
20 Sunyoung
21 Junkyu
21 Dohyun
'''