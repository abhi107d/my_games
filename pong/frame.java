import javax.swing.*;
public class frame extends JFrame{
    frame(){
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        gamepannel gp=new gamepannel();
        gp.game_Thread();
        this.add(gp);
        this.setResizable(false);
        this.pack();
        this.setVisible(true);
        
    }

    
}
