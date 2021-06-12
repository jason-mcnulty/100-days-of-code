# Project Jackal
# Project Jackal will be used to track the buying and selling of stocks

###########################################################################

###########################################################################
# Version 1  
#stock_ticker = 'AAPL'
#number_shares = 200
#stock_price = 350.00

# Perform math here
#total = (number_shares * stock_price)
#str_total = str(total)

# Convert to string 
#str_number_shares = str(number_shares)
#str_stock_price = str(stock_price)

# Print output
#print( 'You bought or sold ' + str_number_shares + ' shares of ' + stock_ticker + ' at $' + str_stock_price + ' per share, '
#+ 'for a total of ' + '$' + str_total + ' dollars')
###########################################################################

###########################################################################
# Version 2 of this code to use the imput function. 
# Gather input values
print ('What is the ticker of your stock?')
stock_ticker = input()
print('How many shares do you want to buy')
number_shares = input()
stock_price = 350.00 # this will eventually come from a web API 


# Convert strings and folats to ints for math


# Perform math here



total = int(str(number_shares)) * int(float(stock_price))

# Output
print ('You are about tp purchase ' + str(int(number_shares) + 'of ' + stock_ticker + 'at a price of ' + str(int(stock_price))))
print(' for a total of ' + str(int(total)))
###########################################################################
