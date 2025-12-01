"""
Problem: Directions Reduction
Difficulty: 5 kyu
Source: Codewars
Link: https://www.codewars.com/kata/550f22f4d758534c1100025a

Description:
Simplify a path by removing adjacent opposite directions (NORTH/SOUTH, EAST/WEST).
Removing one pair may expose new adjacent opposites that can also be removed.

Examples:
    ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] -> ["WEST"]
    ["NORTH", "SOUTH", "EAST", "WEST"] -> []
    ["NORTH", "WEST", "SOUTH", "EAST"] -> ["NORTH", "WEST", "SOUTH", "EAST"]

Key Concepts:
- Stack data structure (LIFO - Last In, First Out)
- Pattern matching
- Cascading effects (removing one pair can expose another)

Time Complexity: O(N) - single pass through array
Space Complexity: O(N) - worst case, no directions cancel

My Approach:
1. Use a stack to track uncanceled directions
2. For each direction:
   - If stack is empty, push it
   - If top of stack is opposite to current direction, pop (they cancel)
   - Otherwise, push current direction
3. Stack automatically handles cascading cancellations because we always
   compare with the most recently added (uncanceled) direction

Edge Cases Handled:
- Empty input -> returns []
- Single direction -> returns [direction]
- No cancellations possible -> returns original array
- All directions cancel -> returns []
- Cascading cancellations -> handled naturally by stack
"""

def dirReduc(directions):
    """
    Reduce a path by removing adjacent opposite directions.
    
    Args:
        directions (list): List of direction strings ("NORTH", "SOUTH", "EAST", "WEST")
    
    Returns:
        list: Simplified list of directions
    """
    # Mapping of each direction to its opposite
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    
    stack = []
    
    for direction in directions:
        # If stack has elements and top is opposite to current direction
        if stack and stack[-1] == opposites[direction]:
            stack.pop()  # Cancel them out
        else:
            stack.append(direction)  # Keep this direction
    
    return stack


# Test cases
if __name__ == "__main__":
    # Basic cancellation
    assert dirReduc(["NORTH", "SOUTH"]) == []
    assert dirReduc(["EAST", "WEST"]) == []
    
    # Single direction
    assert dirReduc(["NORTH"]) == ["NORTH"]
    
    # No cancellations
    assert dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]) == ["NORTH", "WEST", "SOUTH", "EAST"]
    
    # Simple cancellation
    assert dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == ["WEST"]
    
    # All cancel
    assert dirReduc(["NORTH", "SOUTH", "EAST", "WEST"]) == []
    
    # Cascading cancellation
    assert dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]) == ["WEST", "WEST"]
    
    # Same direction repeated
    assert dirReduc(["NORTH", "NORTH"]) == ["NORTH", "NORTH"]
    
    # Empty input
    assert dirReduc([]) == []
    
    print("✅ All tests passed!")






