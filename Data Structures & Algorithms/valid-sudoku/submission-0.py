class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check all rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
                    
        # Check all columns
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
                    
        # Check all 3x3 sub-boxes
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                # Calculate the starting points for the current 3x3 grid
                start_r = box_row * 3
                start_c = box_col * 3
                
                # Traverse the 3x3 grid
                for i in range(3):
                    for j in range(3):
                        val = board[start_r + i][start_c + j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)
                            
        # If no duplicates were found, the board is valid
        return True