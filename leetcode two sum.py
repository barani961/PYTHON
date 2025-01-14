
        
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the number and its index
        num_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in num_map:# Check if the complement exists in the dictionary
               
               
                return [num_map[complement], i]    # If it does, return the indices of the complement and the current number
            
            num_map[nums[i]] = i # Store the index of the current number

        return []# Return an empty list if no solution is found


if __name__ == "__main__":
    solution = Solution()
    nums=list(map(int,input(" enter the numbers for the list by space").split()))
    target=int(input("enter the target to check if  sum of 2 num is is equal so that it return the index of two elements:"))
    result = solution.twoSum(nums, target)
    print("Indices:", result)  

