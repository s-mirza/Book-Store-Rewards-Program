"""

Author: Sarah Mirza

Program Title: Book Store Rewards

File Description:

<Briefly describe the programs and its goals.>

"""

num_of_books = int(input("How many books did you purchase this month? "))
subtotal = 0
points_earned = 0
for books in range(1, num_of_books + 1):
  price_of_books = float(input(f"Enter price for Book {books}: $"))
  subtotal= subtotal+price_of_books


print("********************************************")
print("                 Receipt                    ")
print("********************************************")
taxes_owed = subtotal * 0.07
final_price = subtotal + taxes_owed
if subtotal >= 20 and subtotal < 40:
    points_earned = 5
elif subtotal >= 40 and subtotal < 60:
    points_earned = 15
elif subtotal >= 60 and subtotal < 80:
    points_earned = 30
elif subtotal >= 80 and subtotal < 100:
    points_earned = 60
elif subtotal >= 100:
    points_earned = 120
    
print(f"          Sub Total: $ {subtotal:>5.2f}")
print(f"         Taxes Owed: $ {taxes_owed:>5.2f}")
print("********************************************")
print(f"              Total: $ {final_price:>5.2f}")
print(f"      Points Earned:   {points_earned:>5.2f}")
print("********************************************")

