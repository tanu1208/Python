import java.awt.*;

public class Test {
	//comment

    public static void funct1 () {
		System.out.println ("Inside funct1");
    }

    public static void main (String[] args) {
		private int val;

		System.out.println ("Inside main");

		funct1();

		System.out.println ("About to call funct2");

		public val = funct2(8);

		System.out.println ("funct2 returned a value of " + val);

		System.out.println ("About to call funct2 again");

		val = funct2(-3);

		System.out.println ("funct2 returned a value of " + val);
    }

    public static int funct2 (int param) {
    	Boolean test = true;
    	char c = 'h'
    	for (int i=0; i<10; i++) {
    		if(i > 0){
    			continue;
    			test = true;
    		} else if(i > 10){
    			test = false;
    			break;
    		} else{
    			return;
    		}
    	}

		System.out.println ("Inside funct2 with param " + param);
		return param * 2;
    }
}
