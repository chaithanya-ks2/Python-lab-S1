year = int(input("Enter the year: "))
limit = int(input("Enter the limit: "))

def isLeap(year):
    if (year%400==0) or (year%4==0 and year%100!=0):
        return True
    else:
        return False

leaps = []
for i in range(year, limit+1):
    if isLeap(i):
        leaps.append(i)
        break
for k in range(i+4, limit+1, 4):
    leaps.append(k)
    
print(leaps)



