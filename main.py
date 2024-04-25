import re

def arithmetic_arranger(problems, show_answers=False):
    # pass
    # Check amount of problems/string
    if len(problems) > 5:
       return "Error: Too many problems."
    # Check that ALL strings are correctly formatted
    generalRegex = re.compile('^\d{1,4}\s[+\-]\s\d{1,4}$')
    for string in problems:
        # If any string doesn't match...
        if generalRegex.search(string) is None:
            # ...pinpoint if it's a sign issue
            if re.search('\s[+\-]\s', string) is None:
                return "Error: Operator must be '+' or '-'."
            # ...pinpoint if it's a valid char issue:
            elif re.search('^\d+\s[+\-]\s\d+$', string) is None:
                return "Error: Numbers must only contain digits."
            # ...pinpoint if it's a length issue:
            elif re.search(generalRegex, string) is None:
                return "Error: Numbers cannot be more than four digits."
    # --- DONE CHECKING FOR ERRORS ---
    # DEFINE STRINGS
    upperStr = ""
    lowerStr = ""
    hyphenStr = ""
    resultStr = ""
    splitStr = ""
    for string in problems:
        # Store operator
        operator = string[string.index(" ")+1]
        # Split into operands
        oper1 = string.split(" "+operator+" ")[0]
        oper2 = string.split(" "+operator+" ")[1]
        # Get width of calculation
        if len(oper1) > len(oper2):
            maxLen = len(oper1)+2
        else:
            maxLen = len(oper2)+2
        # Add to strings
        # upperStr += f'{"a"*4}{oper1}{" "*(maxLen-len(oper1))}'
        upperStr += f'{" "*(maxLen-len(oper1))}{oper1}{" "*4}'
        lowerStr += f'{operator}{" "*(maxLen-len(oper2)-1)}{oper2}{" "*4}'
        hyphenStr += f'{"-"*maxLen}{" " *4 }'
        
        
        if operator == "+":
            result = str(int(oper1) + int(oper2))
        else:
            result = str(int(oper1) - int(oper2))

        resultStr += f'{" "*(maxLen-len(result))}{result}{" "*4}'
    # RETURN STRINGS - USE .rstrip TO REMOVE RIGHTMOST WHITESPACE
    if show_answers == False:
        final = f'{upperStr.rstrip()}\n{lowerStr.rstrip()}\n{hyphenStr.rstrip()}'
        return final
    else:
        final = f'{upperStr.rstrip()}\n{lowerStr.rstrip()}\n{hyphenStr.rstrip()}\n{resultStr.rstrip()}'
        return final

print(int("2"))
print(type(2))
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
