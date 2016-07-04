#!/usr/bin/perl -w
################################################################################
#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
################################################################################
#
# Program Name: tv_schedtable.pl
# Date:		03-July-2016
# Author:	Frank Cermak
# Summary:	Presents information in a Table.
#
################################################################################
use Tk;
use Tk::Table;
use strict;

################################################################################
# Globals used for file input and the @shows array.
################################################################################
my @shows = "";
my $file = "";

################################################################################
# Create the main window called mw and add the title.
################################################################################
my $mw = MainWindow->new;
$mw->geometry("1200x400");
$mw->resizable(1,1);
$mw->title("TV Schedule");

################################################################################
# Create the table and attach it to mw using pack().  
################################################################################
my $table_frame = $mw->Frame()->pack();
my $table       = $table_frame->Table(-columns => 48,
                                          -rows => 12,
                                     -fixedrows => 1,
                                  -fixedcolumns => 1,
                                    -scrollbars => 'oes',
                                        -relief => 'raised');
# These are the column headers.
my @tableHeader = (" ", "12am", "12:30am", "1am", "1:30am", "2am", "2:30am", "3am", "3:30am", 
                   "4am", "4:30am", "5am", "5:30am", "6am", "6:30am", "7am", "7:30am",
                   "8am", "8:30am", "9am", "9:30am", "10am", "10:30am", "11am", "11:30am",
                   "12:00pm", "12:30pm", "1:00pm", "1:30pm", "2:00pm", "2:30pm", "3:00pm", "3:30pm", 
                   "4:00pm", "4:30pm", "5:00pm", "5:30pm", "6:00pm", "6:30pm", "7:00pm", "7:30pm", 
                   "8:00pm", "8:30pm", "9:00pm", "9:30pm", "10:00pm", "10:30pm", "11:00pm", "11:30pm");

################################################################################
# Fill in the column headers using strings from the @tableHeader array.
################################################################################
foreach my $col (1 .. 48)
{
  my $tmp_label = $table->Label(-text => $tableHeader[$col], -width => 8, -relief =>'raised');
  $table->put(0, $col, $tmp_label);
}

################################################################################
# Default fill in each of the cells of the table with the string ...........   
################################################################################
my $tmp_label = "";
foreach my $row (1 .. 11)
{
  foreach my $col (1 .. 48)
  {
    $tmp_label = $table->Label(-text => "..........",     
                                  -padx => 2,
                                  -anchor => 'w',
                                  -background => 'white',
                                  -relief => "groove");
    $table->put($row, $col, $tmp_label);
  }
}
$table->pack();

################################################################################
# Create three buttons in the button_frame and attach it to the mw.    
# Refresh Table, Test, Exit are the buttons.
################################################################################
my $button_frame = $mw->Frame()->pack(-side => "top");
my $button_color = $button_frame->Button(-text => "Refresh Table",
                   -command => sub{refreshTable()})->pack(-side => "left");

my $button_exit = $button_frame->Button(-text => "Test",
                   -command => sub{testSubroutine()})->pack(-side => "right");

my $button_next = $button_frame->Button(-text => "Exit",
                   -command => sub{exit})->pack(-side => "right");

################################################################################
# Add a text area. Not necessary but can be used to show program state.
################################################################################
my $scroll_text = $mw->Scrollbar();
my $main_text = $mw->Text(-yscrollcommand => ['set', $scroll_text],
                          -background => 'white',
                          -foreground => 'black');

$scroll_text->pack(-side=>"right", -expand => "no", -fill => "y");
$main_text->pack(-side => "bottom", -anchor => "w",
                 -expand => "no", -fill => "both");

################################################################################
# The MainLoop.    
################################################################################
MainLoop;

################################################################################
# Subroutine testSubroutine()
################################################################################
sub testSubroutine {
   printf("testSubroutine.\n");
   my $row = 2; my $col = 4;
   my $outString = "\ntestSubroutine()";                       
   my $scroll_text = $table->get($row, $col);
   #printf("$outString\n");                         
   #$main_text->delete('0.0', 'end');
   $main_text->insert("end", $outString);      
}

################################################################################
# Subroutine refreshTable()   
################################################################################
sub refreshTable {
  dumpMySqlTable();	# Call this subroutine before reading the file.
  readFile();		# Read the file that dumpMySqlTable created.

  foreach my $col (1 .. 48)
  {
    my $tmp_label = $table->Label(-text => $tableHeader[$col], 
                             -width => 8, -relief =>'raised');
    $table->put(0, $col, $tmp_label);
  }

  foreach my $row (1 .. 11)
  {
    foreach my $col (1 .. 48)
    {
      if($row eq 1) 
      {
        $tmp_label = $table->Label(-text => $shows[$col],     
                                  -padx => 2,
                                  -anchor => 'w',
                                  -background => 'white',
                                  -relief => "groove");
        $table->put($row, $col, $tmp_label);
      }
      else 
      {
        my $tmp_label = $table->Label(-text => "...Refresh...",
                                    -padx => 2,
                                    -anchor => 'w',
                                    -background => 'white',
                                    -relief => "groove");
        $table->put($row, $col, $tmp_label);
      }
    }
  }

  $table->pack();
  my $outString = "\nRefreshed Table";		# This is sent to the text area.
  #$main_text->delete('0.0', 'end');
  $main_text->insert("end", $outString);     	# This is the main_text area call.

}

################################################################################
# Subroutine dumpMySqlTable()   
################################################################################
sub dumpMySqlTable {

my $outString = "\ndumpMySqlTable()";	# This is sent to the text area.
#$main_text->delete('0.0', 'end');
$main_text->insert("end", $outString);	# This is the main_text area call.

use DBI;
my @gRowArray = "";
my $dsn = "DBI:mysql:tvschedule";
my $dbh = "";
my $sql = "";
my $sth = "";
my $username = 'frank';
my $password = 'frank';
my %attr = ( PrintError=>0,  # turn off error reporting via warn()
             RaiseError=>1); # turn on error reporting via die()

my $outfile = "shows.txt";
open (OUTFILE, ">$outfile") or die "Could not open outfile";

$dbh  = DBI->connect($dsn, $username, $password, \%attr);
$sql = "SELECT show_title FROM channel4;";
$sth = $dbh->prepare($sql);
$sth->execute();

my $arraySize = "";
printf OUTFILE " \n";		# Need a leading blank line so the shows line up right.

while(@gRowArray = $sth->fetchrow_array()){
   $arraySize = scalar @gRowArray;
   printf OUTFILE @gRowArray;
   printf OUTFILE "\n";
}

$sth->finish();
$dbh->disconnect();
close OUTFILE;

}

################################################################################
# subroutine readFile
# Open text file and read in the contents. Assign to @shows array.
################################################################################
sub readFile {
   @shows = "";
   $file = "shows.txt";
   open INFILE, $file or die "Unable to open shows.txt";
   @shows = <INFILE>;
   close INFILE; 
}



