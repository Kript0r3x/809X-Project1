
import random
import copy
import time
import matplotlib.pyplot as plt

def intersects(a, b):
    return a[0] <= b[1] and b[0] <= a[1]

def before(a, b):
    return a[1] < b[0]

def partition(items, p, r):
    pick = random.randint(p, r)
    items[pick], items[r] = items[r], items[pick]
    intersection = copy.deepcopy(items[r]);
    
    for i in range(p, r):
        if intersects(intersection, items[i]):
            if items[i][0] > intersection[0]:
                intersection[0] = items[i][0]
            if items[i][1] < intersection[1]:
                intersection[1] = items[i][1]

    s = p
    for i in range(p, r):
        if before(items[i], intersection):
            items[i], items[s] = items[s], items[i]
            s += 1

    items[r], items[s] = items[s], items[r]


    t = s + 1
    while t <= i:
        if intersects(items[i], intersection):
            items[t], items[i] = items[i], items[t]
            t += 1
        else:
            i -= 1

    return (s, t)


def fuzzy_sort(items, p, r):
    if (p < r):
        pivot = partition(items, p, r);
        fuzzy_sort(items, p, pivot[0]);
        fuzzy_sort(items, pivot[1], r);



file_path = 'small_overlap.txt'


def read_data(file_path, n):
    items = []
    with open(file_path, 'r') as f:
        for i in range(n):
            line = f.readline()
            if not line:
                break
            item = [float(x) for x in line.split()]
            items.append(item)
    return items

items = read_data(file_path, 50)
# print(items)
# fuzzy_sort(items, 0, len(items)-1)
# print(items)

file_path = 'small_overlap.txt'
num_items = []
time_taken = []

for i in range(10, 1000000, 1000):
    items = read_data(file_path, i)
    start_time = time.time()
    fuzzy_sort(items, 0, len(items)-1)
    end_time = time.time()
    num_items.append(i)
    time_taken.append(end_time - start_time)
    print(f"n={i}, time={end_time - start_time}")
    

file_path = 'all_overlap.txt'
num_items2 = []
time_taken2 = []

for i in range(10, 1000000, 1000):
    items = read_data(file_path, i)
    start_time = time.time()
    fuzzy_sort(items, 0, len(items)-1)
    end_time = time.time()
    num_items2.append(i)
    time_taken2.append(end_time - start_time)
    

plt.plot(num_items, time_taken, label = 'small overlap')
plt.plot(num_items2, time_taken2, label = 'all overlap')
plt.xlabel('Number of Items')
plt.ylabel('Time Taken (Seconds)')
plt.title('Fuzzy Sort Performance')
plt.legend()
plt.show()
