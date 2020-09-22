def bsearch(l, value):
    lo, hi = 0, len(l)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if l[mid] < value:
            lo = mid + 1
        elif value < l[mid]:
            hi = mid - 1
        else:
            return mid
    return -1


l = [0,1,2,3,4,5,6]
x = 6
print(bsearch(l,x))

# how??  to go to this puzzle? https://app.finxter.com/learn/computer/science/159
Solution
6

Explanation
How to find a value in a sorted list?

A naive algorithm compares each element in the list against the searched value. For example, consider a list of 1024 elements. The naive algorithm performs in the order of 1024 comparisons in the worst-case. In computer science, the worst-case runtime complexity can be expressed via the Big-O notation. We say, for n elements in a list, the naive algorithm needs O(n) comparisons. The function O defines the asymptotical worst-case growth.

The function bsearch is a more effective way to find a value in a sorted list. For n elements in the list, it needs to perform only O(log(n)) comparisons. In the same example, Bsearch requires only up to log(1024)=10 comparisons. Hence, Bsearch is much faster.

Why is Bsearch so fast?

The naive algorithm compares all elements with the searched value. Instead, Bsearch uses the property that the list is sorted in an ascending manner. It checks only the element in the middle position between two indices lo and hi.
If this middle element is smaller than the searched value, all left-hand elements will be smaller as well because of the sorted list. Hence, we set the lower index lo to the position right of the middle element.
If this middle element is larger than the searched value, all right-hand elements will be larger as well. Hence, we set the upper index hi to the position left of the middle element.
Only if the middle element is exactly the same as the searched value, we return the index of this position.
This procedure is repeated until we find the searched value or there are no values left. In each loop iteration, we reduce the search space, i.e., the number of elements between lo and hi, by half.