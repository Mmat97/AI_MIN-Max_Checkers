import time



#first two for regular pieces 
max_moves_black = [ (-1, 1),  (1, 1)]
max_moves_white = [ (-1, -1),  (1, -1)]
max_moves = [ (-1, 1),  (1, 1),  (1, -1),  (-1, -1)] #ex: diagonla right down is (1, 1)


white_edge=[ (0, 7), (2, 7), (4, 7), (6, 7)]

black_edge=[(1, 0), (3, 0), (5, 0), (7, 0)]



class InputClass:
    gameName = ""
    color=""
    enemy_color=""
    time_remain=0.0
    my_pieces=[]
    my_kings=[]
    enemy_pieces=[]
    enemy_kings=[]
    game_board=[]


def check_status(new_loc):
    #check if in board
    a=0 <= new_loc[0] < 8
    b=0 <= new_loc[1] < 8
    if a and b:
        return True
    else:
        return False
    
def check_if_enemy(inputProc,enemy_loc):

    if(enemy_loc in inputProc.enemy_pieces):
        return True
    else:
        return False
    
    
def get_jumps(piece_loc, inputProc,visited_so_far,g,piece_loc_status):#if and how update piece loc for my_piece and further board
    possible_jumps = []
    z_moves=[]
    q=0
    if(inputProc.color=="WHITE"):
        z_moves=max_moves_white
    elif(inputProc.color=="BLACK"):
        z_moves=max_moves_black
    if(piece_loc_status==True):
        z_moves=max_moves
        
    for move in z_moves:
        if(q>0):
            break
        x=piece_loc[0] + move[0]
        y=piece_loc[1] + move[1]
        enemy_loc = (x, y) #check if enemy location valid-could be anywhere in currpos+z_moves 
        
        if(check_status(enemy_loc)):
         
            if check_if_enemy(inputProc,enemy_loc) and inputProc.game_board[enemy_loc[1]][enemy_loc[0]] != '.':#if enemy yeah, else return because 
                
                 
                 x=enemy_loc[0] + move[0]
                 y=enemy_loc[1] + move[1]
                 new_loc = (x, y)
                 
                 #check if location behind enemy is valid 
                 if check_status(new_loc) and inputProc.game_board[new_loc[1]][new_loc[0]] == '.':
                     #starting from curr location since need to keep track of jumps
                    
                     if new_loc not in visited_so_far:
                         visited_so_far.append(new_loc)#add first jump, but if another in same direction or another....
                         q=q+1
                        
                         possible_jumps.append(new_loc)
                         if(inputProc.color=="BLACK" and new_loc in white_edge or (inputProc.color=="WHITE" and new_loc in black_edge) and piece_loc_status!=True):
                             continue   
                            
                         
                        
                         x=get_jumps(new_loc, inputProc, visited_so_far,g+1,piece_loc_status)

                         for jump in x:
                              
                             possible_jumps.append(jump) #append
                             
                         
    return possible_jumps
    
    
    
    
def get_valid_move_s(piece_loc,inputProc):
    color=inputProc.color
    possible_moves=[]
    visited_so_far=[piece_loc]
     
    #jumps for priority
    g=0
    piece_loc_status=False
    if(piece_loc in inputProc.my_kings):
        #z_moves=max_moves
        piece_loc_status=True
    possible_moves.extend(get_jumps(piece_loc, inputProc,visited_so_far,g,piece_loc_status))#for loop of this function so do possiblemoves for EACH piece
    if(len(possible_moves)>0):
        return possible_moves
    
    if(inputProc.color=="WHITE"):
        z_moves=max_moves_white
    elif(inputProc.color=="BLACK"):
        z_moves=max_moves_black
    if(piece_loc in inputProc.my_kings):
        z_moves=max_moves
    for m in z_moves:#global
       
        #check for possible new location from all choices
        new_loc=(piece_loc[0] + m[0], piece_loc[1] + m[1])
        
        #can move to that place if...
        if check_status(new_loc) and inputProc.game_board[new_loc[1]][new_loc[0]] == '.':
            possible_moves.append(new_loc)
            return possible_moves#FOR SINGLE JUST NEED ONE VALID-[(5, 4)], [(5, 4), 5], (2, 7)] error########################
    return possible_moves#else jumps or nothing
        
    

    
    
