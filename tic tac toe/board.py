class board_class:
    
    


    def __init__(self,cp):
        self.board=[[" " for i in range(3)] for i in range(3)]
        self.current_player=cp
        self.remaining=9


    def player_switch(self):
        if self.current_player=="x":
            self.current_player="o"
        else:
            self.current_player="x"

    

       

    def mark_board(self,i,j):
        if self.board[i][j]!=" ":
            return False
        self.remaining=self.remaining-1
        self.board[i][j]=self.current_player
        self.player_switch()
        return True

    def unmark(self,i,j):
        self.remaining=self.remaining+1
        self.board[i][j]=" "
        self.player_switch()

    def win_check(self):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2] and self.board[i][0]!=" ":
                return True
            elif self.board[0][i]==self.board[1][i]==self.board[2][i]and self.board[0][i]!=" ":
                return True

        if self.board[0][0]==self.board[1][1]==self.board[2][2] and self.board[0][0]!=" ":
            return True
        elif self.board[0][2]==self.board[1][1]==self.board[2][0] and self.board[2][0]!=" ":
            return True
        
        return False
    
