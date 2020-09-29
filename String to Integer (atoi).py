# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

# - Only the space character ' ' is considered as whitespace character.
# - Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

class Solution:
    def myAtoi(self, str: str) -> int:
        str=str.strip()
        if not str:
            return 0

        val=0
        neg=False

        if str[0] =="-":
            neg=True


        elif str[0]=="+":
            neg=False

        elif not str[0].isnumeric():
            return 0

        else:
            val=ord(str[0])-ord("0")
        for i in range(1,len(str)):
            if str[i].isnumeric():
                val=val*10+(ord(str[i])-ord("0"))
                if neg and val>=2147483648:
                    return -2147483648
                if not neg and val>=2147483647:
                    return 2147483647
            else:
                break
        if not neg:
            return val
        else:
            return -val



#Method: Use ord() to get ascii value of characters and strip function to eliminate whitespaces in the start and the end
