# def division_binary(binary1, binary2):
#     result = ''
#     temp = '0'
#     remainder = '0'

#     for i in range(len(binary1)):
#         if int(binary2) > int(temp):
#             result += '0'
#             temp += binary1[i]

#         else: 
#             remainder = subtract_binary(temp, binary2)
#             if remainder == '0':
#                 temp = binary1[i]
#                 result += '1'
            
#             else:
#                 remainder = str(remainder).lstrip('0')
#                 result += '1'
#                 temp = remainder + binary1[i]
    
#     if int(temp) != 0:
#         result += '1'
#     else:
#         result += '0'

#     return result

def division_binary(binary1, binary2):
    result = ''
    temp = '0'
    remainder = '0'
    decimal_point_pos = binary1.find('.') - binary2.find('.')

    # Remove decimal points from binary strings
    binary1 = binary1.replace('.', '')
    binary2 = binary2.replace('.', '')

    for i in range(len(binary1)):
        if int(binary2, 2) > int(temp, 2):  # Convert to base-2 integer
            result += '0'
            temp += binary1[i]

        else: 
            remainder = subtract_binary(temp, binary2)
            if remainder == '0':
                temp = binary1[i]
                result += '1'
            
            else:
                remainder = str(remainder).lstrip('0')
                result += '1'
                temp = remainder + binary1[i]
    
    if int(temp, 2) != 0:  # Convert to base-2 integer
        result += '1'
    else:
        result += '0'

    # Adjust decimal point position
    if decimal_point_pos > 0:
        result = result[:-decimal_point_pos] + '.' + result[-decimal_point_pos:]

    return result


def multiply_binary():
    print("multiply")


def subtract_binary(binary1, binary2):
    # Split binary numbers into integer and fractional parts
    if '.' in binary1:
        int1, frac1 = binary1.split('.')
    else:
        int1 = binary1
        frac1 = ''
    if '.' in binary2:
        int2, frac2 = binary2.split('.')
    else:
        int2 = binary2
        frac2 = ''

    # Determine the maximum length for integer and fractional parts
    max_int_len = max(len(int1), len(int2))
    max_frac_len = max(len(frac1), len(frac2))

    # Zero-pad integer and fractional parts to the maximum length
    int1 = int1.zfill(max_int_len)
    int2 = int2.zfill(max_int_len)
    frac1 = frac1.ljust(max_frac_len, '0')
    frac2 = frac2.ljust(max_frac_len, '0')

    # Initialize variables for result and borrowing
    result_int = ''
    result_frac = ''
    borrow = 0

    # Subtract fractional parts
    for i in range(max_frac_len - 1, -1, -1):
        diff = int(frac1[i]) - int(frac2[i]) - borrow
        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0
        result_frac = str(diff) + result_frac

    # Subtract integer parts with consideration of borrow from fractional part
    for i in range(max_int_len - 1, -1, -1):
        diff = int(int1[i]) - int(int2[i]) - borrow
        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0
        result_int = str(diff) + result_int

    # Combine integer and fractional parts
    result = result_int.lstrip('0') or '0'  # Remove leading zeroes
    if result_frac:
        result = result_int.lstrip('0') or '0'  # Remove leading zeroes
        result += '.' + result_frac.rstrip('0')  # Remove trailing zeroes
    if result_frac in ['0' * (i + 1) for i in range(8)]:
        result = result[:-1]
        


    return result



def add_binary(binary1, binary2):
    if '.' in binary1:
        int1, frac1 = binary1.split('.')
    else:
        int1 = binary1
        frac1 = ''
    if '.' in binary2:
        int2, frac2 = binary2.split('.')
    else:
        int2 = binary2
        frac2 = ''

    if '.' in binary1 or '.' in binary2:
        max_len_frac = max(len(frac1), len(frac2))
        frac1 = frac1.ljust(max_len_frac, '0')
        frac2 = frac2.ljust(max_len_frac, '0')

    max_len_int = max(len(int1), len(int2))
    int1 = int1.zfill(max_len_int)
    int2 = int2.zfill(max_len_int)

    result_int = ''
    result_frac = ''
    carry = 0

    for i in range(len(frac1) - 1, -1, -1):
        if frac1[i] == '.':
            result_frac = '.' + result_frac
        else:
            bit_sum = int(frac1[i]) + int(frac2[i]) + carry
            result_frac = str(bit_sum % 2) + result_frac
            carry = bit_sum // 2

    int_sum = carry
    for i in range(len(int1) - 1, -1, -1):
        bit_sum = int(int1[i]) + int(int2[i]) + int_sum
        result_int = str(bit_sum % 2) + result_int
        int_sum = bit_sum // 2

    result_int = str(int_sum % 2) + result_int

    result = result_int.lstrip('0') or '0'  # Remove leading zeroes
    if result_frac:
        result = result_int.lstrip('0') or '0'  # Remove leading zeroes
        result += '.' + result_frac.rstrip('0')  # Remove trailing zeroes
    if result_frac in ['0' * (i + 1) for i in range(8)]:
        result = result[:-1]
    return result



def complement(bin_str:str):
    def invert(input):
        inversed = False
        input = input[::-1]
        for i, char in enumerate(input): 
            if inversed:
                input = input[:i] + ('.' if char == '.' else '0' if char == '1' else '1') + input[i + 1:]
            if char == '1':
                inversed = True

        fin_result = input[::-1]
        return fin_result
    

    bin_str = list(bin_str)

    if bin_str[0] == '1':
        bin_str.insert(0, '111')
    elif bin_str[0] == '0':
        bin_str.insert(0, '000')

    bin_str = "".join(bin_str)
    return invert(bin_str)
    

# TESTING
# print(f"1.) {complement("1011.011")}")
# print(f"2.) {complement("01011011.01")}")
# print(f"3.) {complement("1001.110")}")
# print(f"4.) {complement("00100111.10")}")
# print(f"5.) {complement("01010011.01")}")
# print(f"6.) {complement("10010100.11")}")
# print(f"7.) {complement("00110101.010")}")

# if __name__ == "__main__":
#     print(f"1.) {subtract_binary('1011', '0111')}")
#     print(f"2.) {subtract_binary('1011.011', '0111.11')}")
#     print(f"3.) {subtract_binary('1011.01', '1100.01')}")
#     print(f"4.) {subtract_binary('1111', '1001')}")