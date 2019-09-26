from colorama import init 
from termcolor import colored 
  

#import Library for UI Test
from uisoup import uisoup

#Import SubProcess to open Calc App
from subprocess import Popen

# Import sleep that might be useful to wait in some cases
from time import sleep


def open_calculator(): 
  Popen(["calc.exe"])


def check_numbers(calculator):
    b1 = calculator.find(c_name='btn0')
    b1.click()
    b1 = calculator.find(c_name='btn1')
    b1.click()
    b1 = calculator.find(c_name='btn2')
    b1.click()
    b1 = calculator.find(c_name='btn3')
    b1.click()
    b1 = calculator.find(c_name='btn4')
    b1.click()
    b1 = calculator.find(c_name='btn5')
    b1.click()
    b1 = calculator.find(c_name='btn6')
    b1.click()
    b1 = calculator.find(c_name='btn7')
    b1.click()
    b1 = calculator.find(c_name='btn8')
    b1.click()
    b1 = calculator.find(c_name='btn9')
    b1.click()
    be = calculator.find(c_name='btnEquals')
    be.click()

def add_integers(calculator):
    b1 = calculator.find(c_name='btn2')
    b1.click()
    ba = calculator.find(c_name='btnAdd')
    ba.click()
    b2 = calculator.find(c_name='btn3')
    b2.click()
    be = calculator.find(c_name='btnEquals')
    be.click()

def subtract_integers(calculator):
    b1 = calculator.find(c_name='btn4')
    b1.click()
    ba = calculator.find(c_name='btnSubtract')
    ba.click()
    b2 = calculator.find(c_name='btn5')
    b2.click()
    be = calculator.find(c_name='btnEquals')
    be.click()

def multiplication_integers(calculator):
    b1 = calculator.find(c_name='btn6')
    b1.click()
    ba = calculator.find(c_name='btnMultiply')
    ba.click()
    b2 = calculator.find(c_name='btn7')
    b2.click()
    be = calculator.find(c_name='btnEquals')
    be.click()

def division_integers(calculator):
    b1 = calculator.find(c_name='btn8')
    b1.click()
    ba = calculator.find(c_name='btnDivide')
    ba.click()
    b2 = calculator.find(c_name='btn9')
    b2.click()
    be = calculator.find(c_name='btnEquals')
    be.click()

def division_by_zero(calculator):
    b1 = calculator.find(c_name='btn5')
    b1.click()
    ba = calculator.find(c_name='btnDivide')
    ba.click()
    b2 = calculator.find(c_name='btn0')
    b2.click()
    be = calculator.find(c_name='btnEquals')
    be.click()

def division_by_any_number(calculator):
    b1 = calculator.find(c_name='btn7')
    b1.click()
    ba = calculator.find(c_name='btnDivide')
    ba.click()
    b2 = calculator.find(c_name='btn4')
    #b2 = calculator.find(c_name='btnDecimal')
    #b2 = calculator.find(c_name='btn5')
    b2.click()
    be = calculator.find(c_name='btnEquals')
    be.click()
    
def success():
    init()
    print(colored('---Success---', 'white', 'on_green'))

def division_zero_by_any_number(calculator):
    b1 = calculator.find(c_name='btn0')
    b1.click()
    ba = calculator.find(c_name='btnDivide')
    ba.click()
    b2 = calculator.find(c_name='btn4')
    #b2 = calculator.find(c_name='btnPoint')
    #b2 = calculator.find(c_name='btn5')
    b2.click()
    be = calculator.find(c_name='btnEquals')
    be.click()

def main():    
    print('Starting the test')
    print('Opening Calculator app')
    open_calculator()
    sleep(5) # Time in seconds
    print('Get and drag calulator window in right coordinates')
    calculator = uisoup.get_window('Calculator')
    calculator.drag_to(50, 50, x_offset=30, y_offset=5)
    success()
    print('Checking if numbers from 0-9 work')
    check_numbers(calculator)
    success()
    print('Adding Two numbers')
    add_integers(calculator)
    success()
    print('Subtracting Two numbers')
    subtract_integers(calculator)
    success()
    print('Multipling two numbers')
    multiplication_integers(calculator)
    success()
    print('Dividing Two numbers')
    division_integers(calculator)
    success()
    print('Dividing By Any number')
    division_by_any_number(calculator)
    success()
    print('Dividing Zero by Any number')
    division_zero_by_any_number(calculator)
    success()
    print('Dividing By Zero')
    division_by_zero(calculator)
    success()
    print('Done')
main()




    






















    
