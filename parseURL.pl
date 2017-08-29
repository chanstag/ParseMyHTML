#!/usr/bin/perl

use LWP::Simple;
my $browser = LWP::UserAgent->new;


print "content-type: text/html \n\n";


my $url = 'https://acsapps.wku.edu/pls/prod/wkup_tar_trans_display.wkup_tar_trans_get_sbgi';

my $content = $browser->get($url); 
die "couldn't get $url" unless defined $content; 

#print $content->content(); 

my $values =  $content->content() =~ m/ VALUE=".*"/;

print $values;
