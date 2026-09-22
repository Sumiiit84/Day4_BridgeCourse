
n = 1234
reversed = 0
while n > 0:
    nums = n % 10
    reversed = reversed * 10 + nums
    n = n // 10
    
print(reversed)
    