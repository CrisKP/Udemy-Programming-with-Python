# Example of global variables

tax = 0                             #tax is a global variable
def calc_tax(amount, tax_rate):
    global tax                      #access global variable (no need for return as tax can be accessed by main())
    tax = amount * tax_rate         #change global variable

def main():
    calc_tax(10, 0.25)
    print('Tax:', tax)              #global tax variable

if __name__ == '__main__':
    main()
