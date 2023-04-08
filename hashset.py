# first solution

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

# newer solution

class MyHashSet:

    def __init__(self):
        self.__set = set()

    def add(self, key: int) -> None:
        self.__set.add(key)

    def remove(self, key: int) -> None:
        if key in self.__set:
            self.__set.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.__set:
            return True
        else:
            return False
