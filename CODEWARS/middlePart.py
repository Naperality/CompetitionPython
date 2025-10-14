def get_middle(s):
    # return s[int(len(s)/2)] if len(s) % 2 != 0 else s[int(len(s)/2)-1]+s[int(len(s)/2)]
    return s[(len(s)-1)//2:(len(s)+2)//2]

print(get_middle('test'))