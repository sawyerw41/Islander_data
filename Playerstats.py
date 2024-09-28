lastnames = r'data\lastnames.txt'



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



'''
Makes sure you put in a valid situation and also allows you to type 'info' so you can get a list of valid situations
Will tell you that you didnt enter a valid situation if that is the case and will keep repeating untill you do
'''
def find_situation():



    situation = ''
    while True:
        situation =input('\nWhat situation do you want to see stats for? \nType "info" for what types ')
        if situation == "info":
            #gives you the type of situations you can look for and re prompts you
            print("\nall","5on5",'4on5','5on4','other',sep="\n")
            situation =input('What situation do you want to see stats for? ')
        if situation != 'all' and (situation != '5on5') and (situation != '4on5') and (situation !='5on4') and (situation !='other'):
            #apears if you didnt put a valid input and starts the prompt over in order to prevent breaks
            print('You didnt enter in a valid situation please try again or press info to see your opions')
            situation == ""
        else:
            return situation
            break


def find_player():
    
    while True:
        
        
        
        player_name = input('Enter a players last name or type "player list" to get a list of names: ')
        if player_name == 'player list':
            print_lines_last(lastnames)
            continue

        
        
        is_player = player_search(player_name)

        
        
        if is_player == True:
            return player_name
            break
        
        else:
            print("try again")


        







def player_search(player_name):
   
    with open(r'data\lastnames.txt') as my_file:
        word = player_name
        
        player_found = False
        for line in my_file:
            stripped_line = line.strip()
            if stripped_line.lower() == word.lower():
            
                player_found = True

        return player_found        
    
  
    

def find_season(file,situation,season):
    with open(file) as my_file:
        for line in my_file:
            splitline = line.split(",")
            
            if ((splitline[1] == str(season)) and (splitline[5] == situation)):
                
                assist = float(splitline[33]) - float(splitline[34])
                print(splitline[2],"had",splitline[33],"points with",splitline[34],"goals",assist,"assist")    
            





def main():
    Player_name = find_player()
    season = int(input("What season Stats do you want to see? "))
    situations = find_situation()
    player_file = convert_name_into_file(Player_name)
    find_season(player_file,situations,season)
   
     
        

    


    #print_lines_last(player_file)

main()