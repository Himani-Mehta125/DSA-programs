import time

start = time.time()

# Your code
for i in range(1000000):
    pass

end = time.time()

print("Start Time :", start)
print("End Time   :", end)
print("Execution Time :", end - start, "seconds")










import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 3, 8, 2, 1]

start = time.perf_counter()

bubble_sort(arr)

end = time.perf_counter()

print(f"Execution Time: {end - start:.8f} seconds")