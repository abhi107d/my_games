import pygame as p
from moving_bar import move_bar
from bird import bird
from sys import exit
from naturalselection import natural_selection



def rungame():
    max=0
    
    p.init()
    screen=p.display.set_mode((700,400))
    p.display.set_caption("Flappy bird")
    
    bir=bird(screen,140,400,10,0.3,6,[0,1])
    mb=move_bar(screen,20)
    frame=0
    clock=p.time.Clock()

    generations=natural_selection(screen,mb)


    




    while True:
        
        screen.fill((0,0,0))
        for e in p.event.get(): 
            if e.type==p.QUIT:  
                p.quit()
                exit()
            if e.type == p.KEYUP:
                bir.event=True   



        if frame%100==0:
            mb.put(700,400)
        
        
        
        score=generations.draw_geneoms()
        if max<score:
            max=score



        
        bir.draw()
        bir.update_evnt()
        mb.animate(3)
        frame+=1


        font = p.font.Font(None, 30)
        text_surface = font.render(f"max : {max}", True, "white")
        text_rect = text_surface.get_rect()
        text_rect.topleft = (500, 20)
        screen.blit(text_surface, text_rect)


        font = p.font.Font(None, 30)
        text_surface = font.render(f"curr: {score}", True, "white")
        text_rect = text_surface.get_rect()
        text_rect.topleft = (600, 20)
        screen.blit(text_surface, text_rect)

        
        p.display.update()      
        clock.tick(60)


rungame()