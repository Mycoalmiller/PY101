from datetime import datetime

age = int(input('what is your age?'))
retire = int(input('what age would you like to retire?'))
a = (retire - age)
year = datetime.now().year

def retirement():

    year_of_retirement = year + a
    return (f'What is your age? {age}'
        f' at what age would you like to retire? {retire}'

        f' its {year}. you will retire in {year_of_retirement}.'
        f' you have only {a} years of work to go!')

print(retirement())