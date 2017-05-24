#S.McDonald 12/2/2016
#total_sales
#This program receives an amount of sales for each day of the week from the
#user and then calculates the total sale for the week and displays it.


def main():

    #input
    #receive total sales for each day from user
    Monday = float(input("Please enter the total store sales for Monday: "))
    Tuesday = float(input("Please enter the total store sales for Tuesday: "))
    Wednesday = float(input("Please enter the total store sales for Wednesday: "))
    Thursday = float(input("Please enter the total store sales for Thursday: "))
    Friday = float(input("Please enter the total store sales for Friday: "))
    Saturday = float(input("Please enter the total store sales for Saturday: "))
    Sunday = float(input("Please enter the total store sales for Sunday: "))

    #list that holds store's sales for each day
    sales = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday] #list: all 7 days of the week

    #processing
    #calculate total weeks sales using a loop
    total_sales = 0 #start total_sales at 0
    for store in sales:
        total_sales += store #compute total sales
    #output/display   
    print("Total weekly sales: $", format(total_sales, ',.2f'), sep='') #display total weekly sales


#call main()
main()
    

