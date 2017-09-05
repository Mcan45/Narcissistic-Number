def narcissistic( value ):
    power = len(str(value))
    sum = 0
    for i in str(value):
        sum += int(i) ** power
    if value == sum:
        return True
    else:
        return False
