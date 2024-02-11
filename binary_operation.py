def division_binary():
    print("division")
        
def multiply_binary():
    print("multiply")

def subtract_binary(binary1, binary2):
    max_len = max(len(binary1), len(binary2))

    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)

    result = ''
    temp = 0

    for i in range(max_len - 1, - 1, -1): 
        num = int(binary1[i]) - int(binary2[i]) - temp
        if num % 2 == 1: 
            result = '1' + result 
        else: 
            result = '0' + result
        
        if num < 0: 
            temp = 1
        else: 
            temp = 0
    
    if temp != 0: 
        result = '01' + result 

    if int(result) == 0: 
        result = 0
    
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

   if '.'in binary1 or '.' in binary2:
        max_len_frac = max(len(frac1), len(frac2))
        frac1 += '0' * (max_len_frac - len(frac1))
        frac2 += '0' * (max_len_frac - len(frac2))

   result_int = ''
   result_frac = ''
   carry = 0

   if frac1 or frac2:
        for i in range(max_len_frac - 1, -1, -1):
                if frac1[i] == '.':
                    result_frac = '.' + result_frac
                else:
                    bit_sum = int(frac1[i]) + int(frac2[i]) + carry
                    result_frac = str(bit_sum % 2) + result_frac
                    carry = bit_sum // 2
#    else:
#         result_frac = '00'
   if result_frac:
        result_frac = '.' + result_frac 

   while carry:
        bit_sum = carry
        result_frac = str(bit_sum % 2) + result_frac
        carry = bit_sum // 2

   int_sum = carry
   for i in range(len(int1) - 1, -1, -1):
        bit_sum = int(int1[i]) + int(int2[i]) + int_sum
        result_int = str(bit_sum % 2) + result_int
        int_sum = bit_sum // 2
   result_int = str(int_sum % 2) + result_int


   result = result_int + result_frac
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

