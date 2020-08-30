public class Flight extends Support
{
   private int start;
   private String procedure;

   public Flight(int i, String depart, String arrive)
   {
      super(i, depart, arrive);
      start = i + 1000;
      System.out.println("Class Flight");
   }

   public int getStart()
   {
      return start;
   }

   public String getProcedure()
   {
      return procedure;
   }

   public String setProcedure(String s)
   {
      procedure = s;
      return procedure;
   }
   
}