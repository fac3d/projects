/*
* Filename: FileReceiver.java
*
*
*
*/

}import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;


public class FileReceiver {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(6000)) {
            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     DataInputStream in = new DataInputStream(clientSocket.getInputStream());
                     PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

                    // Read the file name and size
                    String fileName = in.readUTF();
                    long fileSize = in.readLong();

                    // Receive the file contents
                    FileOutputStream fileOutputStream = new FileOutputStream("received_" + fileName);
                    byte[] buffer = new byte[4096];
                    long bytesRead = 0;
                    while (bytesRead < fileSize) {
                        int read = in.read(buffer);
                        fileOutputStream.write(buffer, 0, read);
                        bytesRead += read;
                    }
                    fileOutputStream.close();

                    // Send a reply
                    out.println("success");

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
