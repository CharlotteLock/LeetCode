def int2rom(n):
    if n < 1 or n > 3999:
        print('input error.')
        return 0
    rom_lst = [' ',
               'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 
               'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC',
               'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM',
               'M', 'MM', 'MMM']
    rom = ''
    bit = n % 10
    ten = (n % 100) // 10
    hun = (n % 1000) // 100
    tho = n // 1000
    if tho != 0:
        rom += rom_lst[27 + tho]
    if hun != 0:
        rom += rom_lst[18 + hun]
    if ten > 0:
        rom += rom_lst[9 + ten]
    if bit > 0:
        rom += rom_lst[bit]
    return rom

int2rom(3999)
