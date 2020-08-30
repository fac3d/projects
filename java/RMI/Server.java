/*
 * Filename: Server.java
 *
 * Description:
 *
 * Compile as javac Server.java
 *
 * Copy .class file(s) to ./example/hello
 *
 * Run as java -cp $CLASSPATH -Djava.rmi.server.codebase=file:$CLASSPATH/ example.rmifunctions.Server
 *
 * Cloned from example on Oracles website.
 *
 * Author: Frank Cermak
 *
 * Date: 2020-01-26
 *
 * Revisions:
 *
 */
package example.rmifunctions;
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.io.*;

public class Server implements RMIFunctions {

    public Server() {}

    public String sayHello() {
        return "Hello, World!";
    }
    public String sayGoodBye() {
        return "Good Bye!";
    }
    public int add(int a, int b) {
        return (a+b);              
    }

    public int openFile(String fileName) {
        try 
        {
           PrintWriter writer = new PrintWriter(fileName, "UTF-8");
           writer.println("The first line");
           writer.println("The second line");
           writer.close();
        } 
        catch (IOException ex) 
        {

        }
        return (0);
    }

    public static void main(String args[]) {

        try {
            Server obj = new Server();
            RMIFunctions stub = (RMIFunctions) UnicastRemoteObject.exportObject(obj, 0);
            Registry registry = LocateRegistry.getRegistry();
            registry.bind("RMIFunctions", stub);

            System.err.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
