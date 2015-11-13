def best_palindrome(s):
    best_partitions = {}
    def palindrome_partitioning(s):
        if s in best_partitions:
            return best_partitions[s]

        if len(s) == len(set(s)):
            best_partitions[s] = len(s) - 1
            return len(s) - 1

        if len(s) == 1 or s == s[::-1]:
            return 0

        res = float('inf')
        for i in xrange(1, len(s)):
            res = min(res, palindrome_partitioning(s[:i]) + palindrome_partitioning(s[i:]) + 1)

        best_partitions[s] = res
        return res

    return palindrome_partitioning(s)

def minCut(s):
    n=len(s)
    ptable=[[False for i in range(n)]for j in range(n)]
    dp=[n-i for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if s[i]==s[j] and (j-i<2 or s[i+1]==s[j-1]):
                ptable[i][j]=True
                dp[i]=min(dp[i],1+dp[j+1])
    return dp[0]-1


from datetime import datetime
startTime = datetime.now()
s = 'XfCtL38GNmYvAhmYEIecokbWJjAXsdGZ3Ro1dT1BEx6fFGPqmMMaRAaYcPFvcobsNtWZxW1U11kEHfRbMpv2q3VGPVOP8dK'
print best_palindrome(s)
print datetime.now() - startTime