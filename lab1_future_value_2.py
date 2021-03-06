def calculate_future_value(monthly_investment, yearly_interest_rate, years):
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    future_value = 0

    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    return future_value

def main():
    print('Welcome to the Future Value Calculator')

    choice = 'y'
    while choice == 'y':
        monthly_investment = float(input('Enter your monthly investment:\t'))
        yearly_interest_rate = float(input('Enter yearly interest rate:\t'))
        years = int(input('Enter number of years:\t\t'))
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)

        print('Future value:\t\t\t'+ str(round(future_value, 2)))
        choice = input('Continue? (y/n)\t\t')

    print('Thanks for using the Future Value Calculator')

if __name__ == '__main__':
    main()
