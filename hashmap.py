# Time complexity: O(1) on average and O(n) worst case
     
class MyHashMap:
  def __init__(self):
    self.__map = {}

  def put(self, key: int, value: int) -> None:
    self.__map[key] = value 

  def get(self, key: int) -> int:
    if key not in self.__map:
      return -1
    return self.__map[key]

  def remove(self, key: int) -> None:
    if key not in self.__map:
      return None
    del self.__map[key]
