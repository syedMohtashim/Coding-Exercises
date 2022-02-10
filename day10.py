# ================================
# | ATTEMPT 1 of arrayManipulation|
# ================================

def arrayManipulation(n, queries):
    ls = []
    for i in range(n):
        ls.append(0)
    for j in range(len(queries)):
        a,b = queries[j][0]-1 , queries[j][1]
        val = queries[j][-1]
        
        for k in range(a,b):
            ls[k]+=val
    return max(ls)
# ================================
# | ATTEMPT 2 of arrayManipulation|
# ================================

# ======================================================
# In this attempt , I will use the prefix-sum-algorithm |
# --> https://iq.opengenus.org/prefix-sum-array/        |
# ======================================================
def arrayManipulation(n, queries):
    ls = [0]*(n+1)
    for q in queries:
        a = q[0]-1
        b = q[1]
        k = q[2]

        ls[a]+=k
        ls[b]-=k

    sum_of_arr , max_val = 0,0
    for i in ls:
        sum_of_arr+=i
        if sum_of_arr>max_val:
            max_val = sum_of_arr

    print(max_val)



# ALL are HackerRank Problems

# There is a string, , of lowercase English letters that is repeated 
# infinitely many times. Given an integer, , 
# find and print the number of letter a's 
# in the first  letters of the infinite string.


def repeatedString(s, n):
    count=0
    target = 'a'
    q = n//len(s)
    r = n%len(s)
    
    for char in s:
        if char == target:
            count+=1
    count = count*q
    for i in s[:r]:
        if i == target:
            count+=1
            
    return count



# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valley = sea_level = 0
    for i in path:
        if i=='U':
            sea_level+=1
        else:
            sea_level-=1
        if i=='U' and sea_level==0:
            valley+=1
    return valley


#================================
# HackerRank: Frequency Queries||
#================================
# ref: https://stackoverflow.com/questions/52489613/hackerrank-frequency-queries
def freqQuery(queries):
    freq_table = {}
    res = 0
    ls = []
    for q in queries:
        if q[0] == 1:
            if q[1] in freq_table:
                freq_table[q[1]] +=1
            else:
                freq_table[q[1]] = 1
            
        elif q[0] == 2:
            if q[1] in freq_table.keys():
                if freq_table[q[1]]>0:
                    freq_table[q[1]]-=1
            else:
                continue
        elif q[0] == 3:
            for key,value in freq_table.items():
                if value == q[1]:
                    res = 1
                    ls.append(1)
                else:
                    ls.append(0)
                    
                # print(res)
    print(ls)

        
# freqQuery([(1,1) ,(1,1), (1,1) ,(1,4) ,(1,5), (2,1),(3,2)])


#================================
# HackerRank: Time Conversion||
#================================

def timeConversion(s):
    am_pm = s[-2:]
    time = s[:-2]
    
    if am_pm == 'AM' and time[:2] == '12':
        return '00'+time[2:]
    elif am_pm == 'AM' and time[:2] != '12':
        return time
    elif am_pm == 'PM' and time[:2] == '12':
        return time
    else:
        return str(int(time[:2])+12) + s[2:8]




#=================================
# HackerRank: Game of Thrones - I||
#=================================

from collections import Counter
def gameOfThrones(s):
    # Write your code here
    a = Counter(s)
    b = 0
    for i,j in a.items():
        if j%2 !=0:
            b+=1
    if b==1 or b==0:
        return 'YES'
    else:
        return 'NO'


def conv(s):
    count = 0
    dic = Counter(s)
    yes = 0
    no = 0
    for k,val in dic.items():
        if len(s)%2 == 0:
            if val%2 != 0:
                no+=1
                # return 'NO'
                # break
            else:
                yes+=1
                # return 'YES'
                
        else:
            if val%2 != 0:
                count+=1
            else:
                continue
    if count > 1 or no>0:
        return 'NO'
    else:
        return 'YES'
        
str = 'vfjdalxdrxggdbdpehuisictklykjrmgwxjykjbbgihllnbpwvaodchpnhbyynfxkqvubzyijftuswkotmewoondvpcwcjtpbqldpjnyrivlfhaatgxhukmsbooezjvdzigpsvpldmwktylmfkvbwityyheaqzdsjlhbgymlllwejjtovoqrylrxtvxlwadilmltnyealceunzjiqbcomtlhrivpkyxxnlqajxawzgqnibxyczmrvyyoitftufsjqjjbglxhtnwbruztvmmsmliugopcvilntwqbhnidchetdepysbteobyxrqzoynbtjrutgewllceoivpaxienlfkdvmrvztokmkftodecgksoghrfrvudcfiztzwsukejwkclpipvshmardhkacnfjxecxbwtncckogxeoobjxplostzvxocimgkljigzkjlbrkfiygrvwcmqxlnubpcnyoajyhijstmldrtdzkzxplqmydjzvlpvcreaanlsixeoqzrqksnzffndlwfgkwdmnhooucifzotqokiydxzidmoolvwvrzjegxudzdibrdthnbhsygdbvtrgondfmmlvliynlioeljoakvvkcyozrfhhtkmhyzelhcyumobzxpcjkxwoxkpopwxkijugkysudsopjrrigtutsqjpazfrvccenwmxwgrzbirkziuidodvemkelpwjrapewddukxulflxgtroygttkgdrtupelptrnxuhjrbwymvfhmvfupahxdysxpxkesbrryyarcyqqtxyisfejglgllblayxeszxkzymqaliqgfqoywtjegsruteutcbldyvcwiuyvdpbifsidnsjvkdpfhkyjnjolfqkplkkqznyhfjmubyqnbfskrqwebksgbexooheqxexenlzqjrfmwxxqpturdmzgqxwhgcxfhwkwhlptcufaucqjxlcdzelsdizlkwrtsbsbmhuqdaqzehlesnhtrslwckiniziccagqjagpcwohfznx'
# print(conv('aaabbbb'))

# ===========================================|
# +++++++++++++++++++++++++++++++++++++++++++|
# Hacker Rank: Sherlock and the Valid String |
# +++++++++++++++++++++++++++++++++++++++++++|
# ===========================================|


def isValid(s):
    dic = Counter(s)
    freq = Counter(dic)

    if len(freq) == 1:
        return 'YES'
    elif len(freq) == 2:
        max_key = max(freq.keys())
        min_key = min(freq.keys())

        if freq[max_key] == 1 and max_key-min_key == 1:
            return 'YES'
        elif freq[min_key] == 1 and min_key == 1:
            return 'YES'

    return 'NO'


def l_r_s(s):
    
    c = Counter(s)
    
    dic = {}
    a = list(set(c.values()))
    if len(a) == 1 and a[0] ==1:
        # return len(s)
        print(len(s))
    else:
        # print(c)
        for k,v in c.items():
            if v != 1:
               dic[k] = v
        if len(dic)==1:
            a = list(dic.values())
            print(a[0]) 
        
        else:
            ls = sorted(list(dic.values()))
            # print(set(ls))
            if len(set(ls)) == 1:
                print(ls)
                print(len(ls))
            else:
                print(ls[0])


# print(l_r_s('abc'))
l_r_s('abbbcdd')



