#QUICK-SORT
def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)

def partition(A, p, r):
    pivot = A[r]
    smaller = p
    for j in range(p, r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller += 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller

#HEAP-SORT
def maxHeapify(A, heapSize, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= heapSize - 1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heapSize - 1 and A[r] > A[largest]:
        largest = r
    if i != largest:
        A[largest], A[i] = A[i], A[largest]
        maxHeapify(A, heapSize, largest)

def buildMaxHeap(A):
    heapSize = len(A)
    for i in range(heapSize//2, -1, -1):
        maxHeapify(A, heapSize, i)

def heapSort(A):
    buildMaxHeap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        maxHeapify(A, i, 0)

#COUNTING-SORT
def countSort(A):
    output = [0] * len(A)
    count = [0] * 1002

    for i in range(0, len(A)):
        count[A[i]] += 1

    for i in range(1, 1002):
        count[i] += count[i - 1]

    i = len(A) - 1
    while i >= 0:
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1
        i -= 1

    for i in range(0, len(A)):
        A[i] = output[i]