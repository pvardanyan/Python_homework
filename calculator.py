# Easy and pretty way
# print(eval(input("Enter expression: ")))


# Long way (in expression first does [ * and / ] operations and only then [+ and - ] )

def mult_div(expr):
    i = 0
    while i < len(expr):
        if expr[i] == '*':
            expr[i-1] = float(expr[i-1]) * float(expr[i+1])
            expr.pop(i+1)
            expr.pop(i)
            i -= 1
        elif expr[i] == '/':
            expr[i-1] = float(expr[i-1]) / float(expr[i+1])
            expr.pop(i+1)
            expr.pop(i)
            i -= 1
        i+=1    
    return expr

def sum_minus(expr):
    num = float(expr[0])
    i = 1
    while i < len(expr):
        if expr[i] == '+':
            num = num + float(expr[i+1])
            i += 2
        elif expr[i] == '-':
            num = num - float(expr[i+1])
            i += 2     
    return num

def calculator():
    print("Enter your expression with spaces:")
    expr = input().split(" ")
    try:
        result = sum_minus(mult_div(expr))
        return result
    except Exception as e:
        return f"Error: {e}"

print(calculator()) 


