#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

inputNum = 1000
listOfMultiples = []
sum = 0

for i in range(inputNum):
    if (i%3==0 or i%5==0):
        listOfMultiples.append(i)
        print(i)

for i in listOfMultiples:
    sum += i

print(sum)

    