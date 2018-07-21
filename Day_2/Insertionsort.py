
def insertion_sort(all):
    if len(all) <= 1:
        return all
    for i in range(2, len(all)):
        key = all[i]
        card = i - 1
        while card >= 0 and all[card] > key:
            all[card + 1] = all[card]
            card -= 1
        all[card + 1] = key
    return all

print(insertion_sort([3,7,10,-1,6,67,59,3267,3750]))
