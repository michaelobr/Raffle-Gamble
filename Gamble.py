#Short introduction of the purpose of this program
print("This short little program will help determine the probability of profitability and ROI from playing 50/50 raffles.")

#The number of tickets the user will purchase
num_user_tickets = int(input("How many tickets will you purchase? ")) 

#The total amount of tickets sold to everybody participating in the 50/50 raffle, this includes the user's. 
sum_tickets_sold = int(input("How many tickets in total are expected to be purchased? ")) 

#Parentheses must be used here, because multiplication comes before divsion in the order of operations which Python adheres to.
winning_probability = (num_user_tickets / sum_tickets_sold) * 100 

ticket_price = int(input("What is the price per 50/50 ticket? ")) 

#Only 50% of the total ticket sales is available to win, so we must divide by 2 here
possible_winnings = (sum_tickets_sold * ticket_price) / 2 

#profit = revenue - cost. If the number is negative, then it is a loss, but the same formula is still used. 
profit = possible_winnings - (num_user_tickets * ticket_price)

#Return on Investment = profit (or loss) from investment / cost of investment 
ROI = ((profit) / (num_user_tickets * ticket_price)) * 100 

#No " " is needed after "purchase," num_user_tickets, etc. because Python automatically includes a space.
print("If you purchase", num_user_tickets, "ticket(s) at a price per ticket of $", ticket_price, "for a total of $",
     (num_user_tickets * ticket_price), "you have a", (winning_probability), "% of winning $", possible_winnings, ".")
print("This would result in a profit of $", profit, "and a ROI of", ROI, "%.")

