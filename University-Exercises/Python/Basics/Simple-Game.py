where = input("Take left or right: ")
attempt = 0
while where != "right":
   where = input("Try again: ")
   attempt += 1
print (f"You Got Out after {attempt+1} attempt{'s' if attempt > 1 else ''}")
