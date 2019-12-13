def golden_ratio(i):
    nums = []
    for i in range(i):
        try:
            nums.append(nums[i - 2] + nums[i - 1])
        except IndexError:
            nums.append(1)
    nums.insert(0, 1)
    print(nums[-1] / nums[-2])


golden_ratio(3)