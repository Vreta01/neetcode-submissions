class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char not in ('+','-','*','/'):
                stack.append(int(char))
            elif len(stack) < 2:
                break
            elif char == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 + num2
                stack.append(total)
            elif char == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                total = num2 - num1
                stack.append(total)
            elif char == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 * num2
                stack.append(total)
            elif char == '/': 
                num1 = stack.pop()
                num2 = stack.pop()
                total = int(num2 / num1)
                stack.append(total)
        if len(stack) == 1:
            return stack.pop()
        else:
            return None