data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
#data = [104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 187, 188, 191]
#data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 187, 188, 191]

#data = [104, 105, 110, 120, 130, 150, 160,170, 183, 185, 187, 188, 191, 350, 360]
#data = [1041, 1052, 1101, 1201, 1301, 1501, 1608, 1736, 1906, 1988]


min_valid = 100
max_valid = 200
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del data[:stop]
print(data)

#this is the another method to deleting data from list.
start = 0
for index in range(len(data) -1, -1, -1):
    if data[index] <= max_valid:
        # we have the index of the last item to keep.
        # set 'Start' to the postion of the first.
        # item to delet, which is 1 after 'index'
        start = index + 1
        break

print(start)
del data[start:]
print(data)


