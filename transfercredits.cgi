#!"C:\xampp\perl\bin\perl.exe"

use strict;
use warnings; 

use DBI; 
use CGI; 

print "content-type: text/html\n\n";
print <<WEB_PAGE; 
    <html>
        <head>
        </head>
        <body>
            <h1> Welcome to Transfer Credit App </h1>
            <form action="/cgi-bin/transfercreds.cgi" method="post">
                <p> Would you like to search by State or by Country?</p><br>
                State: <input type="radio" value="state" name="state"><br>
                Country: <input type="radio" value="country" name="state"><br>
                <input type="submit" value="Submit">
            </form> 
        </body> 
    </html> 
WEB_PAGE

