# here we need find the first occurrrence of value in sorted array
# Input: arr = [false, false, true, true, true]

# Output: 2

# Explanation: The first true's index is 2.

def find_boundary(arr):
  left = 0
  right = len(arr) - 1
  flag  = -1

  while(left <= right):
    mid = (left+right)//2
    
    if arr[mid]:
      flag = mid
      right = mid - 1
    else:
      left = mid + 1

  return flag


print(find_boundary([False, False, False, True, True, True]))


def find_boundary_bruteforce(arr):

  for i in range(0, len(arr)-1):
    if arr[0] == True:
      return i

  return -1

print ("brute force variant")
print(find_boundary([False, False, False, True, True, True]))
