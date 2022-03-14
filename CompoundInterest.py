# Calculate the compound interest.

def calcInterest(principal, rate, years):
    """
    Calculate the compound interest.
    """
    return principal * (1 + rate / 100) ** years

if __name__ == '__main__':
    principal = float(input("Enter the principal: "))
    rate = float(input("Enter the rate: "))
    years = int(input("Enter the number of years: "))
    print("The compound interest is", calcInterest(principal, rate, years))
