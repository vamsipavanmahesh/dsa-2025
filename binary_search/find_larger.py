# Given an array of integers sorted in increasing order and a target,
# find the index of the first element in the array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.

# bruteforce
def find_larger(arr, target):
  length = len(arr) - 1
  for i in range(0, length):
    if arr[i] >= target:
      return i
  return -1

print(find_larger(arr=[1, 3, 3, 5, 8, 8, 10], target=4))

#optimal

def find_boundary_larger(arr, target):
  left = 0
  right = len(arr) - 1
  boundary = -1

  while(left <= right):
    mid = (left + right) // 2

    if(arr[mid] >= target):
      boundary = mid
      right = mid - 1
    else:
      left = mid + 1
  
  return boundary

print("optimal algo")
print(find_larger(arr=[1, 3, 3, 5, 8, 8, 10], target=4))
