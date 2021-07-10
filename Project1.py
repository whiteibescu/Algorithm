def bracketing():

    brackets = input()

    if len(brackets) % 2 == 0:
        stack = []
        for bracket in brackets:
            if bracket in ("(", "{", "["):
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                else:
                    compare = stack.pop()
                    if (compare == "(" and bracket == ")") or (compare == "{" and bracket == "}") or (compare == "[" and bracket == "]"):
                        continue
                    else:
                        return False
        if len(stack) == 0:
            return True
        else: 
            return False
    else:
        return False

t = int(input())
for _ in range(t):

    if bracketing():
        print("YES")
    else:
        print("NO")

