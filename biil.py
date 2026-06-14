print("------billing section------")
order_a_quantity = 2
order_a_rate = 180
total_a = order_a_quantity * order_a_rate
print("total for order a :" + str(total_a))
order_b_quantity = 1
order_b_rate = 320
total_b = order_b_quantity * order_b_rate
print("total for order b :" + str(total_b))
total_bill = total_a + total_b
print(" total bill amount :" + str(total_bill))
cash_given = 500
change = cash_given - total_bill
print("cash given :" + str(cash_given))
print("change :" + str(change))
budget = 1000
paratha_cost = 39
max_parathas = (budget // paratha_cost)
print("maximum parathas that can be bought with a budget of " + str(budget) + " is : " + str(max_parathas))
 
customer_number = 12345
remainder = customer_number % 100

print("remainder when coustmer number is divided by 100: " + str(remainder))


base_points = 4
multiplier = base_points ** 3
print("loyalty points multiplier: " + str(multiplier))



loyalty_points =50
