#!/usr/bin/perl -w
use Tk;
use DBI;

###############################################################################
# https://www.safaribooksonline.com/library/view/mastering-perltk/1565927168/ch07s09.html
# http://docstore.mik.ua/orelly/perl3/tk/ch07_02.htm
# http://docstore.mik.ua/orelly/perl3/tk/ch05_02.htm
###############################################################################
################################################################################
#
# Program Name: tv_schedupdate.pl
# Date:		03-July-2016
# Author:	Frank Cermak
# Summary:	Updates mysql database with a new show.
#
################################################################################

###############################################################################
# Database
###############################################################################
my $dsn = "DBI:mysql:tvschedule";
my $dbh = "";
my $sql = "";
my $sth = "";
my $username = '';
my $password = '';
my %attr = ( PrintError=>0,  # turn off error reporting via warn()
             RaiseError=>1); # turn on error reporting via die();

###############################################################################
# Program globals.
###############################################################################
my $start    = "";
my $channel  = "";
my $newshow  = "";

###############################################################################
# Main Window.
###############################################################################
$mw = MainWindow->new;
$mw->title("TV Schedule Database Update");

###############################################################################
# Arrays.  
###############################################################################
@channels = qw/channel2 channel4 channel5 channel7 channel9/;
@starttime = ("12:00am", "12:30am", "1:00am", "1:30am", "2:00am", "2:30am", "3:00am", "3:30am",
              "4:00am", "4:30am", "5:00am", "5:30am", "6:00am", "6:30am", "7:00am", "7:30am",
              "8:00am", "8:30am", "9:00am", "9:30am", "10:00am", "10:30am", "11:00am", "11:30am",
              "12:00pm", "12:30pm", "1:00pm", "1:30pm", "2:00pm", "2:30pm", "3:00pm", "3:30pm",
              "4:00pm", "4:30pm", "5:00pm", "5:30pm", "6:00pm", "6:30pm", "7:00pm", "7:30pm",
              "8:00pm", "8:30pm", "9:00pm", "9:30pm", "10:00pm", "10:30pm", "11:00pm", "11:30pm");

#@starttime = qw/12:00am 12:30am 1:00am 1:30am 2:00am 2:30am 3:00am 3:30am 4:00am 4:30am/;
# 5:00am  5:30am 6:00am 6:30am 7:00am 7:30am 8:00am 8:30am 9:00am 9:30am
# 10:00am 10:30am 11:00am 11:30am 12:00pm 12:30pm 1:00pm 1:30pm 2:00pm 2:30pm
# 3:00pm  3:30pm 4:00pm 4:30pm 5:00pm 5:30pm 6:00pm 6:30pm 7:00pm 7:30pm
# 8:00pm  8:30pm 9:00pm 9:30pm 10:00pm 10:30pm 11:00pm 11:30pm
###############################################################################
# Entry widget.
###############################################################################
my $entry = $mw->Entry(-textvariable => \$newshow)->pack(-side => "bottom", -fill => "x");

###############################################################################
# Listbox Channels.
###############################################################################
my $lbc = $mw->Scrolled("Listbox", -scrollbars => "osoe", )->pack(-side => "left");
$lbc->insert("end", sort @channels);

###############################################################################
# Listbox Time Slots.
###############################################################################
my $lbts = $mw->Scrolled("Listbox", -scrollbars => "osoe", )->pack(-side => "left");
#$lbts->insert("end", sort @starttime);
$lbts->insert("end", @starttime);

###############################################################################
# Exit Button
###############################################################################
$mw->Button(-text => "_Exit_", 
            -command => sub { exit; })->pack(-side => "bottom");

###############################################################################
# Update DB Button.
###############################################################################
$mw->Button(-text => "Update", 
            -command => sub { updatedb(); })->pack(-side => "bottom");

###############################################################################
# MainLoop.
###############################################################################
MainLoop;

###############################################################################
# subroutine updateddb().
###############################################################################
sub updatedb {
  my $outString = "";
  printf("updatedb: %s\n", $newshow);

  my @selected = $lbts->curselection;
  foreach (@selected) {
    printf("updatedb: %s\n", $starttime[$_]);
    $start = $starttime[$_];
  }

  $outString = "UPDATE channel4 SET show_title = '$newshow' WHERE start = '$start';";
# UPDATE channel4 SET show_title = 'adfadsf' WHERE time_slot = 'slot_7';
  printf("updatedb: %s\n", $outString);
  $dbh = DBI->connect($dsn, $username, $password, \%attr);
  $sql = $outString;
  $sth = $dbh->prepare($sql);
  $sth->execute();
  $dbh->disconnect();

}


