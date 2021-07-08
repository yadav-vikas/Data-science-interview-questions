'''
Given an array of distinct integers, write code to find length of the longest subarray which contains numbers that can be arranged in a continuous sequence.


    
    
For example:


    
    
Input:  arr[] = {10, 12, 11};
    

Output: 3
    


    

Input:  arr[] = {14, 12, 11, 20};
    

Output: 2
    


    

Input:  arr[] = {1, 10, 23, 11, 13, 14, 15, 12, 98}
    

Output: 5
'''

def longestConsecutive( a):
    a = set(a)
    longest = 0
    for i in a:
        if i-1 not in a:
          current = i
          streak = 0
          while i in a:
            i+=1
            streak+=1
            longest = max(longest,streak)
    return longest
  
  print(longestConsecutive([1, 10, 23, 11, 13, 14, 15, 12, 98,21,23,22,26,24,25]))
  #6
  
  print(longestConsecutive([-2, -3, 4, -1, -2, 1, 5, -3]))
  #3
  
  print(longestConsecutive([-1,-2,-3,1,2,3,4,-5,-6,-4]))
  #6
