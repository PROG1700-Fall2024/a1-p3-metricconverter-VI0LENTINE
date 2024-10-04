#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #the numbers of tons, stones, pounds, and ounces are input by the user
    tons = float(input("Please insert the number of tons: "))
    stones = float(input("Please insert the number of stone: "))
    pounds = float(input("Please insert the number of pounds: "))
    ounces = float(input("Please insert the number of ounces: "))

    #the weight should be converted entirely into #ounces (the lowest common denominator) and then divided by 35.274 to obtain the value in kilos
    tOunces = 35840 * tons + 224 * stones + 16 * pounds + ounces
    tKilos = float(tOunces / 35.274)

    #The Python int function should be used to break the total number of kilos into a whole number of metric tons and kilos.
    mTons = float(tKilos/1000)
    intTons = int(mTons)
    kilos = (float(mTons) - intTons)*1000
    intKilos = int(kilos)
    grams = (float(kilos) - intKilos)*1000 

    #Metric tons, kilograms, and grams (The number of grams should #be displayed to one decimal place.)
    print("The metric weight is: ",int(mTons),"metric tons, ",int(kilos),"kilos, and ",round(grams, 1),"grams.")

    # YOUR CODE ENDS HERE

main()