def solution_value(inputProc):#check if return is greater than alpha or less than beta
    #assume enemy makes best move(WHY WE USE MINIMAX) maxzime minimize for reverse fo what we are doing 
    #score=#mmypieces-#enemy
    #mmypieces wants score as big as possible
    #enemy wants to minimize score
    #ex: enemy move at depth three or depth two or whatever(white wants minimum score since means more white)
    #depth is numbe rmoves ahead
    #print((len(inputProc.my_pieces) - len(inputProc.enemy_pieces)))                                                               
    return (len(inputProc.my_pieces) - len(inputProc.enemy_pieces)), (), []
    
    







    
def get_jumps_g(piece_loc, inputProc,visited_so_far,piece_loc_status,z_moves, enemies_defeated):

                
               
    
    
    
    
    
    
    possible_jumps = []
    q=0
    z={}
    for move in z_moves:
        x=piece_loc[0] + move[0]
        y=piece_loc[1] + move[1]
        enemy_loc = (x, y) #check if enemy location valid-could be anywhere in currpos+z_moves 
        
        if(check_status(enemy_loc)):
         
            if check_if_enemy(inputProc,enemy_loc) and inputProc.game_board[enemy_loc[1]][enemy_loc[0]] != '.':#if enemy yeah, else return because 
                
                 
                 x=enemy_loc[0] + move[0]
                 y=enemy_loc[1] + move[1]
                 new_loc = (x, y)
                 
                 #check if location behind enemy is valid 
                 if check_status(new_loc) and inputProc.game_board[new_loc[1]][new_loc[0]] == '.':
                     #starting from curr location since need to keep track of jumps
                  
                     if new_loc not in visited_so_far:
                         enemies_defeated.append(enemy_loc)###############################################
                         visited_so_far.append(new_loc)#add first jump, but if another in same direction or another....
                         q=q+1
                            
                        
                         possible_jumps.append([new_loc])
                         z[new_loc]=[new_loc]
                         
                         
                         if(inputProc.color=="BLACK" and new_loc in white_edge or (inputProc.color=="WHITE" and new_loc in black_edge)  and piece_loc_status!=True ):
                             continue   
                            
                         x, enemies_defeated=get_jumps_g(new_loc, inputProc, visited_so_far,piece_loc_status,z_moves,enemies_defeated)
                         
                       
                               
                                    
                         
                         if(x!=[]):
                             
                             for jump in x.values():
                                 if(len(x.values())==1):
                                     z[new_loc].extend(jump)######add new array for each move
                                     break
                                 else:
                                     qq=0
                                     for j in jump:
                                         if(new_loc!=j):
                                            z[new_loc[0]+qq,new_loc[1]+qq]=[new_loc]
                                         
                                         z[new_loc[0]+qq,new_loc[1]+qq].extend(jump)
                                            
                                         qq=qq+10
                                     
                                    
                          

                        
                         
                                    
                                
                                    
                             
    #return possible_jumps   
    return z, enemies_defeated




def get_valid_move_g(piece_loc,inputProc):
    color=inputProc.color
    possible_moves=[]
    visited_so_far=[piece_loc]
    
    piece_loc_status=False
        
    
    if(piece_loc in inputProc.my_kings):
        piece_loc_status=True
    
    
    if(inputProc.color=="WHITE"):
        z_moves=max_moves_white
    elif(inputProc.color=="BLACK"):
        z_moves=max_moves_black
    if(piece_loc_status==True):
        z_moves=max_moves
    
    dd, enemies_defeated=get_jumps_g(piece_loc, inputProc,visited_so_far,piece_loc_status,z_moves,[])

    
    


    possible_moves=dd
    if(bool(possible_moves)):
        return possible_moves, enemies_defeated


    
    possible_moves={}
    yy=0
    for m in z_moves: 
        new_loc=(piece_loc[0] + m[0], piece_loc[1] + m[1])
        
        if check_status(new_loc) and inputProc.game_board[new_loc[1]][new_loc[0]] == '.':
            
            x=((piece_loc[0],piece_loc[1]),yy)
            
            possible_moves[x]=([new_loc])

            yy=yy+1
            
    return possible_moves, []
    

    
    
    
    
    

    
    
    
    
