import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

# Heap Sort Function

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)

# Quick Sort Function

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

# function to perform quicksort

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

# Merge Sort Function

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0     
    j = 0    
    k = l     
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# Selection Sort Function

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if(lst[j] < lst[min]):
                min = j
        lst[i], lst[min] = lst[min], lst[i]

# Function to do insertion sort

def insertionSort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# BubbleSort Function

def bubblesort(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            return


name = "insertion sort"
name1 = "bubble sort"
name2 = "selection sort"
name3 = "merge sort"
name4 = "quick sort"
name5 = "heap sort"

# list of elements per each sorting algorithm

elements = "As1/output/insertion.txt"
elements1 = "As1/output/bubble.txt"
elements2 = "As1/output/selection.txt"
elements3 = "As1/output/merge.txt"
elements4 = "As1/output/quick.txt"
elements5 = "As1/output/heap.txt"

# list of times for each sorting algorithm


def timefunction(file,sort):
    with open(file, "w") as f:
        for i in range(1, 500):
            a = randint(0, 10*i, 10*i)
            start = time.time()
            sort(a)
            end = time.time()
            f.write(f"{len(a)} {end-start}\n")



def timefunction_2(file, sort):
    with open(file, "w") as f:
        for i in range(1, 500):
            a = randint(0, 10 * i, 10 * i)
            n = len(a)
            start = time.time()
            sort(a, 0, n-1)
            end = time.time()
            f.write(f"{len(a)} {end-start}\n")



# timefunction(elements,insertionSort)
# timefunction(elements1,bubblesort)
# timefunction(elements2,selection_sort)
timefunction_2(elements3,mergeSort)
timefunction_2(elements4,quickSort)
timefunction(elements5,heapSort)


