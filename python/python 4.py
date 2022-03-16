from turtle import position


def will_hit(equation, player_coordinaters):
    character = equation[4]
    if character == "-":
        m= character + equation[5]
    else:
        m = character
        charactor = equation[7]
    
    if character == "-":
        b= character + equation[-1]
    else:
        b= equation[-1]
    
    x,y = position
    if (m*x + b == y):
         return True

    else:
        return False