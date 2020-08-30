/*
 * Filename: RMIFunctions.java
 *
 * Compile as javac RMIFunctions.java
 *
 * Copy .class file(s) to ./example/rmifunction
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
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RMIFunctions extends Remote {
    String sayHello() throws RemoteException;
    String sayGoodBye() throws RemoteException;
    int add(int a, int b) throws RemoteException;
    int openFile(String fileName) throws RemoteException;
}

