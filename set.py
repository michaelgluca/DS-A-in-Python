# a function that removes all the duplicates from the list using a set and then prints the updated list.
def remove_duplicates(my_list):
    return list(set(my_list))

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)

# a function that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.
def has_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

print(has_unique_chars('abcdefg')) 


# find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)


# a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0
    
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1 
            
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1 
            longest_sequence = max(longest_sequence, current_sequence)
    return longest_sequence

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )