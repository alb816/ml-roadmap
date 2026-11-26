from math import factorial

def birthday_problem(n: int, days: int = 365) -> float:
    """
    Calculate the probability that at least two people share the same birthday.
    
    Args:
        n: Number of people in the group
        days: Number of days in a year (default 365)
    
    Returns:
        float: Probability of at least one shared birthday, rounded to 4 decimal places
    """
    if n <= 1: 
        return 0.0
    if n > days:
        return 1.0
    
    no_matches = factorial(days) / (factorial(days - n) * days ** n)
    matches_bday = 1 - no_matches

    return round(matches_bday, 4)


if __name__ == '__main__':
    print(birthday_problem(23))