nums1 = [1, 1, 2, 5, 6, 5, 7, 8, 5, 8, 6, 7]
nums2 = [1, 2, 2, 7, 6, 5, 7, 3, 5, 8, 6, 4]

def remove_dublicates(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    result.sort()
    return result

print(remove_dublicates(nums1))
print(remove_dublicates(nums2))