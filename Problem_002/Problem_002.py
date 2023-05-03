from functools import reduce

list = [3, 2, 1]
newList = []

def productExceptSelf(lst):
  for index, num in enumerate(lst, 0):
    valAtIndex = num
    lst.pop(index)
    product = reduce(lambda a, b: a * b, lst)
    newList.append(product)
    lst.insert(index, num)
  return newList

if __name__ == '__main__':
  print(productExceptSelf(list))