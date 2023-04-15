

def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    max_len = 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])
    return max_len

def commonChild2(s1, s2):
    # Write your code here
    
    for i in s1:
        if i not in s2:
            s1 = s1.replace(i, '')
            
    for i in s2:
        if i not in s1:
            s2 = s2.replace(i, '')
            
    print(s1)
    print(s2)
    
    return longest_common_substring(s1, s2)

def commonChild(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    return dp[m][n]


s1 = "SHINCHAN"
s2 = "NOHARAAA"
print(commonChild(s1, s2))