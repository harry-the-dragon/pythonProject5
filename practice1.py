''''
#6 kyu Detect Pangram
import string

def is_pangram(s):
    s = s.lower()
    for token in string.ascii_lowercase:
        if token not in s:
            return False
    return True

    # w = 0
    # i = alphabet_list(w)
    # for e in list_s:
    #     if e != i:
    #         return False
    #     w +=1
    # return True
    #
    #
    # for i in alphabet_list:
    #     w = 0
    #     if i == list_s[w]:
    #         w += 1
    #
    #     else:
    #         return False
    #     return True


print (is_pangram("abcdefghijklm opqrstuvwxyz"))
'''
'''
#7kyu Complementary DNA

#Passed result
def DNA_strand(dna):
    output = ""
    for i in dna:
        if i == "A":
            output += "T"
        elif i == "T":
            output += "A"
        elif i == "C":
            output += "G"
        else:
            output += "C"

    return output

#Optimal
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])


dna  = "ATTG"
print (list(dna))
print(DNA_strand(dna))
'''
'''
# 8kyu Rck Paper Scissors
#my solution
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock" and p2 == "scissors" or  p1 == "paper" and p2 == "rock" or p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    else:
        return "Player 2 won!"

# optimal solution
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


'''
'''

#6 kyu Find the unique number

#my solution 1:
def find_uniq(arr):
    arr.sort()
    n = len(arr)

    if arr[0] != arr [1]:
        return arr[0]

    if arr[n-2]!= arr[n-1]:
        return arr[n-1]

arr = [ 1, 1, 1, 2, 1, 1 ]
print (find_uniq(arr))
'''
'''
# 8 kyu Reversed Strings
def solution(string):
    return string[::-1]
'''

#6 kyu Persistent Bugger.

def persistence(n):




n = 39
print (persistence(n))



