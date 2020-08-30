/*
* FlightTest.java
*/
import java.util.*;
import java.io.*;

public class FlightTest
{
   public static void main(String[] args)
   {
      Schedule schedule = new Schedule(1000, "LIH", "HNL");
      Flight   flight   = new Flight(    25, "LIH", "HNL");

      System.out.println("Depart: " + schedule.getDepart() + " " +
                         "Arrive: " + schedule.getArrive()  + " " +
                         "Time  : " + schedule.getStart());

      flight.setProcedure("Normal Flight");
      System.out.println("Depart: " + schedule.getDepart() + " " +
                         "Arrive: " + schedule.getArrive()  + " " +
                         "Time  : " + flight.getStart()   + " " +
                         "Special: " + flight.getProcedure()); 
   }

}