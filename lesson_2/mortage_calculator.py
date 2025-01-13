
loan_amount = int(input('what is the loan amount?'))
apr = float(input('what is the annual apr?'))
loan_duration = int(input('how many years is the loan?'))

def calculate_monthly_amount(loan_duration,loan_amount,apr): 
    rate = (apr/100)/12
    months = loan_duration * 12
    payment = loan_amount * (rate / (1-(1+rate)**(-months)))
    payment_rounded = round(payment,2)
    return (f'your monthly payment is ${payment_rounded}')

print(calculate_monthly_amount(loan_duration,loan_amount,apr))