public class Schedule
{
   private int start;
   private String Depart;
   private String Arrive;

   public Schedule(int i, String depart, String arrive)
   {
      System.out.println("Class Schedule");
         start = i;
         Depart = depart;
         Arrive = arrive;
   }

   public int getStart()
   {
      return start;
   }

   public String getDepart()
   {
      return Depart;
   }

   public String getArrive()
   {
      return Arrive;
   }
}