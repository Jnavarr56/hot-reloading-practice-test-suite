"""
Write a program using generator to print the numbers which can be divisible by 
5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program: 100
Then, the output of the program should be: 0,35,70
"""


def div_by_5_7(n):
    output = ""

    i = 0
    while i < n:
        if i % 5 == 0 and i % 7 == 0:
            nextNum = ("" if output == "" else ",") + str(i)
            output += nextNum

        i += 1

    return output


# === Testing below
def test_div_by_5_7():
    assert div_by_5_7(100) == "0,35,70"
