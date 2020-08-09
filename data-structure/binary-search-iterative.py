data=[2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
targeted_search=27

def binary_search_iterative(data,targeted_search):
    low=0
    high=len(data)
    while low <=high:
        mid =(low+high)//2
        print(mid)
        if targeted_search==data[mid]:
            print(data[mid])
            return True
        elif targeted_search <data[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

binary_search_iterative(data,targeted_search)