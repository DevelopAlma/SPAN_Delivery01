
while True:
    try:
        TeamsGroupNumber = int(input("Hello, Please enter the number of teams to rank (min 2, max 8 groups):\n"))  #We request the number of teams to rank
        if 2 <= TeamsGroupNumber <= 8: 
            print(f"The number is: {TeamsGroupNumber}\n")            #range if the number is correct we print it and break the cicle                                                             
            break  
        else:
            print("Error: The number should be between 2 y 8.")      #error message                                                                                                                 
    except ValueError:                                                                                               
        print("")                                                                        


TeamsDefined=[]      #array to define all the groups

for i in range (0,TeamsGroupNumber):
    try:
        TeamName = input(f"Enter team name (max 12 characters, no spaces, '000' not allowed): \n")   #capture the team name 1 by 1
        if len(TeamName) > 12 or ' ' in TeamName or TeamName == "000":                             #input criteria
                print("Invalid team name. Try again.")
        else:      
            TeamsDefined.insert(i,TeamName)                                              #make the Teams list
    except ValueError:
                print("Error: Please enter a valid name")

print(f"The Teams are:{TeamsDefined[0:TeamsGroupNumber]}\n")            #print the Teams list

