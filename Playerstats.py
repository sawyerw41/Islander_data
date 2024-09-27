


def print_lines(file_name):
    with open(file_name) as my_file:
        next(my_file)
        for line in my_file:
            tokens = line.split(',')
            print(tokens[1],tokens[2])




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
    player_name = input('Enter a players name or type "player list" to get ')



def main():
    Player_name = "Enter players name"
    season = int(input("What season Stats do you want to see? "))
    situations = find_situation()
    print(situations)
     
        

    


   # print_lines("barzal.csv")

main()