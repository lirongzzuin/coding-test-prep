def merge_sorted_arrays(nums1, nums2):
    i, j = 0, 0
    merged = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    return merged

# 테스트 실행
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
print(merge_sorted_arrays(nums1, nums2))
