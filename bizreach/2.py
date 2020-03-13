import sys

def main(argv):
  m = int(argv[-1])
  dic = {}
  for i in argv[:-1]:
    num, word = i.split(":")
    num = int(num)
    if m % num == 0:
      dic[num] = word
  if dic:
    for key, value in sorted(dic.items()):
      print(value, end="")
  else:
    print(m)

if __name__ == '__main__':
    main(sys.argv[1:])
