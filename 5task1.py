dict={"Alice":85,"Nishta":90,"Alfiya":67}
a=input("Enter students name:")

if a in dict:
    print(""+a+"'s Marks:",dict[a])
else:
    print("Student name not found")