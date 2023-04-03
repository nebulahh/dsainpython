# this is the design of an hashset 

class MyHashSet:

  def __init__(self):
    self.__key = []
 
  def add(self, key: int) -> None:
    if key in self.__key:
      return
    self.__key.append(key)

  def remove(self, key: int) -> None:
    if key not in self.__key:
      return 
    self.__key.remove(key)

  def contains(self, key: int) -> bool:
    if key in self.__key:
      return True
    return False
