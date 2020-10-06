import java.sql.*;
public class DML extends DBCON
{
    void insert()
    {
        try
        {
            java.util.Scanner sc = new java.util.Scanner(System.in);
            System.out.println("Enter Id");
            int id=sc.nextInt();
            System.out.println("Enter name");
            String name=sc.next();
            System.out.println("Enter course");
            String course=sc.next();
            System.out.println("Enter year");
            int year=sc.nextInt();
            String insertQuery="insert into student values(?,?,?,?);";
            PreparedStatement pst=con.prepareStatement(insertQuery);
            pst.setInt(1,id);
            pst.setString(2,name);
            pst.setString(3,course);
            pst.setInt(4,year);

            pst.executeUpdate();

            System.out.println("data inserted...");

        }
        catch(Exception e)
        {
            System.out.println("data not inserted..."+e);
        }

    }
    void view()
    {
        try
        {
            String viewquery= "select * from student";

            Statement stmt= con.createStatement();

            ResultSet rs = stmt.executeQuery(viewquery);

            while(rs.next())
            {
                System.out.print(" "+rs.getInt(1));
                System.out.print(" "+rs.getString(2));
                System.out.print(" "+rs.getString(3));
                System.out.print(" "+rs.getInt(4));

                System.out.print("\n");
            }

            System.out.println("data found...");

        }
        catch(Exception e)
        {
            System.out.println("data not found..."+e);
        }


    }
    void delete()
    {
        try
        {
            int id=03;
            String delquery="delete from student where sid="+id;
            PreparedStatement pst2=con.prepareStatement(delquery);
            pst2.executeUpdate();

            System.out.println("data delete ...");

        }
        catch(Exception e)
        {
            System.out.println("data not delete..."+e);
        }


    }
    void update()
    {
        try
        {
            System.out.println("data update...");

        }
        catch(Exception e)
        {
            System.out.println("data not update..."+e);
        }


    }
    public static void main(String args[])
    {
        DML obj= new DML();
        obj.insert();
        obj.view();
        obj.delete();

    }
}