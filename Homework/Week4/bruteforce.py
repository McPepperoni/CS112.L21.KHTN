def isPal(s):
    return s == s[::-1]
try:
    s = input()
    result = ''

    for i in range(len(s)):
        key  = False
        temp = ''
        for j in range(len(s) - 1, i - 1, -1):
            if(s[i] == s[j]):
                temp = s[i: j + 1]
                if isPal(temp) and len(temp) > len(result):
                    key = True
                    result = temp
                    break
except EOFError as error:
    # Output expected EOFErrors.
    Logging.log_exception(error)

print(str(len(result)) + ' ' + result)
