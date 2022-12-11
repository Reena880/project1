import time
import sys
MAX_SIZE = sys.maxsize

############# Bubble Sort #############

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]

                drawData(data, ['lightgreen' if x == i or x == i+1 else '#3b4249' for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])


############# Insertion Sort #############

def insertion_sort(data, drawData, timeTick):
    for i in range(1,len(data)):
        value = data[i]
        j = i
        while value <= data[j-1] and j != 0:
            drawData(data, ['lightgreen' if x == j else '#3b4249' for x in range(len(data))])
            time.sleep(timeTick)

            data[j],data[j-1] = data[j-1],data[j]
            j -= 1

        drawData(data, ['lightgreen' if x == j else '#3b4249' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])


############# Selection Sort #############

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)-1):
        pos = i
        last = MAX_SIZE
        for j in range(i+1, len(data)):
            drawData(data, [('lightyellow' if x == j else ('lightblue' if x == i else '#3b4249')) for x in range(len(data))])
            time.sleep(timeTick)

            if data[j] < data[i] and data[j] < last:
                pos = j
                last = data[j]

        drawData(data, [('lightgreen' if x == pos else ('lightblue' if x == i else '#3b4249')) for x in range(len(data))])
        time.sleep(timeTick)
        temp = data[i]
        data[i] = data[pos]
        data[pos] = temp

    drawData(data, ['green' for x in range(len(data))])


############# Merge Sort #############

def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data)-1, drawData, timeTick)

    drawData(data, ['green' for x in range(len(data))])
    time.sleep(timeTick)

def merge_sort_alg(data, left, right, drawData, timeTick):
    if left >= right:
        return
    middle = (left + right)//2

    merge_sort_alg(data, left, middle, drawData, timeTick)
    merge_sort_alg(data, middle+1, right, drawData, timeTick)
    merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, ['#3b4249' for x in range(len(data))])
    time.sleep(timeTick)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]
    
    leftIdx, rightIdx = 0,0

    for i in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[i] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[i] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[i] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[i] = rightPart[rightIdx]
            rightIdx += 1

        drawData(data, ['lightblue' if x == i else '#3b4249' for x in range(len(data))])
        time.sleep(timeTick)


############# Quick Sort #############

colordata = []

def partition(data,low,high, drawData, timeTick):
    i = ( low-1 )
    pivot = data[high]
    for j in range(low , high):
        if data[j] <= pivot:
            i = i+1
            data[i],data[j] = data[j],data[i]

        for x in range(len(colordata)):
            if x == i:
                colordata[x] = '#ff0000'
            elif i < x < high:
                colordata[x] = 'lightyellow'
            elif x == high:
                colordata[x] = 'lightblue'
            else:
                colordata[x] = '#3b4249'

        drawData(data, colordata)
        time.sleep(timeTick)

    data[i+1],data[high] = data[high],data[i+1]
    return ( i+1 )

def quickSort(data,low,high, drawData, timeTick):
    if low < high:
        pi = partition(data,low,high, drawData, timeTick)
        quickSort(data, low, pi-1, drawData, timeTick)
        quickSort(data, pi+1, high, drawData, timeTick)

def quick_sort(data, drawData, timeTick):
    global colordata
    colordata = ['#3b4249' for x in range(len(data))]
    quickSort(data, 0, len(data)-1, drawData, timeTick)
    drawData(data, ['green' for x in range(len(data))])


############# Heap Sort #############

colordata = []  

def heapify(data, n, i, drawData, timeTick):
    largest = i
    l = 2*i
    r = 2*i + 1

    if l < n and data[largest] < data[l]:
        largest = l

    if r < n and data[largest] < data[r]:
        largest = r
        
    if largest != i:
        data[i], data[largest] = data[largest], data[i]

        drawData(data, ['lightblue' if x == i or x == largest else colordata[x] for x in range(len(data))])
        time.sleep(timeTick)

        heapify(data, n, largest, drawData, timeTick)


def heap_sort(data, drawData, timeTick):
    global colordata

    colordata = ['#3b4249' for x in range(len(data))]

    n = len(data)
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick)
    
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]

        drawData(data, ['lightyellow' if x == i or x == 0 else colordata[x] for x in range(len(data))])
        time.sleep(timeTick)
        # colordata[i] = 'green'

        heapify(data, i, 0, drawData, timeTick)

    drawData(data, ['green' for x in range(len(data))])

