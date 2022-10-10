class rental_income():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cash_on_cash = 0
        self.cashflow = 0
        self.roi = 0

    def rent_income(self):
        self.rent = int(input('What are you charging fo rent at this property '))
        self.storage = int(input('How much are you charging for storage per month? '))
        self.laundry = int(input('How much are you charging for laundry? '))
        self.parking = int(input('Are you charging for Parking? '))
        
        self.income = self.rent + self.storage + self.laundry + self.parking 

        print(f'\nTotal monthly income = {self.income}\n ')

    def spend(self):
        self.tax = int(input('How much do you pay per month in Taxes? '))
        self.insurance = int(input('How much do you pay per month for Insurance? '))
        self.utilities = int(input('How much do you pay per month for utilities? '))
        self.hoa = int(input('What is the monthly HOA fees?'))
        self.landscape = int(input('How much do you pay montly for landscaping? '))
        self.vacancy = int(input('What is the monthly vacancy expense? '))
        self.repairs = int(input('What is the monthly expense for repairs?'))
        self.propmanage = int(input('How much do you pay monthly to Property management? '))
        self.mortgage = int(input('How much is the monthly mortgage payment? '))

        self.expenses = self.tax + self.insurance + self.utilities + self.hoa + self.landscape + \
        self.vacancy + self.repairs + self.propmanage + self.mortgage 

        print(f'\nTotal monthly expense = {self.expenses}\n')


    def c_f(self):
        self.cashflow = self.income - self.expenses
        print(f'\nTotal monthly cash flow is {self.cashflow}\n')

    def ROI(self):
        self.down = int(input('What was your down payment? '))
        self.closing = int(input('What were the closing costs? '))
        self.rehab = int(input('What were to costs of renovations? '))
        self.misc = int(input('What were the miscellaneous costs'))

        self.cash_on_cash = self.down + self.closing + self.rehab + self.misc 

        print(f'Total Investment is {self.cash_on_cash}\n')

        self.annual_cf = self.cashflow * 12
        self.total_roi = self.annual_cf / self.cash_on_cash * 100
        print(f'\nTotal ROI percentage is {round(self.total_roi,2)}%\n') 
money = rental_income()
def run():
    while True:
        calculate = input(
            '\nWould you like to calculate the ROI of a rental property? If Yes type y, if No type n')
 
        if calculate.lower() == 'y':
            print(
                '\nFor any categories that are not applicable, please enter zero[0]\n\nFor all other values, enter the dollar amount rounded to the nearest dollar.\n')
            money.rent_income()
            money.spend()
            money.c_f()
            money.ROI()
        elif calculate.lower() == 'n':
            print('We are finished calculating rental ROI. Please come again!')
            break 
        else:
            print('Please type in y for Yes, or n for No')

run()            
