# Binary search
import time
def binary_search(arr, x, debug=False, sorted_array=False): # use hint debug=True for debug output
    if not sorted_array:
        arr.sort()

    low=0
    high = len(arr) - 1
    mid = 0
    itterations = 0

    start_time = time.time()

    while low<=high:
        itterations +=1
        mid = (high + low) //2

        if debug: # use hint for optimization
            print(f"Ітерація {itterations}: low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")  # Output after eteration

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            end_time = time.time()
            print(f"⏱️ Час виконання: {end_time - start_time:.8f} секунд")
            return itterations, arr[mid]

    end_time = time.time()
    print(f"⏱️ Час виконання: {end_time - start_time:.8f} секунд")
    
    # Визначення "число">=x
    upper_element = arr[low] if low<len(arr) else None
    return itterations, upper_element

arr = [0.1, 3.05, 5.23, 0.08, 10, 32.12, 1.15, 0.18, 20.20, 89.22, 24.005, 44.99]
arr.sort()  # Якщо раптом не відсортували, перестраховуємось arr.sort()
x = 3.05
result = binary_search(arr, x, debug=True, sorted_array=True) # use hint for debug and sort
if result[1] is not None:
  print(f"Елемент знайшовся на {result[0]} iтерацію, межа верхня: {result[1]}")
else:
  print(f"Елемент не знайшовся на {result[0]} ітерацію, можливо верхня межа відсутня.")

