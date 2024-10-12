
import csv
import plotter
lastnames = r'data\lastnames.txt'
single_season = "s"
graph = "g"




def print_lines(file_name):
    with open(file_name) as my_file:
        next(my_file)
        for line in my_file:
            tokens = line.split(',')
            print(tokens[1],tokens[2])

def print_lines_last(file_name):
    with open(file_name) as my_file:
       
        for line in my_file:
            
            print(line)

def convert_name_into_file(playername):
    
    player_file_name = ""
    txt = r"data\{price}.csv"
    player_file_name = (txt.format(price = playername))
    
    return player_file_name

def points_graph(file,situation,playername):
    
    with open(file) as my_file:
        plotter.init(playername,"Season","points")
        plotter.new_series("Points total")
        for line in my_file:
            splitline = line.split(",")
            
            if (splitline[5] == situation):
                plotter.add_data_point(float(splitline[33]))
                
            
          
        plotter.plot()


'''
Makes sure you put in a valid situation and also allows you to type 'info' so you can get a list of valid situations
Will tell you that you didnt enter a valid situation if that is the case and will keep repeating untill you do
'''
def find_situation():



    situation = ''
    while True:
        situation =input('\nWhat situation do you want to see stats for? \nType "info" for what types: ')
        if situation == "info":
            #gives you the type of situations you can look for and re prompts you
            print("\nall","5on5",'4on5','5on4','other\n',sep="\n")
            situation =input('What situation do you want to see stats for: ')
        if situation != 'all' and (situation != '5on5') and (situation != '4on5') and (situation !='5on4') and (situation !='other'):
            #apears if you didnt put a valid input and starts the prompt over in order to prevent breaks
            print('You didnt enter in a valid situation please try again or press info to see your opions')
            situation == ""
        else:
            return situation
            break

# makesn sure you enter a valid player name so that there is a file to get for them
def find_player():
    
    while True:
        
        
        
        player_name = input('\nEnter a players last name or type "player list" to get a list of names: ')
        if player_name == 'player list':
            print_lines_last(lastnames)
            continue

        
        
        is_player = player_search(player_name)

        
        
        if is_player == True:
            return player_name
            break
        
        else:
            print("try again")


        






# finds out if the player is in the data base and returns false if they are not
# works inside of find player
def player_search(player_name):
   # turns the players name into a file
    with open(r'data\lastnames.txt') as my_file:
        word = player_name
        
        player_found = False
        for line in my_file:
            stripped_line = line.strip()
            if stripped_line.lower() == word.lower():
            
                player_found = True

        return player_found        
    
  
    
'''
prints out the data if the user is looking for a season stats
needs the players file and information from situation and season in order to identify the right line in the csv files


'''
def find_season(file,situation,season):
    # fixes the ending based on what situation the stat is for
    ending = ""
    if situation == "all":
        ending = 'during all situations.'
    if situation == '5on5':
        ending = "on 5on5 situtations."
    if situation == '4on5':
        ending = "on the penalty kill."
    if situation == '5on4':
        ending = "on the power play."
    if situation == 'other':
        ending = " during other situations"


    
    
    
    with open(file) as my_file:
        for line in my_file:
            splitline = line.split(",")
            
            if ((splitline[1] == str(season)) and (splitline[5] == situation)):
                #changes the values into ints and makesn them more readable
                assist = int(float(splitline[33]) - float(splitline[34]))
                goals = int(float(splitline[34]))
                points = int(float(splitline[33]))
                player_name = splitline[2]
                print('\n',player_name," had ",points," points with ",goals," goals ",assist," assist in the ",season,' season ',ending,sep="")    
            


def print_functions():
    print('\ng - points graph\ns - player season stats\nquit - exit the program')

def is_season(playerfile):
    while True:
        season_input=str(input("\nEnter in a season you want to see stats for or type 'rookie' to see rookie season sats: "))
        if season_input == 'rookie':
            return find_rookie_season(playerfile) 
        
        elif is_season_helper(season_input,playerfile) == True:
            return season_input
       
        else:
            print("Invalid Season Try again")



def is_season_helper(season_input,playerfile):


    with open(playerfile) as saeasonsearchfile:
        
       
                
            is_a_seasson = False
            for line in saeasonsearchfile:
                splitline = line.split(",")
                if splitline[1] == str(season_input):
                    is_a_seasson = True
            
            
            
    return is_a_seasson

                    

def find_rookie_season(player_file):
    with open(player_file) as playfile:
        next(playfile)
        rookie_line = next(playfile)
        rookie_line2 = rookie_line.split(",")
        season = rookie_line2[1]

    return season
        
        





def main():
    
    print('\nWelcome to the Islanders data base program \ntype "about" to see and about page \ntype "commands" to see what commands you can use')
    '''
    lets the user enter the commands that detrim what function they get
    '''
    while True:
        cmd = input("\nEnter command: ")
        if cmd == graph:
            # gets the information for the player and what situation they want and plots their points in that situation on a graph
            Player_name = find_player()
            situations = find_situation()
            player_file = convert_name_into_file(Player_name)
            points_graph(player_file,situations,Player_name)
        if cmd ==single_season:
            # prints out a statline with points assist and goals if the user types in s
            Player_name = find_player()
            situations = find_situation()
            player_file = convert_name_into_file(Player_name)
            season = is_season(player_file)
             
            find_season(player_file,situations,season)
        if cmd == 'quit':
            break
        if cmd == "commands":
            print_functions()
    
    
    
    
    
    
    
    
    

  
    
          
    
  


        
    
    
     
        

    


 

main()