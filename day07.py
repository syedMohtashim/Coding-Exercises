word = 'GlXk@o@M(!YxywBIeotSxXstwa'
temp = ''
for i in word.lower():
	if word.lower().count(i) == 1:
		temp+='('
	else:
		temp+=')'
# print(temp)


def find_outlier(integers):
    # e_ls = []
    # o_ls = []
    # for i in range(len(integers)):
    #     if integers[i]%2==0:
    #         e_ls.append(integers[i])
    #     else:
    #         o_ls.append(integers[i])
    # if len(e_ls)<len(o_ls):
    #     return e_ls[0]
    # else:
    #     return o_ls[0]

    # ------> OR <--------
    
    even = list(filter(lambda x: x%2 ==0 , integers))
    return even[0] if len(even) == 1 else list(set(integers)-set(even))



# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))

def even_index(ls):
    # for i in range(len(ls)):
    #     if sum(ls[:i]) == sum(ls[i+1:]):
    #         return(i)
    # return-1
    r = [i for i in range(len(ls)) if sum(ls[:i]) == sum(ls[i+1:])]
    return r[0] if r else -1


# print(even_index([1,2,3,4,5,1,2,3,4]))


def anagrams(w1, w2):
    ls = []
    match = sorted(w1)
    for i in w2:
        if match == sorted(i):
            
            ls.append(i)
    return ls
# print(anagrams('abba',['abcd','bnvc']))



# ------------------------------------------------------------------------------
# ********************************* { DAY 07 } *********************************
# ------------------------------------------------------------------------------

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal"
# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"
def interpret(string):
    temp = ''
    for i in range(len(string)):
        if string[i].isalpha():
            temp+=str(string[i])
        elif string[i] == '(' and string[i+1] == ')':
            temp+='o'

    return str(temp)


print(interpret("I l()ve G()D , ()()()H MY G()D!!!"))




# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20

# https://www.youtube.com/watch?v=cevaICIEyjs

def twoCitySchedCost(Dict):
    pass