def merge_array(arr1: list, arr2: list) -> list:
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    print(merged)
    return merged


"""
Given a sorted rotated array. Find an element in the array. Print -1 if element does not exist else print the position.
 Eg 4,6,8,99,1,2 : Find 99. Solution: 3
"""


def find_element_in_sorted_rotated_array(nums: list, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

def read_file():
    with open('test.txt') as file:
        word_dict = {}
        for line in file:
            print(line, end='')
            word_list = line.split(' ')
            for word in word_list:
                word = word.replace('\n','')
                word_dict.setdefault(word, 0)
                word_dict[word] += 1
    print(word_dict)

if __name__ == '__main__':
    arr1 = [1, 3, 5, 8, 9, 12, 12, 17]
    arr2 = [2, 4, 6, 8, 12]
    merge_array(arr1, arr2)

    # arr3 = [4, 5, 6, 8, 99, 1, 2 ]
    # arr4 = [7, 9, 12, 17, 1, 2, 3, 4, 5, 6]
    # target = 4
    # print(f'input arr: {arr4}')
    # print(f'Find: {target}')
    # print(f'Solution: {find_element_in_sorted_rotated_array(arr4, target)}')

    # read_file()
