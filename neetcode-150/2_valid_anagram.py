# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

### Solution 1: Sorting Approach (O(n log n) time, O(n) space)

def is_anagram_sorting(input1, input2):
  return sorted(input1) == sorted(input2)

### Solution 2: Using hash map (Two dictionaries)

def is_anagram_hashmap(input1, input2):
  # Early exit if lengths are different
  if len(input1) != len(input2):
    return False
    
  dict1 = {}
  dict2 = {}

  for i in range(len(input1)):
    dict1[input1[i]] = dict1.get(input1[i], 0) + 1
  
  for i in range(len(input2)):
    dict2[input2[i]] = dict2.get(input2[i], 0) + 1
  
  return dict1 == dict2

### Solution 3: Optimized hash map (Single dictionary)

def is_anagram_optimized(input1, input2):
  # Early exit if lengths are different
  if len(input1) != len(input2):
    return False
    
  char_count = {}
  
  # Count characters from first string
  for char in input1:
    char_count[char] = char_count.get(char, 0) + 1
  
  # Decrement counts from second string
  for char in input2:
    if char not in char_count:
      return False
    char_count[char] -= 1
    if char_count[char] == 0:
      del char_count[char]
  
  return len(char_count) == 0

print("Original hash map solution:")
print(is_anagram_hashmap("racecar", "carrace")) # True
print(is_anagram_hashmap("jar", "jam")) # False

print("\nOptimized hash map solution:")
print(is_anagram_optimized("racecar", "carrace")) # True
print(is_anagram_optimized("jar", "jam")) # False
