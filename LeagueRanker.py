

while True:
    try:
        TeamsGroupNumber = int(input("\nHello, Please enter the number of teams to rank (min 2, max 8 groups):\n"))  #We request the number of teams to rank
        if 2 <= TeamsGroupNumber <= 8: 
            print(f"The number is: {TeamsGroupNumber}\n")    #define the range if the number is inside of the range we print it to confirm the value and break the cycle                                                             
            break  
        else:
            print("Error: The number should be between 2 and 8. Please follow the instructions")   #error message if the input is incorrect                                                                                                                
    except ValueError:                                                                                               
        print("Unexpected error")                                                                        


TeamsDefined=[]               #array to save all the groups

for i in range (0,TeamsGroupNumber):
    try:
        TeamName = input(f"Enter team name (max 12 characters, no spaces, '000' not allowed): \n")   #capture the team name 1 by 1
        if len(TeamName) > 12 or ' ' in TeamName or TeamName == "000":       #input criteria
            print("Invalid team name. Please follow the instructions.")
        else:      
            TeamsDefined.insert(i,TeamName)                           #make the Teams list
    except ValueError:
            print("Unexpected error")

print(f"\nThe Teams are: {TeamsDefined[0:TeamsGroupNumber]}\n")       #print the Teams list to confirm

TeamsRanking = []                                        #list to be modified according with the game results
points=0                                                #initial points

for i in range(TeamsGroupNumber):
    TeamsRanking.append(TeamsDefined[i])                 # add the team number
    TeamsRanking.append(points)                          # Add the points

print(f"The initial rank is: {TeamsRanking}\n")          # show the final result

while True:
    try:
        Gamesplayed = int(input("\nHello, Please enter the number of games that took place (min 1, max 10 games):\n"))    #We request the number of teams to rank
        if 1 <= Gamesplayed <= 10: 
            print(f"Games confirmation: {Gamesplayed}\n")                 #range if the number is correct we print it and break the cicle                                                             
            break  
        else:
            print("Error: The number should be between 1 y 10.")          #error message                                                                                                                 
    except ValueError:                                                                                               
            print("Unexpected error") 


for Game in range(Gamesplayed):
    comparison = 0                                          #to ensure the team exist
    position1 = position2 = Result1 = Result2 = None        #to save the results and position inside of the list for future operations

    while True:  
        input_game = input("\nHello, please enter the results for the game (Format: Team1 X, Team2 Y):\n").strip() #request the game information
        
        try:
            team1, score1, team2, score2 = input_game.replace(",", "").split()                       #divide the input data
            score1, score2 = int(score1), int(score2)                                                #convert the points to int
        except ValueError:
            print("Invalid format. Please use: Team1 X, Team2 Y format")                            #ask again if the input is incorrect
            continue  

        if team1 in TeamsRanking and team2 in TeamsRanking:                                           #verify if the teams exist in the previous ranking list
            position1 = TeamsRanking.index(team1)                                                    #capture the position 
            position2 = TeamsRanking.index(team2)                                                    #capture the position 
            Result1, Result2 = score1, score2                                                       #capture the results
            break                                                                                             
        else:
            print("One or both teams are invalid. Please follow up the format")                   #try again if the teams are invalid

    print(f"\nGame confirmation:")                                                               #Print the data to verrify the progress this won't be visible for the customer in the future
    print(f"   {team1} Position: {position1} Score value: {Result1}")
    print(f"   {team2} Position: {position2} Score value: {Result2}\n")
    
    if Result1 > Result2:                                                                         #Update the ranking for each game
        TeamsRanking[position1+1] += 3           
    if Result1 < Result2: 
        TeamsRanking[position2+1] += 3   
    if Result1 == Result2:
        TeamsRanking[position1+1] +=1 
        TeamsRanking[position2+1] +=1 
    else:
        print("")  
        #do nothing
print("Current Ranking:") 
print(TeamsRanking)                          #Print the ranking updated to verify