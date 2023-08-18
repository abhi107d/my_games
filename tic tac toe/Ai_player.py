import copy

class ai_player:

    def print_board(delf,board):
        for i in board.board:
            for j in i:
                print(j, end='|')
            print("\n-------")

 

    def ai(self,board):
        min=[100,0,0]
        max=[-100,0,0]
        cp=board.current_player
        for i in range(3):
            for j in range(3):
                if board.board[i][j]==" ":

                    board.mark_board(i,j)
                    if board.remaining==0 and not board.win_check():  #get tie first no black space and no winss
                        board.unmark(i,j)
                        return [0,i,j]
            
                    elif board.win_check():  #check is win condition occurs
                        if cp==self.max:     #if winner is max
                            board.unmark(i,j)
                            return [board.remaining,i,j]
                        else:                  #if wwinner is min
                            board.unmark(i,j)
                            return [-1*(board.remaining),i,j]
                    
                    else:
                        rt=self.ai(board)
                        if cp==self.max:
                            if rt[0]>max[0]:
                                max[0]=rt[0]
                                max[1]=i
                                max[2]=j
                        else:
                            if rt[0]<min[0]:
                                min[0]=rt[0]
                                min[1]=i
                                min[2]=j
                    board.unmark(i,j)

        if board.current_player==self.max:
            return max                    
        else:
            return min
                    

    

    def play(self,boardd):
        self.max=boardd.current_player
        self.pos=self.ai(copy.deepcopy(boardd))
        boardd.mark_board(self.pos[1],self.pos[2])
             