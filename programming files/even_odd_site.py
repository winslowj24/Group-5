# Open file
with open("numbers.html", "w") as f:
    # Adding HTML to file
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    # Add table to file line by line
    for i in range(1, 50):
        # If i is even, put i in first cell
        if i % 2 == 0:
            f.write("<tr><td>{}</td><td></td></tr>\n".format(i))
        # If i is odd, put i in second cell
        else:
            f.write("<tr><td></td><td>{}</td></tr>\n".format(i))
    # End table tag
    f.write("</table>\n</body>\n</html>")

with open("numbers.html", "r") as f:
    print(f.read())
    
