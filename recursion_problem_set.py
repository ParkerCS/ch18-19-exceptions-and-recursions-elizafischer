'''
- Personal investment
Create a single recursive function (or more if you wish), which can answer the first three questions below.  For each question, make an appropriate call to the function. (5pts each)
'''

#1.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY, so MPR is APR/12).  Assuming you make no payments for 6 months, what is your new balance?  Solve recursively.

money = 10000
apr = 20

monthly_apr = apr/12
#print(monthly_apr)

def one(money, month):
    apr = 0.20
    monthly_apr = apr / 12
    money += money * monthly_apr
    if month < 7:
        one(money, month + 1)
    if month == 6:
        money = round(money,2)
        print("You have $" + str(money), "after 6 months.")

print("\nProblem #1")
one(money, 1)
print()



#2.  You have $5000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  You make the minimum payment of $100 per month for 36 months.  What is your new balance?  Solve recursively.

def two(money, month):
    monthly_apr = 0.20 / 12
    money += money * monthly_apr
    money -= 100
    #if month < month + 1
    if month < 37:
        two(money, month +1)
    if month == 36:
        money = round(money,2)
        print("You have $" + str(money), "after 36 months of paying the minimum of $100 a month.")

print("Problem #2")
two(5000, 36)
print()

#3.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  If you make the minimum payment of $100 per month, how many months will it take to pay it off?  Solve recursively.

def three(money, month, done):
    monthly_apr = 0.20 / 12
    money += money * monthly_apr
    money -= 100
    money = round(money, 2)
    print(money)
    if month < 100 and not done:
        three(money, month +1, False)
    if money <= 0:
        done = True
        print("Your debt was paid off after" , month, "month(s).")

print("Promblem #3 doesn't work because you will never pay off your debt:")
three(10000, 1, False)
print()


#4  Pyramid of Cubes - (10pts) If you stack boxes in a pyramid, the top row would have 1 box, the second row would have two, the third row would have 3 and so on. Make a recursive function which calculates the TOTAL NUMBER OF BOXES for a pyramid of boxes n high.  For instance, a pyramid that is 3 high would have a total of 6 boxes. A pyramid 4 high would have 10.
def four(n, boxnum, index):
    pass

def blah(n_height, boxes, index):
    if index == 0:
        boxes = 0
    boxes += n_height

    if n_height != 0:
        blah(n_height - 1, boxes, index + 1)

    elif n_height == 0:
        print("There would be", boxes, "boxes for that number of rows")

blah(int(input("Enter a number of rows: ")), 0, 0)