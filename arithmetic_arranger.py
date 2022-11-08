

def arithmetic_arranger(problems, calculate=False):
    import re
    #too many problems supplied to the function
    
    if len(problems)>5:
        return('Error: Too many problems.')
    
    # defining rows for the formatter
    first=''
    second=''
    lines=''
    result=''

    for problem in problems:
        operator=problem.split()[1]#defining operator
        num1=problem.split()[0]#first number
        num2=problem.split()[2]#second number
        length=len(max(problem.split(),key=len))#maximum lenght of numbers
        if re.search('[^\s0-9-+]',problem):# If there is a character different than space,0-9,+,-
        # This idea of using reg ex is inspired from a youtube video Landon Schlangen created.
        # Link to the video: https://www.youtube.com/watch?v=6X6pj92PQiw
            if re.search("[^+-]",operator):# If operator string is different than +,-
                return("Error: Operator must be '+' or '-'.")
                break
            else:
                return('Error: Numbers must only contain digits.')
                break
        
        if len(num1)>4 or len(num2)>4:#Numbers more than 4 digits
            return ('Error: Numbers cannot be more than four digits.')
            break
        
        # Manual Formatting
        first=first+' '*((2+length)-len(num1))+num1+4*' '# Defining first numbers set
        second=second+operator+' '*((1+length)-len(num2))+num2+4*' '# Defining second numbers set
        lines=lines+'-'*(2+length)+4*' '# Dash lines 
        
        if calculate:
            op={'+':lambda x,y:x+y,'-': lambda x,y:x-y}
            # Using rjust method in the next step different from previous ones
            # op[operator] will initiate the lambda we defined in the dictionary
            result=result+str(op[operator](int(num1),int(num2))).rjust(2+length)+' '*4
    
    first=first.rstrip()
    second=second.rstrip()
    lines=lines.rstrip()
    
    
    if calculate:
        return(first+'\n'+second+'\n'+lines+'\n'+result.rstrip())
    else:
        return((first+'\n'+second+'\n'+lines))