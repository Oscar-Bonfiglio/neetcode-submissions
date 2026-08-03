class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if lengths don't match then word cannot be Anagram
        if len(s) != len(t):
            return False
        #Creating Hash Table for both strings S & T 
        hashS, hashT = {}, {}

        #Checking the length of each word
        # +1 for each word and will be stored into Hash Table
        # If word doesn't exist then it stays 0 
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i],0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        return hashS == hashT 