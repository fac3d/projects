import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ApolloLander extends JFrame {

    private LanderPanel landerPanel;
    private JButton thrustButton, resetButton;
    private Timer timer;
    private final int DELAY = 100; // update every 100 milliseconds

    public ApolloLander() {
        setTitle("Apollo Lander Simulation");
        setSize(400, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        landerPanel = new LanderPanel();
        add(landerPanel, BorderLayout.CENTER);

        JPanel controlPanel = new JPanel();
        thrustButton = new JButton("Thrust");
        resetButton = new JButton("Reset");

        thrustButton.addActionListener(new ThrustAction());
        resetButton.addActionListener(new ResetAction());

        controlPanel.add(thrustButton);
        controlPanel.add(resetButton);
        add(controlPanel, BorderLayout.SOUTH);

        timer = new Timer(DELAY, new TimerAction());
        timer.start();
    }

    private class ThrustAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            landerPanel.applyThrust();
        }
    }

    private class ResetAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            landerPanel.resetLander();
        }
    }

    private class TimerAction implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            landerPanel.update();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            ApolloLander frame = new ApolloLander();
            frame.setVisible(true);
        });
    }
}

class Lander {
    private double altitude;
    private double velocity;
    private double fuel;

    private static final double GRAVITY = 1.6;
    private static final double THRUST = 5.0;
    private static final double FUEL_CONSUMPTION = 0.1;

    public Lander() {
        reset();
    }

    public void reset() {
        altitude = 1000; // starting altitude in meters
        velocity = 0;
        fuel = 100; // starting fuel in units
    }

    public void applyThrust() {
        if (fuel > 0) {
            velocity -= THRUST;
            fuel -= FUEL_CONSUMPTION;
        }
    }

    public void update() {
        velocity += GRAVITY;
        altitude -= velocity;

        if (altitude < 0) {
            altitude = 0;
            velocity = 0;
        }
    }

    public double getAltitude() {
        return altitude;
    }

    public double getVelocity() {
        return velocity;
    }

    public double getFuel() {
        return fuel;
    }
}

class LanderPanel extends JPanel {
    private Lander lander;

    public LanderPanel() {
        lander = new Lander();
        setPreferredSize(new Dimension(400, 500));
        setBackground(Color.BLACK);
    }

    public void applyThrust() {
        lander.applyThrust();
    }

    public void resetLander() {
        lander.reset();
    }

    public void update() {
        lander.update();
        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Draw lander
        int landerHeight = 20;
        int landerWidth = 10;
        int x = getWidth() / 2 - landerWidth / 2;
        int y = getHeight() - (int) lander.getAltitude() - landerHeight;

        g.setColor(Color.WHITE);
        g.fillRect(x, y, landerWidth, landerHeight);

        // Draw altitude, velocity, and fuel
        g.drawString("Altitude: " + (int) lander.getAltitude() + " m", 10, 20);
        g.drawString("Velocity: " + String.format("%.2f", lander.getVelocity()) + " m/s", 10, 40);
        g.drawString("Fuel: " + String.format("%.2f", lander.getFuel()) + " units", 10, 60);
    }
}
