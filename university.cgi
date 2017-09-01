#!"C:\xampp\perl\bin\perl.exe"

use strict;
use warnings;

use CGI;
use DBI; 

my $cgi = CGI->new();
print $cgi->header();


print <<"WEB_PAGE"; 
    <html>
        <head>
        </head> 
        <body>
            <h1> Transfer Credit APP </h1>
WEB_PAGE


my $letter = $cgi->param("state");

my $driver = "mysql";
my $database = "transfercredits";
my $dsn = "DBI:$driver:database=$database";
my $user = "root";
my $password = "fenix432";

my $dbh = DBI->connect($dsn, $user, $password) or die $DBI::errstr;

my $table = "School";
my $sth = $dbh->prepare("SELECT * FROM $table WHERE SUBSTRING(School, 1, 1)= ?");
$sth -> execute($letter);

while(@data = $sth->fetchrow_array()){
    my $id = $data[0];
    my $school = $data[1];

    print"<p>The id is: $id The school is: $school </p>";
}

print <<"END";

    </body>
</html>
END