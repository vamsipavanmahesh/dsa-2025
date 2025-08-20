# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. 
# Return -1 if the target is not in the array.


def find_first_occurence(arr, target):
  left = 0
  right = len(arr) - 1
  ans = -1

  while(left <= right):
    mid = (left + right) // 2

    if arr[mid] == target:
      ans = mid
      right = mid - 1
    else:
      left = mid + 1

  return ans

print(find_first_occurence(arr=[1, 3, 3, 5, 8, 8, 10], target=8))