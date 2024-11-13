# lcs
def longestCommonSubsequence(text1:str,text2:str)->int:
    rows,cols=len(text1),len(text2)
    dp=[[0 for _ in range(cols+1)] for _ in range(rows+1)]
    for i in range(0,rows):
        for j in range(0,cols):
            if text1[i]==text2[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    return dp[rows][cols]
    

text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1,text2))