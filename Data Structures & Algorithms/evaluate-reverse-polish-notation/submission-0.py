class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a copy so we don't mutate the original input array
        arr = tokens[:]
        operators = {"+", "-", "*", "/"}
        
        # Continue resolving until only the final result remains
        while len(arr) > 1:
            for i in range(len(arr)):
                if arr[i] in operators:
                    # The two preceding elements are the operands
                    # a is the left operand, b is the right operand
                    a = int(arr[i-2])
                    b = int(arr[i-1])
                    
                    # Evaluate the sub-expression
                    if arr[i] == "+":
                        res = a + b
                    elif arr[i] == "-":
                        res = a - b
                    elif arr[i] == "*":
                        res = a * b
                    elif arr[i] == "/":
                        # int(a / b) forces float division and truncates towards zero
                        res = int(a / b) 
                        
                    # Replace the evaluated tokens with the stringified result
                    arr[i-2:i+1] = [str(res)]
                    
                    # Break the inner loop to restart the left-to-right scan
                    break 
                    
        return int(arr[0])