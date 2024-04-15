# data = "7, 3, 5, 8, 0, 2, 5, 4"
# data = [int(i) for i in data.split(", ")]
# moves=0
# largest=0
# while data != []:
#     for i in range(0, len(data)-1):
#         if data[i]==0:
#             del data[:i]
#             moves+=1
#         if data[i]>largest:
#             largest=i
#     if data[largest]%2==0:
#         data[largest]=data[largest]-2
#         moves+=1
#     elif data[largest]%2==1:
#         data[largest]=data[largest]-1
#         moves+=1
# print(moves)

data = "5, 0, 6, 0, 4"

data = [int(i) for i in data.split(", ")]

count = 0
while data:
    count += 1
    if 0 in data:
        zcount = data.count(0)
        start = 0
        if zcount > 1
