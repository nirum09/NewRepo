class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None

def SortedArrtoBST(sorted_array):

    if not sorted_array:
        return None
    mid=(len(sorted_array))/2
    root=sorted_array[mid]
    

