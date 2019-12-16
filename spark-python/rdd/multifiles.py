import sys
from os import walk

 
if __name__ == "__main__":
  mypath = "in/test-data"
  f = []
  for (dirpath, dirnames, filenames) in walk(mypath):
    print(filenames)
