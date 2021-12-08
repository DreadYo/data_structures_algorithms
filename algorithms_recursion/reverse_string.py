# Implement a function that reverses a string using iteration...and then recursion!


def reverse_string_recursive(string):
    if len(string) <= 1:
        return string
    return f"{string[-1]}{reverse_string_recursive(string[1:-1])}{string[0]}"


def reverse_string_iterative(string):
    lst = list(string)
    for i in range(len(lst)//2):
        lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]
    return "".join(lst)


def reverse_string_iterative2(string):
    lst = []
    for i in range(len(string)):
        lst.append(string[len(string)-i-1])
    return "".join(lst)


if __name__ == "__main__":
    print(reverse_string_recursive('yoyo mastery'))
    # should return: 'yretsam oyoy'
    print(reverse_string_iterative('yoyo mastery'))
    # should return: 'yretsam oyoy'
    print(reverse_string_iterative2('yoyo mastery'))
    # should return: 'yretsam oyoy'