def mini_max(current_depth, max_depth, alpha, beta, max_status,inputProc,time_max):
    best_play=[]

    if current_depth >= max_depth or time_max < time.time():#BASE CASE
        #print("SOLUTION")
        return solution_value(inputProc)
        


    best_play, enemies_defeated=get_valid_move_g(inputProc.my_pieces[0],inputProc)

    
    








    
    if max_status:
        max_value = float('-Inf')
        best_moves={}#dictionary for each piece and all valid moves(all valid jumps if jump)
        
        for piece_loc in inputProc.my_pieces:
            d,enemies_defeated=get_valid_move_g(piece_loc,inputProc)
            for valid in d.values():
                best_moves.setdefault(piece_loc, []).append(valid)
        
        s=False
        for piece_loc, valid_moves in best_moves.items():

            a=abs(piece_loc[0] - valid_moves[0][0][0]) != 1 
            b=abs(piece_loc[1] - valid_moves[0][0][1]) != 1 
            if(a or b):
                s=True
                break
               
        #print(best_moves)
        #print()
        if len(best_moves):
            max_depth = 3
            
            value_first,px_first,best_play_first = max_value, (), []
            for piece_loc, valid_moves in best_moves.items():
                if(s==True):
                    a=abs(piece_loc[0] - valid_moves[0][0][0]) == 1 
                    b=abs(piece_loc[1] - valid_moves[0][0][1]) == 1 
                    
                    if(a and b):
                        continue
                
                
                for vm in valid_moves:
                        '''
                        if(type(vm)==int):
                   
                            return value_first,px_first,best_play_first
                        '''
                        end = vm[-1]
                        
                        (inputProc.my_pieces).remove(piece_loc)
                        (inputProc.my_pieces).append(end)#update new location

                        #should be 3,0 to 2,1 instead of 4,1 to 3,2


                        if(s==True):
                            for uu in enemies_defeated:
                                (inputProc.enemy_pieces).remove(uu)#update removes from jumps


                        value,px,best_play  = mini_max(current_depth+1, max_depth, alpha, beta, False,inputProc,time_max)
                        if(s==True):
                            for uu in enemies_defeated:
                                (inputProc.enemy_pieces).append(uu)


                        
                        (inputProc.my_pieces).append(piece_loc)
                        (inputProc.my_pieces).remove(end)
                        #print("MAXXXXXXXX") #(3,0) it is correct gotten next in loop from min from ned best play min then next looop is (5,2) from utility
                        #print(current_depth) #(3,0) it is correct gotten from ned best play min then next looop is (5,2) from utility
                        #print(piece_loc) #(3,0) it is correct gotten from ned best play min then next looop is (5,2) from utility
                        #print("WEHBDUREBUHERBEUHB")
                        #print(vm) #(2,1) it is correct
                        #print(value) #0
                        #print("current")
                        #print(max_value) #-inf?
                        #print(px) #-inf?
                        #print(best_play) #-inf?
                        #print(max(alpha, max_value)) #-inf?
                        #print(beta) #(2,1) it is correct
                        if value > max_value:
                            max_value = value
                            max_px=piece_loc
                            max_best_play=vm

                            alpha = max(alpha, max_value)
                            if alpha >= beta or (time_max-time.time()) < 20:
                            
                                return max_value, max_px, max_best_play
               
            return max_value, max_px, max_best_play

        
         
            
            
            
        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    
    else:






        x = InputClass() 
        x.gameName = inputProc.gameName
        x.color=inputProc.enemy_color
        x.enemy_color=inputProc.color
        x.time_remain=inputProc.time_remain
        x.my_pieces=inputProc.enemy_pieces
        x.my_kings=inputProc.enemy_kings
        x.enemy_pieces=inputProc.my_pieces
        x.enemy_kings=inputProc.my_kings
        x.game_board=inputProc.game_board

        min_value = float('Inf')
        best_moves={}#dictionary for each piece and all valid moves(all valid jumps if jump)
        
        for piece_loc in inputProc.enemy_pieces:
            d,enemies_defeated=get_valid_move_g(piece_loc,x)
            for valid in d.values():
                best_moves.setdefault(piece_loc, []).append(valid)
        
        '''
        s=False
        
        for piece_loc, valid_moves in best_moves.items():
            print(piece_loc)
            print(valid_moves)
            #if(type(valid_moves[0])==int):
                #return min_value, px, best_play
            if(len(valid_moves[0])>1):
                s=True
                break
        '''

        s=False
        for piece_loc, valid_moves in best_moves.items():

            a=abs(piece_loc[0] - valid_moves[0][0][0]) != 1 
            b=abs(piece_loc[1] - valid_moves[0][0][1]) != 1 
            if(a or b):
                s=True
                break
        












           
        #print(best_moves)#(5,4) to (4,3)
        if len(best_moves):
            for piece_loc, valid_moves in best_moves.items():
                '''
                if(s==True):
                    if(type(valid_moves[0])==int):
                        return min_value, px, best_play
                        
                    if(len(valid_moves[0])<=1):
                        continue
                '''
                if(s==True):
                    a=abs(piece_loc[0] - valid_moves[0][0][0]) == 1 
                    b=abs(piece_loc[1] - valid_moves[0][0][1]) == 1 
                    
                    if(a and b):
                        continue


                for vm in valid_moves:
                        '''
                        if(type(vm)==int):
                            return min_value, px, best_play
                        '''
                        end = vm[-1]
                        (inputProc.enemy_pieces).remove(piece_loc)
                        (inputProc.enemy_pieces).append(end)#update new location
                        if(s==True):
                            for uu in enemies_defeated:
                                (inputProc.my_pieces).remove(uu)#update removes from jumps

                        value,px,best_play  = mini_max(current_depth+1, max_depth, alpha, beta, True,inputProc,time_max)
                        if(s==True):
                            for uu in enemies_defeated:
                                (inputProc.my_pieces).append(uu)


                        (inputProc.enemy_pieces).append(piece_loc)
                        (inputProc.enemy_pieces).remove(end)
                        if value < min_value:
                            min_value = value
                            max_px=piece_loc
                            max_best_play=vm
                            
                            beta = min(beta, min_value)
                            if alpha >= beta or (time_max-time.time()) < 20:
                                #print("MINFIRST")
                                #print(current_depth)
                                return min_value, max_px, max_best_play
            #print("MINLLLLLL") 
            #print(current_depth) 
            return min_value, max_px, max_best_play
    
    
    
    
