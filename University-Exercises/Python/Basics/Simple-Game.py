# ask the user to go left or right
where = input("Take left or right: ")

#to count attempts that user make
attempt = 0

#This condition cheks that user will not take the wrong option
while where != "right":
   where = input("Try again: ")

   #Each failure will be added to the counter 
   attempt += 1

#This prints how many attempts you've made to find the right option so far. 
print (f"You Got Out after {attempt+1} attempt{'s' if attempt > 1 else ''}")
