#!/usr/bin/env python

def m_sort(lst):
        """
        Sorts a list of integers in increasing order using the merge sort algorithm.

        >>> m_sort([1, 2, 4, 6])
        [1, 2, 4, 6]

        >>> m_sort([3, 2, 1])
        [1, 2, 3]

        >>> m_sort([1])
        [1]

        """

        if (len(lst) == 1):
                return lst
        l1 = lst[:len(lst)//2]
        l2 = lst[len(lst)//2:]

        l1 = m_sort(l1)
        l2 = m_sort(l2)

        return merge(l1, l2)


def merge(l1, l2):
        """
        Merges two lists of integers in increasing order.

        >>> merge([1, 2, 3], [5, 6, 7])
        [1, 2, 3, 5, 6, 7]

        >>> merge([3], [1])
        [1, 3]

        >>> merge([2, 4, 6], [1, 3, 5])
        [1, 2, 3, 4, 5, 6]
        """
        merged = []
        while(len(l1) > 0 and len(l2) > 0):
                if l1[0] > l2[0]:
                        merged.append(l2.pop(0))
                else:
                        merged.append(l1.pop(0))
        while(len(l1)>0):
                merged.append(l1.pop(0))
        while(len(l2)>0):
                merged.append(l2.pop(0))
        return merged

if __name__ == "__main__":
	import doctest
	doctest.testmod()
