import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;
import java.nio.file.Files;

import org.apache.poi.hwpf.HWPFDocument;
import org.apache.poi.hwpf.extractor.WordExtractor;
import org.apache.poi.poifs.filesystem.POIFSFileSystem;
import org.apache.poi.xwpf.extractor.XWPFWordExtractor;
import org.apache.poi.xwpf.usermodel.XWPFDocument;

import com.itextpdf.text.pdf.PdfReader;
import com.itextpdf.text.pdf.parser.PdfReaderContentParser;
import com.itextpdf.text.pdf.parser.SimpleTextExtractionStrategy;
import com.itextpdf.text.pdf.parser.TextExtractionStrategy;


public class Test 
{
	 public static final String PREFACE = "/home/rishi/Desktop/abc.docx";
	 public static final String RESULT = "/home/rishi/Desktop/hello.txt";
	
	
public static void main(String []args) throws IOException
{
	 File file = new File(PREFACE);
	 String fileType = Files.probeContentType(file.toPath());
	 System.out.println(fileType);
	
       	 switch(fileType)
	 {
	  case "application/pdf" : new Test().parsePdf(PREFACE, RESULT);
	                         break;
	  case "application/msword" : parseDoc();
	                            break;
	  case "application/vnd.openxmlformats-officedocument.wordprocessingml.document" : parseDocx();
	                                                                                 break;
	 }
}	

public void parsePdf(String pdf, String txt) throws IOException 
{
    PdfReader reader = new PdfReader(pdf);
    PdfReaderContentParser parser = new PdfReaderContentParser(reader);
    PrintWriter out = new PrintWriter(new FileOutputStream(txt));
    TextExtractionStrategy strategy;
    for (int i = 1; i <= reader.getNumberOfPages(); i++) {
        strategy = parser.processContent(i, new SimpleTextExtractionStrategy());
        out.println(strategy.getResultantText());
    }
    File file = new File("/home/rishi/Downloads/sweetjs.pdf");
    String fileType = Files.probeContentType(file.toPath());
    out.flush();
    out.close();
    reader.close();
}
public static void parseDoc()
{
               	 POIFSFileSystem fs = null;
        try {
		 fs = new POIFSFileSystem(new FileInputStream(PREFACE));
		 File file = new File("/home/rishi/Desktop/_Contents.doc");
	         String fileType = Files.probeContentType(file.toPath());
	         HWPFDocument doc = new HWPFDocument(fs);
		 WordExtractor we = new WordExtractor(doc);
		 String text = we.getText();
	     File fil = new File("/home/rishi/Desktop/hello.txt");
		 Writer output = new BufferedWriter(new FileWriter(fil));
		 output.write(text);
		 output.close();
	} catch (Exception exep) {
		 System.out.println(exep);
	}
}

public static void parseDocx(){
	
	File file = null;
    try {
		file = new File(PREFACE);
		String fileType = Files.probeContentType(file.toPath());
		FileInputStream fis = new FileInputStream(file);
		XWPFDocument doc = new XWPFDocument(fis);
		XWPFWordExtractor ex = new XWPFWordExtractor(doc);
		String text = ex.getText();
	        File fil = new File("/home/rishi/Desktop/hello.txt");
	        Writer output = new BufferedWriter(new FileWriter(fil));
	        output.write(text);
	        output.close();
	    } catch (Exception exep) {
		System.out.println(exep);
	    }
    }
}
