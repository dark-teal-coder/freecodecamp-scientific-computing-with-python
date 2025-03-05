def arithmetic_arranger(math_problems, display=False):
    ## Exception 1: No more than 5 problems supplied
    if len(math_problems) > 5:
        raise Exception("Error: Too many problems.")

    values = {}

    for prob_num, prob in enumerate(math_problems):
        ## Python index starts at 0
        prob_num += 1
        ## Argument 1 is a list
        # print(prob)
        operand1, operator, operand2 = prob.split()

    ## Exception 2: Only + and -
    if operator not in ['+', '-']:
        raise Exception("Error: Operator must be '+' or '-'.")
    ## Exception 3: Only digits allowed
    if not operand1.isdigit() or not operand2.isdigit():
        raise Exception("Error: Numbers must only contain digits.")
    ## Exception 4: Only 4 digits
    if (len(operand1) > 4) or (len(operand2) > 4):
        raise Exception("Error: Numbers cannot be more than four digits.")

    ## Answer line and its length
    operand1_digit = len(operand1)
    operand2_digit = len(operand2)
    max_digit = max(operand1_digit, operand2_digit)
    ans_line = "-" * (max_digit + 2)
    prob_width = len(ans_line)

    ## Math calculations
    ans = eval(prob)

    ## Right alignment
    line1 = operand1.rjust(prob_width)
    line2 = operator + ' ' + operand2.rjust(max_digit)
    line3 = ans_line
    line4 = str(ans).rjust(prob_width)
    # print(line1, line2, line3, line4, sep='\n')

    ## Storing values
    dict_key = "prob" + str(prob_num)
    dict_val = [line1, line2, line3, line4]
    values[dict_key] = dict_val

    ## Check how individual value is stored in dictionary
    print(values)
    ## Combine the same line of each problem
    prob_count = len(values)
    ## Display the answer or not
    if display == False:
        prob_count = prob_count - 1
    data = []
    for i in range(0, prob_count):
        data_line = ""
    for prob_line in values.values():
        # print(prob_line)
        if prob_line[i] == prob_line[-1]:
            data_line += prob_line[i]
        continue
        data_line += prob_line[i] + ' '*4
    print(data_line)
    data.append(data_line)

    ## Combine list item representing each data line into 1 string
    arranged_problems = '\n'.join(data)

    return arranged_problems



# print(arithmetic_arranger())
