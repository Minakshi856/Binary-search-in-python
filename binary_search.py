
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

size = int(input("Enter the size of the array: "))
user_arr = [int(input(f"Enter element {j+1}: ")) for j in range(size)]
search = int(input("Enter the element you want to search for: "))

user_arr.sort()
result = binary_search(user_arr, search)

print("\n" + "-" *30)
print(f"Sorted Array used for search: {user_arr}")

if result != -1:
    print(f"Element {search} found at index {result}.")
else:
    print(f"Element {search} not found in the list.")

print("-" * 30)
print("Binary Search Complexity Analysis:")
print(f"Input size (n): {len(user_arr)}")
print(" Time Complexity: (Big O)")
print(" Best Case: O(1)")
print(" Avg/Worst Case: O(log n)")
print(" Space Complexity: O(1)")

