
class MyHashMap:

    def __init__(self):
        self.__obj = {}

    def put(self, key: int, value: int) -> None:
        if key in self.__obj:
          self.__obj.update({key: value})
        self.__obj[key] = value

    def get(self, key: int) -> int:
      if key not in self.__obj:
        return -1
      return self.__obj[key]

    def remove(self, key: int) -> None:
      if key not in self.__obj:
        return 
      self.__obj.pop(key) 
      
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
