def reverse(x):
    if x == 0:
        return 0
    re_int = 0
    if x < 0:
        re_int_type = -1
        x = x * (-1)
    else:
        re_int_type = 1
    while x:
        re_int = re_int * 10 + (x % 10)
        x = x // 10
    re_int *= re_int_type
    if re_int > 2**31-1 or re_int < -(2**31):
        return 0
    return re_int
#reverse(-123)
