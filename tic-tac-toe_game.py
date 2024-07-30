import itertools



def win(current_game):
    def all_same(l):
        if l.count(l[0])==len(l) and l[0]!=0:
            return True
        else:
            return False
        
    #diagonally
    diags=[]
    for col,row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print("Winner is (/) diagonal")
        return True
        
    diags=[]
    for i in range(len(game)):
        diags.append(game[i][i])
    if all_same(diags):
        print("Winner is (/) diagonal")
        return True
    
    
    #vertical
    for col in range(len(game)):
        check = []
       
        for row in game:
            check.append(row[col])

        if all_same(check):
            print("winner is vertically(|)")
            return True
           

    #horizontal
    for row in game:
        print(row)
        if all_same(row):
            print ("winner is horizontally(-)")
            return True
    
    return False
            
            
            
            
            
            

def game_board(gamesize,game_map, player=0,row=0,column=0,just_display=False):
    
        
        
    try:
        s=" "
        if game_map[row][column]!=0:
            print("this place is already occupado!")
            return game_map, False
            
            
            print(s)
        if not just_display:
            game_map[row][column]=player
       
        for count, row in enumerate(game_map):
            print(count,row)
            
        return game_map, True
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return game_map, False
    
        
        
        
        
        
        
        
play=True

players=[1,2]

while play:
    gamesize=int(input("enter size of game tic-tac-toe"))
    s=" "
    for i in range(gamesize):
        s+="  "+str(i)
    print(s)
    game=[[0 for i in range(gamesize)] for i in range(gamesize)]

    
    
    game_won=False
    
    game,_=game_board(gamesize,game,just_display=True)
    player_choice=itertools.cycle([1,2])
    
    
    
    
    while not game_won:
        current_player=next(player_choice)
        print(f"\nplayer {current_player}")
        
        played = False
        while not played:
            column_choice=int(input("enter column : "))
            row_choice=int(input("enter row : "))
            game,played=game_board(gamesize,game,current_player,row_choice,column_choice)
        
        if win(game):
            game_won=True
            again=input("do you wnna play again(y/n) ")
            if again.lower()=="y":
                print("restating")
            elif again.lower()=="n":
                play=False
                print("se you later")
            else:
                print("invalid input")
                play=False
        
        