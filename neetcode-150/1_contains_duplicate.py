# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


### Solution 1:

# Using extra Space, with Dict

def find_duplicate(nums):
  dict = {}

  length_of_input = len(nums)

  for iterator in range(0, length_of_input):
    if(dict.get(nums[iterator]) == 1):
      return True
    dict[nums[iterator]] = 1

  return False

print(find_duplicate([1,2,3,4])) # False
print(find_duplicate([1,1,2,3,4])) # True

### Solution 1:
#### Using sort, if we don't consider space used in sorting

def find_duplicate_sort(nums):
  sorted_input = sorted(nums)

  length_of_input = len(sorted_input)

  for iterator in range(1, length_of_input):
    if sorted_input[iterator-1] == sorted_input[iterator]:
      return True
  
  return False

print(find_duplicate_sort([1,2,3,4])) # False
print(find_duplicate_sort([1,1,2,3,4])) # True