package javatutor;

public class javaproject {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//single line comment
				System.out.println("Hello world"); 
				/*multi-line
				  comment
				 */
				
				/*variables
				water-bucket
				lunch-lunchbox
				
				In Java: 
				Variables are containers which stores data variables
				String- array of character , 
				int- real numbers like 1, 2, 3, 4, 
				float- numbers with pointers 1.2, 3.5, 4.2, 
				char- characters like a, b, c, d, 
				boolean- yes or no
				
				How to declare variables?
				syntax- <dataType> <variableName> = <value>;
		 		*/
				String name = "Java";	// duplicate variable don't allowed
				System.out.println(name);
				int a = 45, x=34, y=65;
			    float b = 45.22f;
			    boolean isAdult = false;
			    System.out.println(b);
			    System.out.println(isAdult);
			    
			    /* Rules for constructing name of variables in java
			     1. Can contain digits, underscores, dollar signs, letters
			     2. Should begin with letter, $ or _
			     3. Java is case sensitive language which means that 
			        java and Java are two different variables altogether
			     4. Should not contains white spaces
			     5. You cannot use reserved keywords from Java like String/int/boolean/float
			     */
			    
			    /* Two types of Java Datatypes:
			      1. Primitive - byte(8-bit), short(16-bit), int(32-bit), long(64-bit), 
			                     float(32-bit), double(64-bit), boolean(1-bit), char(16-bit)
			      2. Non Primitive or Reference Data Types - 
			     */
			    
//			    byte u = 56;//range from -127 to 127
//			    double d = 45.3435463;//range from 
//			    char grade = 'A';// single quote for char and double quote for string
//			    System.out.println(u);
//			    System.out.println(d);
//			    System.out.println(grade);
//			    
//			    /* Operators in Java
//			    
//			    Operand, operator, Operand	=	Result
//			    4			+			7  	= 	11
//			    
//			    Types of operators in Java
//			    Arithmatic Operators
//			    Assignment Operators
//			    Logical Operators
//			    Comparison Operators
//			    */
//			    
//			    /*Assignment operator :
//		    	1. normal assignment =
//		    	2. increment and assignment +=
//		    	3. decrement and assignment -=
//		    	4. multiple and assignment *=
//		    	5. divide and assignment /=
//		    	6. modulo and assignment %=
//		    */
//			    int num1 = 34, num2 = 43;
//			    System.out.print("The value of num1 + num2: ");
//			    System.out.println(num1 + num2);
//			    System.out.print("The value of num1 - num2: ");
//			    System.out.println(num1 - num2);
//			    System.out.print("The value of num1 / num2: ");
//			    System.out.println(num1 / num2);
//			    System.out.print("The value of num1 % num2: ");
//			    System.out.println(num1 % num2);
//			   
//			    System.out.println(num1++);		// first print num1 then increment by 1
//			    System.out.println(++num1);		// first increment by 1 then print num1
//			   
//			    System.out.println(num1--);		// first print num1 then decrement by 1
//			    System.out.println(--num1);		// first decrement by 1 then print num1
//			    
//			    /*Comparison operators:
//			     	1. ==
//			     	2. !=
//			     	3. <
//			     	4. >
//			     	5. <=
//			     	6. >=
//			     */
//			    
//			    /* Logical operator:
//			     	1. && - Logical and Operator =returns true if both conditions are true
//			     	2. || - Logical or operator	 =returns true if any condition are true
//			     	3. !  - Logical not			 =returns true if condition is false and vice versa
//			     */
//			    
//			    //Taking user input in Java
//			    Scanner scan= new Scanner(System.in);
//			    System.out.print("enter input: ");
//			    String input= scan.nextLine();		// it will accept only string
//			    System.out.println(input);
//			    
//			    // string methods
//			    String Name = "java";
//			    String channel = "CodeWithHarry";
//			    System.out.println(Name.length()); //length of string
//			    System.out.println(Name + "by" + channel); //concatinated
//			    System.out.println(Name.toUpperCase()); // Capitalize variable string
//			    System.out.println(Name.toLowerCase()); // uncaptilize/lowercase variable string
//			    System.out.println(Name + "by\'");	// adding special character using escape sequence
//			    System.out.println(Name.contains("Har")); //check if har is available in name
//			    System.out.println(Name.charAt(2));	// return character of 2nd index
//			    System.out.println(name.endsWith("ry"));	//return true if name endswith ry
//			    System.out.println(name.indexOf("va"));	//return indexing
//			    
//			    
//			    // math functions
//			    int numb1 = 3, numb2 = 7;
//			    System.out.println(Math.max(numb1, numb2));
//			    System.out.println(Math.min(numb1, numb2));
//			    System.out.println(Math.sqrt(36));
//			    System.out.println(Math.abs(-36));
//			    System.out.println(Math.abs(6));
//			    System.out.println(Math.random());
//			    System.out.println(4+(8-4)*Math.random());
			    
			    // If-else statements

	}

}
