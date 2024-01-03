from collections import Counter
import random
import math

nums = []
i = 0

while i < 150:
    nums.append(random.randint(0, 100))
    i += 1

def measures_of_central_tendency(nums):
    mean = math.fsum(nums)/len(nums)

    counter = Counter(nums)
    mode = counter.most_common(1)[0][0]

    median = None
    sorted_nums = sorted(nums)
    x = math.floor(len(sorted_nums) / 2)
    if len(nums) / 2 == 0:
        median = (sorted_nums[x] + sorted_nums[x + 1]) / 2
    else:
        median = sorted_nums[x]

    isSymmetry = None
    if mode == median == mean:
        isSymmetry = 'Распределение является симмметричным.'
    else:
        isSymmetry = 'Распределение является асиммметричным.'

    print('average:', mean)
    print('median: ', median)
    print('mode:', mode)
    print(isSymmetry)


measures_of_central_tendency(nums)

