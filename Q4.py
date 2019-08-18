print (" DAYS BETWEEN TWO DAYS ")

a1 = int (input("PLEASE PROVIDE THE SMALLEST YEAR:/n "))
b1 = int (input ("PLEASE PROVIDE THE SMALLEST MONTH:/n "))
c1 = int (input ("PLEASE PROVIDE THE SMALLEST DAY:/n "))

date1 = (a1,b1,c1)

a2 = int (input ("PLEASE PROVIDE THE LARGEST YEAR:/n "))
b2 = int (input ("PLEASE PROVIDE THE LARGEST MONTH:/n "))
c2 = int (input ("PLEASE PROVIDE THE LARGEST DAY:/n "))

date2 = (a2,b2,c2)

difference_between_years = (a2-a1)
difference_between_months = (b2-b1)
difference_between_days = (c2-c1)
print ("the gap between two dates is"+str (difference_between_years)+"years",str (difference_between_months)+"months",str(difference_between_days)+"days")