def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


num_list = [12,34,56,78,41,123,1,83,22,43,17,23,66,8,3,90]
selection_sort(num_list)
print(num_list)