def checkMode(inputProc,time_max):#agent return 
    if inputProc.gameName=='SINGLE':
        best_play=get_valid_move_s(inputProc.my_pieces[0],inputProc)
        px=inputProc.my_pieces[0]
        
        if(best_play!=[]):
            a=abs(px[0] - (best_play[0][0])) > 1 
            b=abs(px[1] - (best_play[0][1])) > 1 
            if a or b:
                return 0,px, best_play 
        
        
        
        
        
        
        
        for piece_loc in inputProc.my_pieces:#LOOP of ALL MY PIECES
            x=get_valid_move_s(piece_loc,inputProc)
            if(x!=[]):
                a=abs(piece_loc[0] - (x[0][0])) > 1 #if jump(distance greater than 1 for x or y)
                b=abs(piece_loc[1] - (x[0][1])) > 1 
                if(best_play==[] and x!=[]):
                   best_play=x
                   px=piece_loc
                elif a or b:
                    best_play=x
                    return 0,piece_loc, best_play 
        return 0,px, best_play#return starting position and next locations
    
    
    
    
    
    
    
    
    else:
        max_depth=3

        if (inputProc.time_remain < 40) or (len(inputProc.my_pieces)>(2*len(inputProc.enemy_pieces))):
            best_play=get_valid_move_s(inputProc.my_pieces[0],inputProc)
            px=inputProc.my_pieces[0]

            if(best_play!=[]):
                a=abs(px[0] - (best_play[0][0])) > 1 
                b=abs(px[1] - (best_play[0][1])) > 1 
                if a or b:
                    return 0, px, best_play 







            for piece_loc in inputProc.my_pieces:#LOOP of ALL MY PIECES
                x=get_valid_move_s(piece_loc,inputProc)
                if(x!=[]):
                    a=abs(piece_loc[0] - (x[0][0])) > 1 #if jump(distance greater than 1 for x or y)
                    b=abs(piece_loc[1] - (x[0][1])) > 1 
                    if(best_play==[] and x!=[]):
                       best_play=x
                       px=piece_loc
                    elif a or b:
                        best_play=x
                        return 0, piece_loc, best_play 
            return 0, px, best_play#return starting position and next locations
    
        elif inputProc.time_remain < 100:
            max_depth = 2
        
        
        
        
        
        
        
        max_enemy_target = 0
        if inputProc.color == 'WHITE':
            for row in range(8):
                for col in range(8):
                    if inputProc.game_board[row][col] == 'b' or inputProc.game_board[row][col] == 'B':
                        max_enemy_target += 1
        else:
            for row in range(8):
                for col in range(8):
                    if inputProc.game_board[row][col] == 'w' or inputProc.game_board[row][col] == 'W':
                        max_enemy_target += 1

        depth = 2
        if (max_enemy_target > 10 ) and inputProc.time_remain > 100:
            max_depth = 3

        
        
        
        
        
        
        return mini_max(0,max_depth, float('-Inf'), float('Inf'), True,inputProc,time_max)#TRUE sicne starts max at root
        
        
        
       
                
            
        
            
         
        
        
    
    
        
    
