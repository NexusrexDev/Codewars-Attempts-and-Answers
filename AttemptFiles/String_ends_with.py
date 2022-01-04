def solution(string, ending):
    if len(ending) > 0:
        if string[-len(ending):] == ending:
            return True
        else:
            return False
    else:
        return True

#Test:
print(solution('abc', 'bc'))