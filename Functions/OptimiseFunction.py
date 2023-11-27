
"""
this is a function that alow the user to enter multiple values
so the * in front of the parameter indicate that, when the function will be call, it can takes multiple values.


the state in the function is an optimise way of writing a for loop in python,
the benefits of doing this permit us to gain more time in our programme execution
"""
def multilple_persone(*persons):
    [print(f"Hello {person} !") for person in persons]



"""
as seen benith, i have called the function and writing into it parameter multiple parameters values.
once i click on run
"""
multilple_persone("FredWil", "willy")