""""""
"""
Write and test the method for flattering the nested list

case 1
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]

case 2
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]

"""

def flattened_list(l: list) -> list:
  flattened = []
  for item in l:
    if isinstance(item, list):
      flattened.extend(flattened_list(item))
    else:
      flattened.append(item)
  return flattened

"""
Write and test the method for picking highest and lowest frequency in the list

input = [1,2,3,1,1,2,4,5,5,6,4]
output = [1,3]

Write and test the method for picking highest and lowest frequency in the list

input = [1,2,3,1,1,2,4,5,5,6,4,6]
output = [1,3]

input = [1,2,2,2,3,1,1,4,5,5,6]
output = [1, 3]

input = [1,2,2,2,3,1,1,4,5,5,6.'a']

"""
from typing import List

def find_frequency(l : List[int]) -> list:
  frequency_dict = {}

  for item in l:
    if isinstance(item, int):
      frequency_dict.setdefault(item, 1)
      frequency_dict[item] += 1
      # if item in frequency_dict:
      #   frequency_dict[item] += 1
      # else:
      #   frequency_dict[item] = 1
    else:
      raise Exception('invalid input')

  max_frequency = max(frequency_dict.values())
  min_frequency = min(frequency_dict.values())

  highest_frequency_list = [key for key, value in frequency_dict.items() if value == max_frequency]
  lowest_frequency_list = [key for key, value in frequency_dict.items() if value == min_frequency]

  return [min(highest_frequency_list), min(lowest_frequency_list)]

if __name__ == '__main__':
  l1 = [[1, 1], 2, [1, 1]]
  l2 = [1, [4, [6]]]
  l3 = [1, [4, [6]], 'a', 'b']
  l4 = [[], [], [], [[]]]
  print(flattened_list(l3))


  l5 = [1,2,2,2,3,1,1,4,5,5,6]
  l6 = [1,2,2,2,3,1,1,4,5,5,6,'a']
  print(find_frequency(l5))



