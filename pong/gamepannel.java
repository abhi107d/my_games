import java.awt.*;
import java.util.Random;

import javax.swing.*;
public class gamepannel extends JPanel implements Runnable{
    final int ts=20;
    Random r=new Random();
    Thread gameThread;
    int p1=0;
    int p2=0;
    keyHandller kl=new keyHandller();
    int batspeed=ts;
    int pongspeedx=10;
    int pongspeedy=0;
    int b1p=(13)*ts;
    int b2p=(13)*ts;
    int py=600/2;
    int px=1000/2;
    boolean gameover=false;
    gamepannel(){
        this.setPreferredSize(new Dimension(1000, 650));
        this.setBackground(Color.black);
        this.addKeyListener(kl);

        this.setFocusable(true);
    }
    public void game_Thread(){
        gameThread=new Thread(this);
        gameThread.start();

    }
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        //bat 1
        g2d.setColor(Color.orange);
	    g2d.fillRect(0, b1p,ts , 5*ts);
        //bat 2
        g2d.setColor(Color.blue);
        g2d.fillRect(1000-(ts), b2p,ts , 5*ts);
        //pong
        g2d.setColor(Color.pink);
        g2d.fillRect(px, py, 10, 10);

        //bottom line
        g2d.setColor(Color.white);
        g2d.setStroke(new BasicStroke(2));
        g2d.drawLine(0, 600, 1000, 600);
        
        //middle line
        g2d.setColor(Color.white);
        Stroke dashed = new BasicStroke(3, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0, new float[]{9}, 0);
        g2d.setStroke(dashed);
        g2d.drawLine(500, 0, 500, 650);

        //player1 score
        g2d.setFont(g.getFont().deriveFont(30f));
        g2d.drawString(String.valueOf(p2), 700, 640);

        //player2 score
        g2d.drawString(String.valueOf(p1), 200, 640);

        //gameover
        if(gameover){
            
            if(p1==10){
                g2d.setColor(Color.YELLOW);
                g2d.drawString("Game Over", 400, 300);
                g2d.drawString("Player 1 wins", 390, 350);


            }
            else{
                g2d.setColor(Color.BLUE);
                g2d.drawString("Game Over", 400, 300);
                g2d.drawString("Player 2 wins", 390, 350);
            }
        }


        g2d.dispose();

    }
    
    public void update(){

        //human controll
        //--player 1 yellow
        if(kl.u1==true && b1p!=0){
            b1p=b1p-batspeed;

        }
        if(kl.d1==true && b1p<600-(5*ts)){
            b1p=b1p+batspeed;
 
        }
         //--player2 blue
        if(kl.u2==true && b2p!=0){
            b2p=b2p-batspeed;

        }
        if(kl.d2==true && b2p<600-(5*ts)){
            b2p=b2p+batspeed;
 
        }

        //pong collition
        int dr=0;
        px=pongspeedx+px;
        py=pongspeedy+py;
        if(px==1000-2*ts && py>=b2p && py<=b2p+5*ts)pongspeedx=pongspeedx*-1;
        if(px==ts && py>=b1p && py<=b1p+5*ts)pongspeedx=pongspeedx*-1;
        if(py<=0)pongspeedy=pongspeedy*-1;
        if(py>=600-ts)pongspeedy=pongspeedy*-1;

        //pong bat direction
        for(int i=0;i<10;i++){
            
            dr=r.nextInt(2);
            if(dr==0)dr--;
            if(b1p+i*10<=py && b1p+(i+1)*10>=py  && px==ts){
                 pongspeedy=(1+i)*dr;
            }
       
            if(b2p+i*10<=py && b2p+(i+1)*10>=py && px==1000-2*ts){
                pongspeedy=(1+i)*dr;

            } 
        }


        //point count
        int R=r.nextInt(5);
        if(px>1000){
            p1++;
            py=600/2;
            px=1000/2;
            pongspeedy=dr*R;
            
        }
        if(px<0){
            p2++;
            py=600/2;
            px=1000/2;
            pongspeedy=dr*R;
        }
        if(p1==10|| p2==10){
            gameover=true;
        }

        
        


    }
    private void reset() {
        gameover=false;
        p1=0;
        p2=0;

    }


    @Override
    public void run() {
        long rt;
        long ct=System.nanoTime();
        long rate=1000000000/60;
        while(gameThread!=null){

            //update values
            if(!gameover)update();
            else if(kl.reset){
                reset();
            }

            //repaint components
            repaint();


            //Frame rate
            rt=System.nanoTime()-ct;
            if(rt<rate){
                try {
                    Thread.sleep((rate-rt)/1000000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            ct=System.nanoTime();


        }
        
    }
    
    
}
