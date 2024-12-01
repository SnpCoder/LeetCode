def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    gp, sp = 0, 0
    satisfy = 0
    while gp < len(g) and sp < len(s):
        if g[gp] <= s[sp]:
            satisfy += 1
            gp += 1
            sp += 1
        else:
            sp += 1
    return satisfy


g = [10, 9, 8, 7]
s = [5, 6, 7, 8]
print(findContentChildren(g, s))
