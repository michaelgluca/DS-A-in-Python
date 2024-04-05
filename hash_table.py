class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
        
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

def item_in_common(list1, list2):
    my_dictionary = {}
    for i in list1:
        my_dictionary[i] = True
    for j in list2:
        if j in list1:
            return True
    return False

def find_duplicates(nums):
    nums_counts = {}
    for num in nums:
        nums_counts[num] = nums_counts.get(num, 0) + 1
    duplicates = []
    for num, count in nums_counts.items():
        if count > 1:
            duplicates.append(num)
    return duplicates

def first_non_repeating_char(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1 :
            return char
    return None

def group_anagrams(strings):
    anagrams_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagrams_groups:
            anagrams_groups[canonical].append(string)
        else:
            anagrams_groups[canonical] = [string]
    return list(anagrams_groups.values())

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []