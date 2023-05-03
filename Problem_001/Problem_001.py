def ifAddUptoK():
  list = [10, 15, 2, 7]
  k = 17

  for i in list:
    for j in range(len(list)):
      if i + list[j] == k:
        print(True, i, list[j])

if __name__ == '__main__':
    ifAddUptoK()