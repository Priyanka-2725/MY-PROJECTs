import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class PongGame extends JPanel implements KeyListener, ActionListener {
    private boolean play = false;
    private int score = 0;

    private Timer timer;
    private int delay = 8;  // Initial delay for slower ball movement

    // Paddle variables
    private int playerX = 310; // Starting position

    // Ball variables
    private int ballPosX = 120;
    private int ballPosY = 350;
    private int ballXDir = -1; // Start slow
    private int ballYDir = -2; // Start slow

    public PongGame() {
        addKeyListener(this);
        setFocusable(true);
        setFocusTraversalKeysEnabled(false);
        timer = new Timer(delay, this);
        timer.start();
    }

    // Drawing the game
    public void paint(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;

        // Smooth rendering
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Background color
        g2d.setColor(Color.BLACK);
        g2d.fillRect(0, 0, getWidth(), getHeight());

        // Borders
        g2d.setColor(Color.YELLOW); // Solid yellow
        g2d.setStroke(new BasicStroke(5));
        g2d.drawRect(5, 5, getWidth() - 10, getHeight() - 10); // Border

        // Paddle
        g2d.setColor(Color.GREEN); // Solid green
        g2d.fillRect(playerX, getHeight() - 50, 100, 8);
        
        // Paddle shadow
        g2d.setColor(new Color(0, 0, 0, 80)); // Shadow
        g2d.fillRect(playerX + 5, getHeight() - 45, 100, 8);

        // Ball
        g2d.setColor(Color.YELLOW); // Solid yellow
        g2d.fillOval(ballPosX, ballPosY, 20, 20);
        
        // Ball shadow
        g2d.setColor(new Color(0, 0, 0, 50)); // Ball shadow
        g2d.fillOval(ballPosX + 3, ballPosY + 3, 20, 20);

        // Score
        g2d.setFont(new Font("Serif", Font.BOLD, 25));
        g2d.setColor(Color.WHITE);
        g2d.drawString("Score: " + score, getWidth() - 150, 30);

        // Game Over
        if (ballPosY > getHeight() - 30) {
            play = false;
            ballXDir = 0;
            ballYDir = 0;
            g2d.setColor(Color.RED);
            g2d.setFont(new Font("Serif", Font.BOLD, 30));
            g2d.drawString("Game Over, Score: " + score, getWidth() / 2 - 150, getHeight() / 2);

            g2d.setFont(new Font("Serif", Font.BOLD, 20));
            g2d.drawString("Press Enter to Restart", getWidth() / 2 - 120, getHeight() / 2 + 50);
        }

        g.dispose();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        timer.start();

        if (play) {
            // Ball and paddle interaction
            if (new Rectangle(ballPosX, ballPosY, 20, 20).intersects(new Rectangle(playerX, getHeight() - 50, 100, 8))) {
                ballYDir = -ballYDir;
                score += 5;

                // Gradually increase ball speed
                if (ballXDir > 0) {
                    ballXDir++; // Increase speed to the right
                } else {
                    ballXDir--; // Increase speed to the left
                }

                if (ballYDir > 0) {
                    ballYDir++; // Increase speed downward
                } else {
                    ballYDir--; // Increase speed upward
                }
            }

            ballPosX += ballXDir;
            ballPosY += ballYDir;

            // Left wall
            if (ballPosX < 0) {
                ballXDir = -ballXDir;
            }
            // Top wall
            if (ballPosY < 0) {
                ballYDir = -ballYDir;
            }
            // Right wall
            if (ballPosX > getWidth() - 20) {
                ballXDir = -ballXDir;
            }
        }

        repaint();
    }

    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
            if (playerX >= getWidth() - 100) {
                playerX = getWidth() - 100;
            } else {
                moveRight();
            }
        }

        if (e.getKeyCode() == KeyEvent.VK_LEFT) {
            if (playerX < 10) {
                playerX = 10;
            } else {
                moveLeft();
            }
        }

        if (e.getKeyCode() == KeyEvent.VK_ENTER) {
            if (!play) {
                play = true;
                ballPosX = 120;
                ballPosY = 350;
                ballXDir = -1; // Reset speed to initial
                ballYDir = -2; // Reset speed to initial
                playerX = getWidth() / 2 - 50;
                score = 0;
                repaint();
            }
        }
    }

    public void moveRight() {
        play = true;
        playerX += 20;
    }

    public void moveLeft() {
        play = true;
        playerX -= 20;
    }

    @Override
    public void keyReleased(KeyEvent e) {}

    @Override
    public void keyTyped(KeyEvent e) {}

    public static void main(String[] args) {
        JFrame frame = new JFrame();
        PongGame game = new PongGame();

        // Set window to fullscreen, but keep title bar and buttons
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        frame.setSize(screenSize.width, screenSize.height);
        frame.setTitle("Pong Game");
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(game);
        frame.setVisible(true);
        game.requestFocus();
    }
}
