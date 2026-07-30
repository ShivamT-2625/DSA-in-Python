def minAddToMakeValid(s: str) -> int:
    if not s:
        return 0

    dict1 = {}

    for ch in s:
        if ch == "(":
            if ch not in dict1:
                dict1[ch] = 0
            dict1[ch] += 1

        elif ch == ")":
            if ch not in dict1:
                dict1[ch] = 0
            dict1[ch] += 1

    print(dict1)

minAddToMakeValid("S((shva))")