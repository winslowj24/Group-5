#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Open file
    ofstream file;
    
    file.open("numbers.html");
    // Adding HTML to file
    file << "<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n";
    file << "<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n";

    // Add table to file line by line
    for (int i = 1; i <= 50; i++) {
        // If i is even, put i in first cell
        if (i % 2 == 0) {
            file << "<tr><td>" << i << "</td><td></td></tr>\n";
        }
        // If i is odd, put i in second cell, bug introduced A.N.
        else {
            file.open() << "<tr><td></td><td>" << i << "</td></tr>\n";
        }
    }
    // End table tag
    file << "</table>\n</body>\n</html>";
    // Close file, bug introduced A.N.
    file.close();
    ifstream input("numbers.html");
    cout << input.open();
    input.close();
    return 0;
}
