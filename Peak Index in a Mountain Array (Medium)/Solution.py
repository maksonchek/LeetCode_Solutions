class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l+r)//2
            if m != 0 and m != len(arr)-1:
                if (arr[m-1] <= arr[m] and arr[m] <= arr[m + 1]):
                    l = m + 1
                elif (arr[m-1] >= arr[m] and arr[m] >= arr[m + 1]):
                    r = m - 1
                elif (arr[m-1] < arr[m] and arr[m] > arr[m + 1]):
                    return m
            else:
                if m == 0:
                    if arr[m+1] >= arr[m]:
                        l = m + 1
                    else:
                        return m
                elif m == len(arr)-1:
                    if arr[m-1] >= arr[m]:
                        r = m - 1
                    else:
                        return m

        return l

