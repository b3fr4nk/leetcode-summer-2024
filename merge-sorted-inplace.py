def merge(nums1,m, nums2,n ):
    target = m+n - 1
    p1 = m - 1
    p2 = n - 1
    while target >= 0:
        if p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[target] = nums1[p1]
                p1 -= 1
            else:
                nums1[target] = nums2[p2]
                p2 -= 1
        elif p1 < 0:
            nums1[target] = nums2[p2]
            p2 -= 1
        elif p2 < 0:
            nums1[target] = nums1[p1]
            p1 -= 1
        else:
            return
        target -= 1
