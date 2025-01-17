# The sum of the squares of the first ten natural numbers is 1**2 + 2**2 + ... + 10**2 = 385.
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10) = 55**2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


sum = 0
sum_sqr = 0

for i in range(1, 101):
    sum += i
    sum_sqr += i * i

print(sum * sum - sum_sqr)
