import java.awt.BorderLayout;
import java.io.File;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import uk.co.caprica.vlcj.component.EmbeddedMediaPlayerComponent;
import uk.co.caprica.vlcj.player.MediaPlayerFactory;
import uk.co.caprica.vlcj.player.embedded.EmbeddedMediaPlayer;

public class ReverseVideoPlayer {

    private final JFrame frame;
    private final EmbeddedMediaPlayerComponent mediaPlayerComponent;
    private final EmbeddedMediaPlayer mediaPlayer;

    public ReverseVideoPlayer(String videoPath, float playbackRate) {
        frame = new JFrame("Reverse Video Player");
        mediaPlayerComponent = new EmbeddedMediaPlayerComponent();
        mediaPlayer = mediaPlayerComponent.getMediaPlayer();

        frame.setLayout(new BorderLayout());
        frame.add(mediaPlayerComponent, BorderLayout.CENTER);
        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        mediaPlayer.setRate(playbackRate);
        mediaPlayer.playMedia(videoPath);
        mediaPlayer.setTime(mediaPlayer.getLength());
        mediaPlayer.setRate(-playbackRate);
    }

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java ReverseVideoPlayer <video-file-path> <playback-rate>");
            System.exit(1);
        }

        String videoPath = args[0];
        float playbackRate = Float.parseFloat(args[1]);

        SwingUtilities.invokeLater(() -> new ReverseVideoPlayer(videoPath, playbackRate));
    }
}