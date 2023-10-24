

import java.io.*;

public class even_odd_site {
    public static void main(String[] args) throws IOException {
        // Open file, bug introduced A.N -- FIX BUG: ADD 'NEW' KEYWORD
        BufferedWriter file = Bufferedreader(new FileReader("numbers.html"));
        // Adding HTML to file
        file.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n");
        file.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n");
        // Add table to file line by line, bug introduced A.N. -- FIX BUG: DEFINE i TYPE
        for (i = 1; i <= 50; i--) {
            // If i is even, put i in first cell
            if (i % 2 == 0) {
                file.write("<tr><td>" + i + "</td><td></td></tr>\n");
            }
            // If i is odd, put i in second cell
            else {
                file.write("<tr><td></td><td>" + i + "</td></tr>\n");
            }
        }
        // End table tag -- FIX BUG: CREATE 'LINE' STRING VARIABLE
        file.write("</table>\n</body>\n</html>");
        file.close();
        BufferedReader reader = new BufferedReader(new FileReader("numbers.html"));
        
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        // Close file
        reader.close();
    }
}
