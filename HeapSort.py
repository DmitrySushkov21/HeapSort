class HeapSort(object):
    def __init__(self):
        self.iteration_counter = 0

    def sort(self, arr):
        n = len(arr)
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

        return arr

    def heapify(self, arr, n, i):
        largest_element = i
        left_element = 2 * i + 1
        right_element = 2 * i + 2
        if left_element < n and arr[i] < arr[left_element]:
            largest_element = left_element

        if right_element < n and arr[largest_element] < arr[right_element]:
            largest_element = right_element

        if largest_element != i:
            arr[i], arr[largest_element] = arr[largest_element], arr[i]
            self.heapify(arr, n, largest_element)

        self.iteration_counter += 1
