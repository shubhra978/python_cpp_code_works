def swap_case(s):
    new_result = ""
    for items in s:
        if(items == items.lower()):
            new_result+= items.upper()
        elif(items == items.upper()):
            new_result +=items.lower()
            
    return new_result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
