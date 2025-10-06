
def recursive_poly(word):
    if len(word) <= 1:
        return "YES"
    if word[0] != word[-1]:
        return "NO"
    return recursive_poly(word[1:-1])

print(recursive_poly("racecar"))