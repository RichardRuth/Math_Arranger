def arithmetic_arranger(problems, sumShow = False):
  
  # Define 4 string lines of results display

  operand_1_line = ""
  operand_2_line = ""
  dash_line = ""
  answer_line = ""

  val = 0

  # Check to see if more than 5 problems provided. If so, per rules, program ends with error message
  
  if len(problems) > 5:
      return "Error: Too many problems."

  # If max problems not exceeded, then continue processing each problem in list

  else:
      for problem in problems:

        # using string splice to find first operator in problem set using standard problem format stated in rules

        operand_1_end = problem.find(" ")              # space between end of operand 1 and operator
        operand_1 = (problem[0:operand_1_end])         # pulls operator 1 - up to but not including op1 end

        operator_end = operand_1_end + 2               # finds operator end from space before to space after
        operator = (problem[operand_1_end+1:operator_end])     # pull operator after space

        operand_2 = (problem[operator_end+1:-1])          # uses space after operator to find beginning 
        operand_2 = operand_2 + problem[-1]               # joins beginning with rest to end
        
        # test to make sure values are all digits per rules

        try:
            isinstance(int(operand_1), int) != True or isinstance(int(operand_2), int) != True
        except ValueError:
            val = 2

        # Test for error conditions per rules

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        elif val == 2:
            return "Error: Numbers must only contain digits."
        elif len(operand_1) > 4 or len(operand_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:

            # error tests passed - continue calculating and constructing lines

            # compute totals needed for sum line if sumShow evaluates to true
            
            if operator in ["+"]:
                sum_numbers = int(operand_1) + int(operand_2)
            elif operator in ["-"]:
                sum_numbers = int(operand_1) - int(operand_2)

            # find out bigger operand and width of problem needed for spaceing purposes
            
            bigger_operand = max(len(str(operand_1)),len(str(operand_2)))
            width_problem = bigger_operand + 2

            operand_1_line = operand_1_line + "    " + (operand_1.rjust(width_problem))
            
            operand_2_line = operand_2_line + "    " + (operator + (operand_2.rjust(width_problem-1)))

            dline = "-"*(width_problem)
            dash_line += "    " + dline
            
        # if sumShow evaluates to True, answers must be shown - construct answer line

        if sumShow == True:
            sum_numbers = str(sum_numbers)
            answer_line = answer_line + "    " + (sum_numbers.rjust(width_problem))

        # construct final lines that strip first 4 spaces before printing

        operand_1_done = operand_1_line[4:].rstrip()
        operand_2_done = operand_2_line[4:].rstrip()
        dash_line_done = dash_line[4:].rstrip()
        answer_done = answer_line[4:].rstrip()

        # construct final print solution depending upon whether answers to be shown or not

        if sumShow == True:
          arranged_problems = operand_1_done + "\n" + operand_2_done + "\n" + dash_line_done + "\n" + answer_done
        else:
          arranged_problems = operand_1_done + "\n" + operand_2_done + "\n" + dash_line_done
  return arranged_problems
