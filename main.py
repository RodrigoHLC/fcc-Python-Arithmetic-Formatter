import re

def arithmetic_arranger(problems, show_answers=False):
    # pass
    # Check amount of problems/string
    if len(problems) > 5:
       return "Error: Too many problems."
    splitStr = ""
    upperStr = ""
    lowerStr = ""
    hypenStr = ""
    resultStr = ""
    # Check that ALL strings are correctly formatted
    generalRegex = re.compile('^\d{1,4}\s[+\-]\s\d{1,4}$')
    for string in problems:
        # If any string doesn't match
        if generalRegex.search(string) is None:
            # pinpoint if it's a sign issue
            if re.search('\s[+\-]\s', string) is None:
                return "Error: Operator must be '+' or '-'."
            # pinpoint if it's a valid char issue:
            elif re.search('^\d+\s[+\-]\s\d+$', string) is None:
                return "Error: Numbers must only contain digits."
            # pinpoint if it's a length issue:
            elif re.search(generalRegex, string) is None:
                return "Error: Numbers cannot be more than four digits."
        # --- DONE CHECKING FOR ERRORS ---
