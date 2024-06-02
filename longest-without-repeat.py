def lengthOfLongestSubstring(s):
    # store the character and the index in s once seen
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        # check if character is in seen dict
        if s[r] not in seen:
            # output set to current index or the previous output whatever is greater
            output = max(output, r-l+1)
        else:
            if seen[s[r]] < l:
                # if above happens there are characters separating the two repeating characters and output is adjusted
                output = max(output, r-l+1)
            else:
                # if this code is run the repeating characters are side by side and output is adjusted accordingly
                l = seen[s[r]] + 1
        # adds the character to dict
        seen[s[r]] = r
    return output
