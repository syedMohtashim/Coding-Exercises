# ------------------------------------------------------------------------------
# ********************************* { DAY 09 } *********************************
# ------------------------------------------------------------------------------


# Question : New year chaos !
# Hacker-rank

def sol(arr):
	bribe = 0
	for i in range(len(arr)-1, 0, -1):
		if arr[i] != i+1:
			if arr[i-1] == i+1:
				bribe += 1
				arr[i-1], arr[i] = arr[i], arr[i-1]
			elif arr[i-2] == i+1:
				bribe += 2
				arr[i-2], arr[i-1], arr[i] = arr[i], arr[i], arr[i-2]
			else:
				print('Too Chaotic')
				return
	print(bribe)

def minimumBribes(q):
    # Write your code here
    bribe = 0
    for i in range(len(q)-1, 0, -1):
        if q[i] != i+1:
            if q[i-1] == i+1:
                bribe+=1
                q[i-1] , q[i] = q[i] , q[i-1]
            elif q[i-2] == i+1:
                bribe+=2
                q[i-2] , q[i-1]= q[i-1], q[i]
            else:
                print('Too chaotic')
                return 
                
    print(bribe)
# minimumBribes([2, 5, 1, 3, 4])


# def checkMagazine(mag, note):
#     hash_map = {}
#     for i in mag:
#         hash_map[i] = False
#     count = 0
#     for j in note:
#         if j in mag:
#             if hash_map[j] == False:
#                 hash_map[j] = True
#                 count+=1
#             else:
#                 break
#         else:
#             break
#     if count == len(note):
#         print('Yes')
#     else:
#         print('No')

from collections import Counter
def checkMagazine(magazine, note):
    # if Counter(note) - Counter(magazine) == {}:
    #     return 'Yes'
    # else:
    #     return 'No'
    # print(Counter(note))
    # print(Counter(magazine))
    note_dict = {}
    mag_dict = {}
    count = 0
    for i in note:
        if i in note_dict:
            note_dict[i] +=1
        else:
            note_dict[i] = 1

    for j in magazine:
        if j in mag_dict:
            mag_dict[j] +=1
        else:
            mag_dict[j] = 1

    print(f"NOTES: {note_dict}")
    print(f"MAGAZINES: {mag_dict}")

    for k1, v1 in note_dict.items():
        for k2, v2 in mag_dict.items():
            if v1 - v2 ==0:
                count+=1
            else:
                break

    print(count)
    

# mag = ['two', 'times', 'three', 'is', 'not', 'four']
# note = ['two', 'times', 'two', 'is', 'four']
mag = input("Enter Mag: ")
mag = mag.split()
note = input("Enter note: ")
note = note.split()
print(checkMagazine(mag, note))