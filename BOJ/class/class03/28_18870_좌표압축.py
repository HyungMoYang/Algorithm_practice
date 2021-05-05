import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

numbers_elem = sorted(list(set(numbers)))
numbers_dict = dict()

for i in range(len(numbers_elem)):
    numbers_dict[numbers_elem[i]] = i

for num in numbers:
    print(numbers_dict[num], end=" ")