def getInput(filename):
    file =  open(filename, "r")
    inputProc = InputClass()   
    lines = file.readlines() 
    
    inputProc.gameName = lines[0].replace('\n', '')
    inputProc.color = lines[1].rstrip()
    if(inputProc.color=='WHITE'):
        inputProc.enemy_color='BLACK'
    else:
        inputProc.enemy_color='WHITE'
    inputProc.time_remain=float(lines[2])
    
    
    start=8
    
  
    for y, line in enumerate(lines[3:11]):
        (inputProc.game_board).append(list(line.rstrip()))
        for x, cell in enumerate(line):
            if cell == '.':
                continue
            if(inputProc.enemy_color=='WHITE'):
                if cell == 'w' or cell == 'W':
                    (inputProc.enemy_pieces).append((x,y))#chr(97+x)+ str(start-y)
                elif cell == 'b' or cell == 'B':
                    (inputProc.my_pieces).append((x,y))
                if cell == 'W':
                    (inputProc.enemy_kings).append((x,y))  
                elif cell == 'B':
                    (inputProc.my_kings).append((x,y))
            else:
                if cell == 'w' or cell == 'W':
                    (inputProc.my_pieces).append((x,y))
                elif cell == 'b' or cell == 'B':
                    (inputProc.enemy_pieces).append((x,y))
                if cell == 'W':
                    (inputProc.my_kings).append((x,y))  
                elif cell == 'B':
                    (inputProc.enemy_kings).append((x,y))

    file.close()
    return inputProc




def main():
    
    inputProc=getInput('input.txt')

    attrs = vars(inputProc)
    start = time.time()#keep track of time 
    time_max = inputProc.time_remain + start
    #print(time_max)

    
    
    
    #Need to check if single or Game
    #get the move needed
    
    yy, piece_loc, best_play = checkMode(inputProc,time_max)
    with open("output.txt", 'w') as file:
        if(best_play!=[]):
            a=abs(piece_loc[0] - (best_play[0][0])) > 1 #if jump(distance greater than 1 for x or y)
            b=abs(piece_loc[1] - (best_play[0][1])) > 1 
            if a or b:
                jump_status = True
            else:
                jump_status = False
            for m in best_play:
                if jump_status:
                    file.write("J ")
                else:
                    file.write("E ")
                file.write("{} {}".format(chr(97+piece_loc[0])+ str(8-piece_loc[1]), chr(97+m[0])+ str(8-m[1])))#chr(97+x)+ str(start-y)
                if(m!=best_play[-1]):
                    file.write("\n")
                piece_loc = m
        '''
        print("MY TIME END:")
        print(time.time())
        print("STAR:")
        print(start)
        print(inputProc.time_remain)
        '''
        return
    
    
    
    #game: if(inputProc.color=="WHITE" and new_loc in white_edge or (inputProc.color=="BLACK" and new_loc in black_edge)):
                        #king_status=True
   
    
    
    
    

    


if __name__ == '__main__':
    main()  