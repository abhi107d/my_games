
from board import board_class
from human_playerfu import human_player
from Ai_player import ai_player
import random
import tkinter as tk

firstp=random.choice(("x","o"))
print(f"FIRST PLAYER IS {firstp}") 
board=board_class(firstp) # --> inizalisating board
ai=ai_player()
hp=human_player()




def gameover():
        if board.remaining==0:
       
            canvas.create_text(150, 350, text="Its a Tiee!!!", fill="green", font=('Helvetica 15 bold'))             
             
    
        else:
            if board.current_player=="x":
                canvas.create_text(150, 350, text="O wins!!!", fill="red", font=('Helvetica 15 bold'))   
            else:
                canvas.create_text(150, 350, text="X wins!!!", fill="blue", font=('Helvetica 15 bold'))   

# redraw
def draw():  
    for i in range(0,3):
        for j in range(0,3):
            if(board.board[i][j]=='o'):
                canvas.create_oval((100*j)+10,(100*i)+10,100*(j+1)-10,100*(i+1)-10,outline="red",width=3)

            elif board.board[i][j]=='x':
                canvas.create_line((100*j)+10,(100*i)+10,100*(j+1)-10,100*(i+1)-10,fill="blue",width=3)
                canvas.create_line(100*(j+1)-10,(100*i)+10,(100*j)+10,100*(i+1)-10,fill="blue",width=3)

        for i in range(3):
            if board.board[i][0]==board.board[i][1]==board.board[i][2] and board.board[i][0]!=" ":
                canvas.create_line(0,(i*100)+50,300,(i*100)+50,width=3,fill="green")
            elif board.board[0][i]==board.board[1][i]==board.board[2][i]and board.board[0][i]!=" ":
                canvas.create_line((i*100)+50,0,(i*100)+50,300,width=3,fill="green")

        if board.board[0][0]==board.board[1][1]==board.board[2][2] and board.board[0][0]!=" ":
            canvas.create_line(0,0,300,300,width=3,fill="green")
            
        elif board.board[0][2]==board.board[1][1]==board.board[2][0] and board.board[2][0]!=" ":
            canvas.create_line(0,300,300,0,width=3,fill="green")
            
        
##########################################
         


def main2(event):
    if board.win_check():
        return
    position=False
    for i in range(0,3):
        for j in range(0,3):
            if event.x>j*100 and event.x<(j+1)*100 and event.y>i*100 and event.y<(i+1)*100:
                x=i   # to get the mouse click position
                y=j
                position=True
    if not position:
        return            
    if not hp.play(board,x,y):
        return     
    if board.win_check() or board.remaining==0:
        gameover()
    ai.play(board)
    if board.win_check() or board.remaining==0:
        gameover()
    draw()



win=tk.Tk()
win.geometry("400x400")


#inizilizing canvas
canvas=tk.Canvas(win,bg="white",height=400,width=300)
canvas.pack()

#drawing board
for i in range (1,3):
    canvas.create_line((i*100),0,(i*100),300,width=3,fill="grey")
    canvas.create_line(0,(i*100),300,(i*100),width=3,fill="grey")




#binding click action
canvas.bind("<Button-1>",main2)
win.mainloop()



