class X{
 public void x(){
 System.out.print("x is ruuning");
} }
class Y extends X{
 public  void y(){
System.out.print("y is running");
}}
   class inheritance
{
 public static void main( String []args)
{
 Y obj= new Y();
obj.x();
}
}