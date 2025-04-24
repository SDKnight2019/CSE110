#%%
price_of_childs_meal = float( input ("What is the price of a child's meal? "))
price_of_adults_meal = float( input ("What is the price of an adults meal? "))
how_many_children = int( input ("How many children are there? "))
how_many_adults = int( input ("How many adults are there? "))
sales_tax = float( input ("what is the sales tax percent? "))
tip = float( input ("How much would you like to tip? "))
subtotal = ( price_of_childs_meal * how_many_children ) + ( price_of_adults_meal * how_many_adults )
print ( "-"*20 )
print (f"Subtotal: ${subtotal:.2f}")
print ( "-"*20 )
tax_total = ( sales_tax / 100 * subtotal)
print ( "-"*20 )
print (f"Sales tax: ${tax_total:.2f}")
print ( "-"*20 )
print ( "-"*20 )
print (f"Tip: ${tip:.2f}")
print ( "-"*20 )
Total = tax_total + subtotal + tip
print ( "-"*20 )
print (f"Total: ${Total:.2f}")
print ( "-"*20 )
payment_amount = float ( input ("What is your payment amount? "))
change = payment_amount - Total
print ( "-"*20 )
print (f"Change: {change:.2f}")
print ( "-"*20 )

#Coding is actually cool!
# %%
