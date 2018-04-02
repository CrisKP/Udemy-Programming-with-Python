# Example of local variables

def calc_tax(amount, tax_rate):
    tax = amount * tax_rate         #tax is a local variable
    return tax                      #return statement is necessary

def main():
    tax = calc_tax(10, 0.25)        #tax is a local variable
    print('Tax:', tax)

if __name__ == '__main__':
    main()
