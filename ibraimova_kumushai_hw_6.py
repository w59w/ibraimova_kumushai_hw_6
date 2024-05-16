def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Исходный список:", unsorted_list)

sorted_list_bubble = bubble_sort(unsorted_list.copy())
print("Отсортированный список (метод пузырьковой сортировки):", sorted_list_bubble)

sorted_list_selection = selection_sort(unsorted_list.copy())
print("Отсортированный список (метод сортировки выбором):", sorted_list_selection)

element_to_find = 25
index = binary_search(sorted_list_bubble, element_to_find)
if index != -1:
    print(f"Элемент {element_to_find} найден по индексу {index}")
else:
    print(f"Элемент {element_to_find} не найден")
