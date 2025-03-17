from search import Search
from constants import *

def main():
  search = Search()
  search.read_armor(armor_path)
  print(search.armor_data)

if __name__ == "__main__":
  main()
