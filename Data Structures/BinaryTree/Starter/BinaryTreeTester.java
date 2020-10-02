import org.junit.*;
import static org.junit.Assert.*;
import java.util.*;	
import java.util.LinkedList;	
import java.util.ListIterator;	

/**	
 *  Title: class BinaryTreeTester	
 *  @author Lavanya Verma	
 *  @version 3.0 05-April-2015	
 *  Student ID: A15872569
 *  CSE12 Account: cse12sp20bcr
 *  Date: 20 April 2020
 *	
 *  Description: Tester file that tests the BinaryTree	
 * 
 */	

 /**
  * class with methods that tests BinaryTree
  */
public class BinaryTreeTester	
{	
	//Integer empty BinaryTree
	private BinaryTree<Integer> empty;
	//String empty BinaryTree	
    private BinaryTree<Integer>  slist ;
    LinkedList<Integer> llist ;
    @Before	
	public void setUp()	
	{	
        empty  = new BinaryTree();
        llist = new LinkedList<Integer>();
        for(int i = 1; i < 8; i++){
            llist.add(new Integer(i));
        }
        slist = new BinaryTree<>(llist);

    }	
    @Test	
	public void testConstructor(){
        assertEquals("Check element",true,slist.containsBFS(new Integer(1)));
        assertEquals("Check element",true,slist.containsBFS(new Integer(7)));	
        assertEquals("Check element",2,slist.getHeight());	
        assertEquals("Check element",7,slist.getSize());	
        assertEquals("Check element",new Integer(1),slist.minValue());
        // empty
        assertEquals("Check element",0,empty.getSize());
        assertEquals("Check element",0,empty.getHeight());		
        assertEquals("Check element",false,empty.containsBFS(new Integer(1)));
        assertEquals("Check element",null,empty.minValue());

	}

    
    
}