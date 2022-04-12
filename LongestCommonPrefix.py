strs = ["flower","flow","flight"]

# Longest Common Prefix 
def longestCommonPrefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        for j in range(1,len(strs)):
            if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]

print(longestCommonPrefix(strs))