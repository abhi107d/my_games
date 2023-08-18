class human_player:

    def play(self,board,x,y):
    
        self.x=x
        self.y=y
        if not board.mark_board(self.x,self.y):
            return False
        return True
        
