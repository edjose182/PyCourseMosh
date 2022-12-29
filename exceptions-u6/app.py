from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

print("First Code",timeit(code1,number=10000))  ##number tell how many times will
                                                ## repeat the operation
