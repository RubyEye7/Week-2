
def process(name):
    f = open(name)
    answer = []
    for line in f:
        answer.append(line[:-1].split(':'))
    return answer

def averageHeight(array):
    x = 0
    for i in array:
        x += int(i)
    return x / len(array)

def heightRange(array):
    height1 = '72'
    height2 = '78'
    for current_height in array[4]:
        count = 0
        if current_height <= height2 and current_height >= height1:
            count += 1
        else:
            count += 0
    return count


if __name__ == '__main__':
    filename = "athletes.txt"
    data = process(filename)
    print("THE DATA IS:")
    array = []
    for item in data:
        print(item)
        array.append(item[4])
    print("The average height is")
    print(averageHeight(array))
    print(heightRange(array))
