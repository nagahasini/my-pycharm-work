def partition(arr, low, high):
    i = low
    j = high
    pi = arr[low]

    while i < j:
        while i < high and arr[i] <= pi:
            i += 1
        while j > low and arr[j] > pi:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[low] = arr[low], arr[j]
    return j


class Solution:

    def quicksort(self, arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            self.quicksort(arr, low, pi - 1)
            self.quicksort(arr, pi + 1, high)
