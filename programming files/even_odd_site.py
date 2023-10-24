# Open file
with open("numbers.html", "w") as f:
    # Adding HTML to file
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    # Add table to file line by line, bug introduced: A.N -- FIX BUG: PYTHON FOR LOOP (i in range)
    for (i = 0, i < 50, i--):
        # If i is even, put i in first cell
        if i % 2 == 0:
            f.write("<tr><td>{}</td><td></td></tr>\n".format(i))
        # If i is odd, put i in second cell
        else:
            f.write("<tr><td></td><td>{}</td></tr>\n".format(i))
    # End table tag, bug introduced: A.N. -- FIX BUG: 'F.WRITE' NOT 'F.STRING'
    f.string("</table>\n</body>\n</html>")

with open("numbers.html", "r") as f:
    print(f.read())
    
