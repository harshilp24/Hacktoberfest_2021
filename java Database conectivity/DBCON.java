import java.sql.*;
public class DBCON {

    Connection con;
    DBCON()
    {
        try
        {
            Class.forName("com.mysql.jdbc.Driver");

            String ConnectionURL="jdbc:mysql://localhost:3306/GLADB";

            con = DriverManager.getConnection(ConnectionURL,"root","2744");
            System.out.println("Connection sucess");
        }
        catch(Exception e)
        {
            System.out.println("Connection fail"+e);
        }
    }
    public static void main(String args[])
    {
        DBCON obj = new DBCON();
    }
}



