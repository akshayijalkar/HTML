#exact rupees needed to make payment
#create function
def make_amount(rupees_to_make,no_of_five,no_of_one):
    #necessary variables
    five_needed=0
    one_needed=0

    #base calculations
    one=no_of_one*1
    five=no_of_five*5
    amount_have=one+five
    
    #method selection and calculations
    if rupees_to_make < amount_have:
        one_needed=rupees_to_make%5
        rem=rupees_to_make-one_needed
        five_needed=rem/5
     
    elif rupees_to_make==amount_have:
        one_needed=no_of_one
        five_needed=no_of_five
   
    else:
        print(-1)
        
    
    #Populate the variables: five_needed and one_needed


    #print output
    print("No. of Five needed :", five_needed)
    print("No. of One needed  :", one_needed)

    #return output to function
    return five_needed
    return one_needed

#call function with values
#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(37,8,5)