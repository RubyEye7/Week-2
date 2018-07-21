import time

def search(list, input):
    for i in list:
        if i == input:
            print(input)

start = time.time()

search(range(0, 20000000001), 20000000000)

end = time.time()

print(end-start)
