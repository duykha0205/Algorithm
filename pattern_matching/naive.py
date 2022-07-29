def pt_matching(str, pat):
    m = len(pat)
    n = len(str)
    for i in range(n-m):
        for j in range(m):
            if str[i+j] != pat[j]:
                break
            
        if (j == m):
            print("Pattern found at index ", i)
            

txt = "AABAACAADAABAAABAA"
pat = "AABA"
pt_matching(txt, pat)