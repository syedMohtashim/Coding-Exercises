# ------------------------------------------------------------------------------
# ********************************* { DAY 06 } *********************************
# ------------------------------------------------------------------------------


# QUESTION: Array Nesting

def _array_nest(ls):
	count = 0
	visited = set()

	for i in range(len(ls)):
		temp = 0
		while i not in visited:
			visited.add(i)
			i = ls[i]
			temp += 1
		count = max(count, temp)

	return count
nums = [5,4,0,3,1,6,2]
nums = [0,1,2]
# print(_array_nest(nums))

# ls = ['abcedahzucs']
# print("".join(sorted(ls)))


# QUESTION: Shifting Letters
# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# --> Explanation1: We start with "abc".
	# After shifting the first 1 letters of s by 3, we have "dbc".
	# After shifting the first 2 letters of s by 5, we have "igc".
	# After shifting the first 3 letters of s by 9, we have "rpl", the answer.

# -->EXPLAINATION2:
	# Input: s = "aaa", shifts = [1,2,3]
	# Output: "gfd"

# https://codedestine.com/shifting-letters-of-string/


def letter_shifting():
	pass




# QUESTION : LEFT-ROTATE
# d = 2 --> Number of rotations
# arr = [1,2,3,4,5] 

def rotateLeft(d, arr):
    n = len(arr)
    
    for i in range(d):
        temp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = temp
    return arr 





def reverse(x):
        if x > -2147483648 or x <2147483647:
        	
	        #Taking absolute of number for reversion logic
	        n = abs(x)
	        rev = 0
	        #Below logic is to reverse the integer
	        while(n > 0):
	            a = n % 10
	            rev = rev * 10 + a
	            n = n // 10
	        #Below case handles negative integer case
	        if(x < 0):
	            return ("-"+str(rev))
	        return int(rev)
        	# x=str(x)
        	# if x[0] == "-":
        	# 	a = x[::-1]
        	# 	return f"{x[0]}{a[:-1]}"
        	# else:
        	# 	return x[::-1]
        else:
        	return 0
        
		

# a = reverse(-1230)


# print(a)

# def rev_func(x):
# 	n = abs(x)
# 	rev = 0
# 	while(n>0):
# 		a = n%10
# 		rev = rev*10 + a
# 		n = n//10
# 	if (x<0):
# 		num = "-"+str(rev)
# 		num = int(num)
# 	else:
# 		num = int(rev)

# 	if num < -2**31 or num > 2**31 -1 :
# 		return 0
# 	else:
# 		return num


# print(rev_func(1534236469))

def rev_func(x):
	n = abs(x)
	# rev = 0
	# while(n>0):
	# 	a = n%10
	# 	rev = rev*10 + a
	# 	n = n//10
	n = str(n)
	rev = n[::-1]
	if (x<0):
		num = "-"+rev
		num = int(num)
	else:
		num = int(rev)

	if num < -2**31 or num > 2**31 -1 :
		return 0
	else:
		return num


print(rev_func(-153))