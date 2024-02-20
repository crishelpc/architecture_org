import binary_operation


def division_binary(binary1,binary2): 
    if binary1.startswith('0') and binary2.startswith('0'):
        return binary_operation.division_binary(binary1,binary2)
    
    elif binary1.startswith('1') and binary2.startswith('0'):
        binary1 = binary_operation.complement(binary1)
        result = binary_operation.division_binary(binary1,binary2)
        result = binary_operation.complement(result)
        return result 
    
    elif binary1.startswith('0') and binary2.startswith('1'):
        binary2 = binary_operation.complement(binary2)
        result = binary_operation.division_binary(binary1,binary2)
        result = binary_operation.complement(result)
        return result
    
    elif binary1.startswith('1') and binary2.startswith('1'):
        binary1 = binary_operation.complement(binary1)
        binary2 = binary_operation.complement(binary2)
        print(binary1)
        print(binary2)
        result = binary_operation.division_binary(binary1,binary2)

        return result


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