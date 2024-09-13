# You are given a string allowed consisting of distinct characters and an array of strings words. 
# A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# It can be solved using Brute Force or using hashSet.
# But I have solved using the Bit-Mask concept, for basic understanding

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
bit_mask = 0
for i in allowed:
    bit = 1 << (ord(i)-ord('a'))
    bit_mask = bit | bit_mask

ans = len(words)
for word in words:
    for i in word:
        bit = 1 << (ord(i) - ord('a'))
        if bit & bit_mask == 0:
            ans -= 1
            break

print(ans)