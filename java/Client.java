/*
 * Filename: Client.java
 *
 * Description:
 *
 * Compile as javac Client.java
 *
 * Copy .class file(s) to ./example/hello
 *
 * Run as java -cp $CLASSPATH -Djava.rmi.server.codebase=file:$CLASSPATH/ example.rmifunctions.Client
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
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;


public class Client {

    private Client() {}

    public static void main(String[] args) {

        String host = (args.length < 1) ? null : args[0];
        try {
            Registry registry = LocateRegistry.getRegistry(host);
            //Registry registry = LocateRegistry.getRegistry("192.168.1.70");
            RMIFunctions stub = (RMIFunctions) registry.lookup("RMIFunctions");
            String response = stub.sayHello();
            System.out.println("response: " + response);

            response = stub.sayGoodBye();
            System.out.println("response: " + response);

            response = stub.sayHello();
            System.out.println("response: " + response);

            int result=stub.add(2,10);
            System.out.println("result: " + result);

            result=stub.openFile("/tmp/frank.txt");
            System.out.println("result: " + result);

            Thread.sleep(1000);


        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}

