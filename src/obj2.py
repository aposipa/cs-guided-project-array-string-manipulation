# nums = [1,2,3]

# def triple_in_place(nums):
#     for index in range(len(nums)):
#         nums[index] = nums[index] * 3

# print(nums)
# triple_in_place(nums)
# print(nums)

nums = [1,2,3]
x = []
def triple_out_place(nums):
    new_nums = [None] * len(nums)
    for index in range(len(nums)):
        new_nums[index] = nums[index] * 3

    return new_nums

print(x)
print(nums)
x = triple_out_place(nums)
print(nums)
print(x)