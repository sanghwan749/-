import time
import random
def selectionSort(list):
    for i in range(len(list)):
        min_idx=i
        for j in range(i+1,len(list)):
            if list[min_idx]>list[j]:
                min_idx=j
        list[i], list[min_idx]=list[min_idx],list[i]
def bubbleSort(list):
    n=len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j]> list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
def insertionSort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
def built_in_Sort(list):
    list.sort()
test_list=list(i for i in range(10000))
random.shuffle(test_list)
a_1=time.time()
selectionSort(test_list)
a_2=time.time()
random.shuffle(test_list)
b_1=time.time()
bubbleSort(test_list)
b_2=time.time()
random.shuffle(test_list)
c_1=time.time()
insertionSort(test_list)
c_2=time.time()
random.shuffle(test_list)
d_1=time.time()
built_in_Sort(test_list)
d_2=time.time()
a=a_2-a_1
b=b_2-b_1
c=c_2-c_1
d=d_2-d_1
print('선택정렬:%f' % a)
print('\n버블정렬:%f' % b)
print('\n삽입정렬:%f' % c)
print('\n내장함수:%f' % d)