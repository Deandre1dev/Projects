import math
#User inputs investment or bond
print("investment-to calculate the amount of intrest you'll earn on your investment ")
print("bond-to calculate the amount you'll have to pay on a home loan\n")
bond_or_investment=(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))
capatalized_input=bond_or_investment.capitalize()
print(capatalized_input)
#If statements to determine which calculator is needed
if capatalized_input=="Investment":
    deposit=(float(input("Enter amount of money your depositing: ")))
    intrest=(int(input("Enter the intrest rate: ")))/100
    investmment_period=int(input("Enter the amount of years for the investment: "))
    simple_or_compound=(input("Simple intrest or compound intrest: "))
    capatalized_simple_or_compound=simple_or_compound.capitalize()
#calculator is determined
    if capatalized_simple_or_compound=="Simple intrest":
        simple_intrest=(deposit*(1+intrest*investmment_period))
        print("Simple intrest="+(str(simple_intrest)))
    elif capatalized_simple_or_compound=="Compound intrest":
        capatalized_simple_or_compound=simple_or_compound.capitalize()
        compound_intrest=(deposit*math.pow(1+intrest,investmment_period))
        print("Compound intrest="+(str(compound_intrest)))
#elif statement for bond repayment
elif capatalized_input=="Bond":
   repayment_amount= (float(input("Enter value of the houses: ")))
   annual_intrest=(int(input("Enter annual intrest rate: "))/100)/12
   months=(int(input("Number of months: ")))
   repayment=(annual_intrest*repayment_amount)/(1-(1+annual_intrest)**(-months))
   print("Repayment="+(str(repayment)))
#Error statement
else:
    print("Please enter an apropriate option!")


