list = [1,4,8,3,14,12,20,19]

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]= list[j+1], list[j]
        swapped = True
        if not swapped:
           break
    return list
bubble_sort_output= bubble_sort(list)
print(bubble_sort_output)