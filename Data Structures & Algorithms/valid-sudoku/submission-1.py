class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize hash sets for rows, columns, and 3x3 sub-boxes
        # Using defaultdict(set) automatically instantiates a new set for a new key
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        # Make a single pass through the 9x9 board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Ignore empty spaces
                if val == '.':
                    continue
                
                # Identify which 3x3 sub-box the current cell belongs to
                # The board is 9x9, so r // 3 and c // 3 will result in coordinates from (0,0) to (2,2)
                box_idx = (r // 3, c // 3)
                
                # Check for Sudoku rule violations
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_idx]):
                    return False
                
                # Register the value as "seen" in its respective row, column, and sub-box
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        # If we successfully iterate through the board with no violations
        return True