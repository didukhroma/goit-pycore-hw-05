import re
from typing import Generator

def generator_numbers(text:str)->"Generator[float]":
    pattern = r'\d+\.\d+'
    for number in re.findall(pattern,text) :
        yield float(number)


def sum_profit(text:str, generator_numbers:"Generator[float]")->float:   
    return sum(generator_numbers(text)) 
    



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")

