class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for val in tokens:
          if val not in '+-/*':
            stack.append(int(val))
          else:
            r, l = stack.pop(), stack.pop()
            if val == '+':
              stack.append(l + r)
            elif val == '-':
              stack.append(l - r)
            elif val == '*':
              stack.append(l * r)
            else:
              stack.append(int(float(l)/r))
        return stack.pop()
