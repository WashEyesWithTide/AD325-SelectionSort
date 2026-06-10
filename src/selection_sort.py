def selection_sort(arr: list[int]) -> list[int]:
    """
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

if __name__ == "__main__":
    print("Hello World")
    print(selection_sort([64, 34, 25, 12, 22, 11, 90]))