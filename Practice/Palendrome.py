# palendrome number

def swap_case(s):
    return
    s = input()
    print(any(i.isalnum() for i in s) )
    print(any(i.isalpha() for i in s) )
    print(any(i.isdigit() for i in s) )
    print(any(i.islower() for i in s) )
    print(any(i.isupper() for i in s) )

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)