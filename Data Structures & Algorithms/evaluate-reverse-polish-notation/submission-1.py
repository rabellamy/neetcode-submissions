class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            # If token is not an operator, it's a number. Push to stack.
            if token not in operators:
                stack.append(int(token))
            else:
                # Token is an operator. Pop the two most recent operands.
                # Crucial: The first popped element is the RIGHT operand (b).
                b = stack.pop()
                a = stack.pop()
                
                # Evaluate and push the result back onto the stack
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # int() applied to float division guarantees truncation toward zero
                    stack.append(int(a / b))
                    
        # The final remaining element in the stack is our evaluated answer
        return stack[0]