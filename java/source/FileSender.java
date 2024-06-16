/*
* Filename: FileSender.java
*
*
*/
import java.io.*;
import java.net.Socket;

public class FileSender {
    public static void main(String[] args) {
        while (true) {
            try {
                // Connect to the socket on port 6000
                Socket socket = new Socket("localhost", 6000);
                DataOutputStream out = new DataOutputStream(socket.getOutputStream());
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

                // Open a text file
                File file = new File("path/to/your/file.txt");
                String fileName = file.getName();
                long fileSize = file.length();

                // Send the file name and size to the server
                out.writeUTF(fileName);
                out.writeLong(fileSize);

                // Read the file contents and send it to the server
                FileInputStream fileInputStream = new FileInputStream(file);
                byte[] buffer = new byte[4096];
                int bytesRead;
                while ((bytesRead = fileInputStream.read(buffer)) != -1) {
                    out.write(buffer, 0, bytesRead);
                }
                fileInputStream.close();

                // Wait for a reply from the server
                String response = in.readLine();
                if ("success".equalsIgnoreCase(response)) {
                    System.out.println("Success");
                } else {
                    System.out.println("Failure");
                }

                // Close the socket
                socket.close();

                // Wait for a few seconds before repeating (optional)
                Thread.sleep(5000); // Adjust the sleep time as needed

            } catch (IOException | InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}