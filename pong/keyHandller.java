import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
public class keyHandller implements KeyListener{
    boolean u1=false;
    boolean d1=false;
    boolean u2=false;
    boolean d2=false;
    boolean reset=false;

    @Override
    public void keyTyped(KeyEvent e) {
        
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int code=e.getKeyCode();
        switch (code) {
            case KeyEvent.VK_W:
                u1=true;
                break;
            case KeyEvent.VK_S:
                d1=true;
                break;
            case KeyEvent.VK_UP:
                u2=true;
                break;
            case KeyEvent.VK_DOWN:
                d2=true;
                break;
            case KeyEvent.VK_R:
                reset=true;
                break;
            default:
                break;
        }
        
    }

    @Override
    public void keyReleased(KeyEvent e) {
        int code=e.getKeyCode();
        switch (code) {
            case KeyEvent.VK_W:
                u1=false;
                break;
            case KeyEvent.VK_S:
                d1=false;
                break;
            case KeyEvent.VK_UP:
                u2=false;
                break;
            case KeyEvent.VK_DOWN:
                d2=false;
                break;
            case KeyEvent.VK_R:
                reset=false;
                break;
            default:
                break;
        }

       
    }
    
}
