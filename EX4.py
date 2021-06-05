#
import math
import sympy as sp
from sympy.utilities.lambdify import lambdify
def input_equation():
    x = sp.symbols('x')
    user_input = input("Enter equation: ")
    sp_user_input = int(input("Enter start point: "))
    ep_user_input = int(input("Enter end point: "))
    epsilon = 0.0001
    f = sp.sympify(user_input)  # manifulpating equation to a symbol
    fp = D_Calc(f)

    print("Choose the Method that you want\n"
          "1- Bisection Method\n"
          "2- Newton Raphson Method\n"
          "3- Secant Method")
    user_ch = int(input())
    if user_ch == 1:
        Bisection_Method(f,sp_user_input,ep_user_input,epsilon)
    elif user_ch == 2:
        Newton_Raphson_Method(f, fp, sp_user_input, ep_user_input, epsilon)
    elif user_ch == 3:
        Secant_Method(f, sp_user_input, ep_user_input, epsilon)

def D_Calc(f):  #Calculate the derivative of f
    x = sp.symbols('x')
    fprime = f.diff(x)
    return fprime

def Find_Point_In_Segment(f,sp_user_input,ep_user_input):
    x = sp.symbols('x')





def error_Calc(sp_user_input,ep_user_input,epsilon):  #Calculate an error
    return -(math.log(epsilon / (ep_user_input - sp_user_input)) / math.log(2))



def Bisection_Method (f,sp_user_input,ep_user_input,epsilon):
    maxS = error_Calc(sp_user_input,ep_user_input,epsilon)
    steps = 0
    while (ep_user_input - sp_user_input) > epsilon:
        if steps > maxS:
            print(" Steps limit.")
            return None
        mp = (sp_user_input + ep_user_input) / 2
        if f(sp_user_input) * f(mp) > 0:
            sp_user_input = mp
        else:
            ep_user_input = mp
        steps += 1
    return mp, steps

def  Newton_Raphson_Method(f,fp, sp_user_input, ep_user_input, epsilon):


def Secant_Method(f, sp_user_input, ep_user_input, epsilon):



def main():
    input_equation()


main()