import math
def reverseArray(arr):
    """
        in this method, you should insert a array and the program will reverse the array
        """
    for i in range(math.ceil(len(arr)/2)):
        temp=arr[i]
        arr[i]=arr[len(arr)-1-i]
        arr[len(arr)-1-i]=temp
    print(arr)

ahmad=[1,2,3,4,5,6,7]
reverseArray(ahmad)