def canJump(nums):
    max_reachable = 0  # Tracks the farthest index we can reach

    for i, jump in enumerate(nums):
        # If the current index is beyond what is reachable, return False
        if i > max_reachable:
            return False

        # Update the farthest reachable index
        max_reachable = max(max_reachable, i + jump)

        # If we can reach or exceed the last index, return True
        if max_reachable >= len(nums) - 1:
            return True

    return False

# Example usage
nums = [2, 3, 1, 1, 4]
print(canJump(nums))  # Output: True

nums = [3, 2, 1, 0, 4]
print(canJump(nums))  # Output: False
