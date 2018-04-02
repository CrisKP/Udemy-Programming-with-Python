# Main Function

def calculate(x, y):
    return x + y

def main():
    print(calculate(10, 20))

main()      #main will be executed if other programs import this modules

if __name__ == '__main__':      #main will be executed if this modules is the main module
    main()
