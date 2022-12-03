# removes duplicates from a string
def removeDuplicates(s):
    unique = ""
    duplicate = ""
    for c in s:
        if c not in unique and c not in duplicate:
            # not in either, make unique
            unique += c
        elif c in unique and c not in duplicate:
            # only in unique, make duplicate
            duplicate += c
            unique = unique.replace(c, "")
        else:
            # already in duplicate, do nothing
            pass
    return unique + duplicate

def findCommonChars(s1, s2):
    return [x for x in s1 if x in s2]