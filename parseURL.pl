#!/usr/bin/perl
use strict; 
use warnings; 

use LWP::Simple;
use DBI; 
my $browser = LWP::UserAgent->new;


print "content-type: text/html \n\n";


my $url = 'https://acsapps.wku.edu/pls/prod/wkup_tar_trans_display.wkup_tar_trans_get_sbgi';

my $content = $browser->get($url); 
die "couldn't get $url" unless defined $content; 

#print $content->content(); 

my $value = $content->content(); 
#print $value;
my @list;
my @univs; 
foreach (split(/\n/, $value)){
	$_=~ m/VALUE="(.*)"/m || next;

	push @list, $1;

	$_=~ m/>(.*)<\/OPTION>/m || next;  
	
	print$1;
	push @univs, $1;
#	print$2; 
}

 #print @list; 
=for comment
foreach(@list){

	print "$_\n";
	
}
=cut


foreach(@univs){
	print"$_\n"; 
}

#write results out to file or Database

my $driver = "mysql";
my $database = "transfercredits";
my $dsn = "DBI:$driver:database=$database";
my $user = "root";
my $password = "";

my $dbh = DBI->connect($dsn, $user, $password) or die $DBI::errstr;  

my $schooltable = "School";
my $sth = $dbh->prepare("INSERT INTO $schooltable (ID, School) values (?, ?)") or die $DBI::errstr; 
foreach my $i (0 .. $#list){

    $sth->execute($list[i], $univs[i]) or die $DBI::errstr;
}

$sth->finish(); 
$dbh->commit or die $DBI::errstr;
