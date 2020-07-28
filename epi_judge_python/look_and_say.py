from test_framework import generic_test


def look_and_say(n: int) -> str:
    def say_sequence(s):
        say = []
        count, current_digit = 0, s[0]
        for digit in s:
            if digit == current_digit:
                count += 1
            else:
                say.append(str(count) + current_digit)
                count, current_digit = 1, digit
        say.append(str(count) + current_digit)
        return ''.join(say)

    s = '1'
    for i in range(n-1):
        s = say_sequence(s)
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
