import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, x):
    for num in arr:
        if num == x:
            return True
    return False

def binary_search(arr, x):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


 
 
def fib_search(arr, x):
    n = len(arr)
    # Initialize fibonacci numbers
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
 
    # fibM is going to store the smallest
    # Fibonacci Number greater than or equal to n
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
 
    # Marks the eliminated range from front
    offset = -1
 
    # while there are elements to be inspected.
    # Note that we compare arr[fibMm2] with x.
    # When fibM becomes 1, fibMm2 becomes 0
    while (fibM > 1):
 
        # Check if fibMm2 is a valid location
        i = min(offset+fibMMm2, n-1)
 
        # If x is greater than the value at
        # index fibMm2, cut the subarray array
        # from offset to i
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
 
        # If x is less than the value at
        # index fibMm2, cut the subarray
        # after i+1
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        # element found. return index
        else:
            return True
 
    # comparing the last element with x */
    if(fibMMm1 and arr[n-1] == x):
        return True
 
    # element not found. return -1
    return False




def measure_execution_time(search_function, arr, x):
    temp = 0
    counter = 0
    while counter < 5: 
        start_time = time.perf_counter_ns()
        result = search_function(arr, x)
        end_time = time.perf_counter_ns()
        counter += 1
        temp += (end_time - start_time)
    print(result)
    return str(round(temp // 5))
        

def main():
    step_size = 10
    max_size = 10000
    algorithms = [linear_search, binary_search,fib_search]
    results = {algorithm.__name__: [] for algorithm in algorithms}
    for n in range(step_size, max_size + step_size, step_size):
            arr = sorted(random.sample(range(n * 5), n))
            x = random.randint(1, n * 5)
            print('-------------------')
            for algorithm in algorithms:
                time = measure_execution_time(algorithm, arr, x)
                print('iteartions:%d' %n)
                print(f"{algorithm.__name__} average execution times:"+ time + 'ns')
                if n >= 10:
                    results[algorithm.__name__].append(int(time))

                
    x = list(i for i in range(10, max_size + step_size, step_size))
    plt.plot(x, results['linear_search'], 'ro--', linewidth=0.5, markersize=1,label = 'linear')
    plt.plot(x, results['binary_search'], 'go--', linewidth=0.5, markersize=1,label = 'binary')
    plt.plot(x, results['fib_search'], 'bo--', linewidth=0.5, markersize=1,label = 'fib')
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()
