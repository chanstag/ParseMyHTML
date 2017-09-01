#!"C:\xampp\perl\bin\perl.exe"

use strict; 
use warnings;
use CGI; 

print "content-type: text/html\n\n";

my $cgi = CGI->new();

print $cgi->header();

my $state = $cgi->param('state');

my $country = $cgi->param('country');


 

print <<"WEB_PAGE"; 
    <html>
        <head>
        </head> 
        <body>
            <h1> Transfer Credit APP </h1>
WEB_PAGE
my $val = $state;

print "<p>this is the value: $val</p>";

if($val eq "state"){

    print "<div id = 'navbar' style='width: 100%; text-align: center;'>"; 
    print "<a href='university.cgi?state=$_' style='font-size: 20px; margin: 20px;' >$_</a>" for "a".."z"; 
    print "</div>"; 
    print "<hr>";


}
print <<"END";

    </body>
</html>
END

my $driver = "mysql";
my $database = "transfercredits";
my $dsn = "DBI:$driver:database=$database";
my $user = "root";
my $password = "fenix432";

my $dbh->prepare