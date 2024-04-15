data = list(map(int, input().split()))
data.sort()
A=data[0]
B=data[1]
C=data[-1]-A-B
print(A, B, C)