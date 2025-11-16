def isAnagram(s,t):
        if len(s)!=len(t):
            return False
        freq = {}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in t:
            if i not in freq:
                return False
            freq[i]-=1
            if freq[i]<0:
                return False
        return True
s='anagram'
t='nagaram'
print(isAnagram(s,t))