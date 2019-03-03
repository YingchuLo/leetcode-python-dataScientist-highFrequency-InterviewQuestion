# 611 valid triangle number
# hint: a+b >= c
# 1. sort data 
# 2. double loop to get 2 number (a,b)
# 3. the 3rd num would be >= a+b
# 4. how to get all the number >= a+b ? Binarysearch

# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

class Solution(object):

  def binarySearch(self, nums, l, r, target):
    while l < r:
      mid = round((l+r) / 2)
      if nums[mid] >= target:
        r = mid
      else:
        l = mid + 1
    return l if target <= nums[l] else l+1

  # This algorithm will give us O(n^2logn) time complexity.
  def triangleNumber(self, nums):
    nums.sort()
    result = 0
    for i in range(len(nums)-2):
      for j in range(i+1, len(nums)-1):
        k = self.binarySearch(nums, j+1, len(nums)-1, nums[i]+nums[j])
        result += (k-1) - j
    return result

# 412 Fizz Buzz
# Print out numbers from 1 to n. 
# However, for multiple of 3, print out Fizz. For multiple of 5, print out Buzz.
class Solution:
    def fizzBuzz(self, n):
        ans = []

        for num in range(1,n+1):

            div_by_3 = (num % 3 == 0)
            div_by_5 = (num % 5 == 0)

            if div_by_3 and div_by_5:
                # Divides by both 3 and 5, add FizzBuzz
                ans.append("FizzBuzz")
            elif div_by_3:
                # Divides by 3, add Fizz
                ans.append("Fizz")
            elif div_by_5:
                # Divides by 5, add Buzz
                ans.append("Buzz")
            else:
                # Not divisible by 3 or 5, add the number
                ans.append(str(num))

        return ans

#697 Degree of an Array
class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count={},{},{}
        for i,x in enumerate(nums):
            if x not in left:    left[x]=i
            right[x]=i
            count[x]=count.get(x,0)+1
            
        ans=len(nums)
        degree=max(count.values())
        for x in count:
            if count[x] == degree:
                ans=right[x]-left[x]+1
            
        return ans        

# 1 two sum
class Solution:
    def twoSum(self, nums, target):
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[j] == target - nums[i]:
                    return i, j
        print("No two sum solution")

# 2 add two numbers
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
# 4 Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, A,B):
        m, n= len(A), len(B)
        if m > n:
            A,B,m,n=B,A,n,m
        if n == 0:
            print("ValueError")
        half_len=(m+n+1)/2
        imin, imax= 0, m
        
        while imin <= imax:
            i=int(round((imin+imax) /2))
            j=int(round(half_len-i))
            if i < m and B[j-1] > A[i]:
                imin=i+1
            elif i>0 and A[i-1] > B[j]:
                imax=i-1
            else:
                if i== 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1],B[j-1])
                
                if (m+n) % 2 ==1:
                    return max_of_left
                
                if i==m: min_of_right=B[j]
                elif j ==n : min_of_right=A[i]
                else: min_of_right = min(A[i],B[j])
    
                return ( float(max_of_left) + float(min_of_right) ) / 2
# 5 Longest Palindromic(回文) Substring
# https://leetcode.com/problems/longest-palindromic-substring/
#Example 1:
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

#Example 2:
#Input: "cbbd"
#Output: "bb"
#version1
class Solution:
    def expandAroundCenter(self, s, left, right):
        L=left
        R=right
        while L >= 0 and R < len(s) and s[L] == s[R] :
            L=L-1
            R=R+1
        return R-L-1
        
    def longestPalindrome(self, s):
        if len(s) < 1:
            return ""
        
        start = 0
        end = 0
        len1 = 0
        len2 = 0
        len3 = 0
        
        for i in range(0,len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s,i,i+1)
            len3 = max(len1, len2)
            if(len3 > end - start ):
                start = int(i - ( len3 - 1 ) / 2)
                print(start)
                end = int(i + len3 / 2)
                print(end)
        return s[start:end+1]
