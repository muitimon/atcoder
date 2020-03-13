import sys
import requests
import json

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
  s = ""
  for c in argv:
    c_num = ord(c)
    if c_num != 43:
      s = s + c
  endpoint = "http://challenge-server.code-check.io/api/hash?q=" + argv
  try:
    res = requests.get(endpoint).json()
    print(res["hash"])
  except json.decoder.JSONDecodeError as error:
    pass
  #  for i, v in enumerate(argv):
  #      print("argv[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    main(sys.argv[1])
