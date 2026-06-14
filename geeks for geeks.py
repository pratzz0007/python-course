def check_status(a, b, flag):
    # Condition 1: One is non-negative, one is negative, and flag is False
    if flag == False:
        return (a >= 0 and b < 0) or (a < 0 and b >= 0)
    
    # Condition 2: Both are negative and flag is True
    else:
        return a < 0 and b < 0