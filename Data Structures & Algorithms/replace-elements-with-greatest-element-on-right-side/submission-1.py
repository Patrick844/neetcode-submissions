class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)-1):
            greatest_element = max(arr[i+1:])
            arr[i] = greatest_element
        arr[-1] = -1
        return arr

        