def removeZero(number):
    result = number.translate({ord(i): None for i in '0'})
    return result

def main():
    n1 = input("Enter a number ")
    n2 = removeZero(n1)
    print(n2)
    
main()