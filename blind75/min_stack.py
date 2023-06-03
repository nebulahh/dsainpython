class MinStack:
  def __init__(self):
    self.stack = []
    self.len = -1

  def push(self, val: int) -> None:
    self.stack.append(val)
    self.len += 1

  def pop(self) -> None:
    self.stack.pop()
    self.len -= 1

  def top(self) -> int:
    return self.stack[self.len]

  def getMin(self) -> int:
    return min(self.stack)
