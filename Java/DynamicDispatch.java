class Base 
{ 
    void func() 
    { 
        System.out.println("Inside Base's func method"); 
    } 
} 
  
class Child1 extends Base 
{ 
    
    void func() 
    { 
        System.out.println("Inside Child1's func method"); 
    } 
} 
  
class Child2 extends Child1 
{ 
    
    void func() 
    { 
        System.out.println("Inside Child2's func method"); 
    } 
} 
  

class DynamicDispatch 
{ 
    public static void main(String args[]) 
    { 
        Base b = new Base(); 
        Child1 c1 = new Child1(); 
		Child2 c2 = new Child2(); 
		Base ref; 
        ref = b; 
		ref.func(); 
		ref = c1; 
		ref.func(); 
        ref = c2; 
        ref.func(); 
    } 
} 