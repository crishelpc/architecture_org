import binary_operation


def division_binary(binary1,binary2): 
    if binary1.startswith('1') and binary2.startswith('1'):
        return binary_operation.subtract_binary(binary1,binary2)






def add_binary(binary1, binary2):
    if binary1.startswith('0') and binary2.startswith('0'):
        return binary_operation.add_binary(binary1, binary2)
    
    elif binary1.startswith('1') and binary2.startswith('0'):
        binary1= binary_operation.complement(binary1)
        return binary_operation.subtract_binary(binary2, binary1)
    
    elif binary1.startswith('0') and binary2.startswith('1'):
        binary2= binary_operation.complement(binary2)
        return binary_operation.subtract_binary(binary1, binary2)
    
    elif binary1.startswith('1') and binary2.startswith('1'):
        return binary_operation.add_binary(binary1, binary2)

def subtract_binary(binary1, binary2):
    if binary1.startswith('0') and binary2.startswith('0'):
        return binary_operation.subtract_binary(binary1, binary2)
    
    elif binary1.startswith('1') and binary2.startswith('0'):
        return binary_operation.add_binary(binary1, binary2)
    
    elif binary1.startswith('0') and binary2.startswith('1'):
        binary2 = binary_operation.complement(binary2)
        return binary_operation.add_binary(binary1, binary2)
    
    elif binary1.startswith('1') and binary2.startswith('1'):
        return binary_operation.subtract_binary(binary2, binary1)