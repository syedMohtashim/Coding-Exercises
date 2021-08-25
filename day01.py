#   // Maximum and minimum of an array using minimum number of comparisons //

ls = [12,32,45,190,78,9,14,21,7000]


# if lenght is even
if(len(ls)%2 ==0):
	minimum = max(ls[0], ls[1])
	maximum = min(ls[0], ls[1])

	# looping value 2 because first 2 values of index (0  and 1) are selected so start from index 2 i.e 3rd value
	i = 2

# if length is odd
else:
	minimum = maximum = ls[0]

	# looping value 1 because compairing with 1 only
	i = 1
n=len(ls)


while(i < n-1):
	if ls[i] < ls[i+1]:
		minimum = min(minimum, ls[i])
		maximum = max(maximum, ls[i+1])
	else:
		minimum = min(minimum, ls[i+1])
		maximum = max(maximum, ls[i])

	i+=2

print("Maximum Value: ", maximum)
print("Minimum Value: ", minimum)


