import sys

def main(argv):
    a = list(argv)
    a.sort()
    result = list()
    for i, v in enumerate(a):
      if v != "0":
        result.append(v)
        result = result + a[:i]
        result = result + a[i+1:]
        break
    for v in result:
      print(v, end="")

if __name__ == '__main__':
    main(sys.argv[1])
