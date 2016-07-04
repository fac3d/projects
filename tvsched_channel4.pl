#!/usr/bin/perl
use strict;
use warnings;
##############################################################################
#
# Program Name: tvsched_channel4.pl
# Date:		03-July-2016
# Author:	Frank Cermak
# Summary:	MySql tests and various routines.                   
#
###############################################################################

###############################################################################
#
# Database
#
###############################################################################
use DBI;
my $dsn = "DBI:mysql:tvschedule";
my $dbh = "";
my $sql = "";
my $sth = "";
my $username = '';
my $password = '';

###############################################################################
#
# Global Variable Declaration.
#
###############################################################################
my @gRowArray="";			# Global Row Array
my $gFirstFreeRecord="";		# Global First Free Record
my $gLastFreeRecord="";		# Global Last Free Record
my $gPriOneRecord="";		# Global Priority One Record
my $gPriTwoRecord="";		# Global Priority Two Record
my $gPriThreeRecord="";		# Global Priority Three Record
my $gNumberOfFreeRecords="";	# Global Number of Free Records
my $gNumberOfUsedRecords="";	# Global Number of Used Records
my $return=0;


###############################################################################
# Main Program:                         
###############################################################################
my %attr = ( PrintError=>0,  # turn off error reporting via warn()
             RaiseError=>1); # turn on error reporting via die()

printf("main: initializeProgram()\n");    initializeProgram();
printf("main: clearAllTimeSlots()\n");    clearAllTimeSlots();
printf("main: setDefaultProgramming()\n");setDefaultProgramming();
printf("main: showAllTimeSlots()\n");     showAllTimeSlots();
printf("main: showAllUsedTimeSlots()\n"); showAllUsedTimeSlots();
printf("main: showAllFreeTimeSlots()\n"); showAllFreeTimeSlots();

$return = checkTimeSlot('slot_13');
if ($return == 1){
  printf("main: checkTimeSlot(): slot_13 busy: status: %d\n", $return); 
  printf("main: Special Show not added.\n");                           
}

if ($return == 0){
  printf("main: checkTimeSlot(): slot_13 open: status: %d\n", $return); 
  printf("main: updateTimeSlotPriOne()\n"); updateTimeSlotPriOne('slot_13', 'Special Show');
  printf("main: Special Show added.\n");                           
}

printf("main: showAllTimeSlots()\n");     showAllTimeSlots();

printf("main: clearTimeSlot():  \n");     clearTimeSlot('slot_13');
$return = checkTimeSlot('slot_13');
if ($return == 1){
  printf("main: checkTimeSlot(): slot_13 busy: status: %d\n", $return);
  printf("main: Special Show not added.\n");
}

if ($return == 0){
  printf("main: checkTimeSlot(): slot_13 open: status: %d\n", $return);
  printf("main: updateTimeSlotPriOne()\n"); updateTimeSlotPriOne('slot_13', 'Special Show');
  printf("main: Special Show added.\n");
}

#printf("main: checkTimeSlot(): %s\n",     checkTimeSlot('slot_14'));
#printf("main: updateTimeSlotPriOne()\n"); updateTimeSlotPriOne('slot_13', 'Real Special Show');
printf("main: showAllTimeSlots()\n");     showAllTimeSlots();
printf("main: closeProgram()\n");         closeProgram();   
closeProgram();

###############################################################################
# Subroutine: initializeProgram
###############################################################################
sub initializeProgram {

   $dbh  = DBI->connect($dsn, $username, $password, \%attr);

}

###############################################################################
# Subroutine: closeProgram
###############################################################################
sub closeProgram {

   $dbh->disconnect();

}

###############################################################################
# Subroutine: setDefaultProgramming
###############################################################################
sub setDefaultProgramming {

  updateTimeSlotPriOne('slot_11', 'News at 5:00');
  updateTimeSlotPriOne('slot_12', 'News at 5:30');
  updateTimeSlotPriOne('slot_13', 'News at 6:00');
  updateTimeSlotPriOne('slot_14', 'News at 6:30');

  updateTimeSlotPriOne('slot_33', 'News at 4:00');
  updateTimeSlotPriOne('slot_34', 'News at 4:30');
  updateTimeSlotPriOne('slot_35', 'News at 5:00');
  updateTimeSlotPriOne('slot_36', 'News at 5:30');

}

###############################################################################
# Subroutine: checkTimeSlot
# 
#
# Returns 0 for open time slot, 1, 2 or 3 based on used time slot and the 
# priority of what is in there.
###############################################################################
sub checkTimeSlot {

  my $inStr = $_[0];
  printf("checkTimeSlot(): %s\n", $inStr);
  $sql = "SELECT time_slot FROM channel4 where time_slot = '$inStr' 
                                          and show_title != ''";
  $sth = $dbh->prepare($sql);
  $sth->execute();
  @gRowArray = $sth->fetchrow_array();  
  $sth->finish();
  return (scalar @gRowArray);

}

###############################################################################
# Subroutine: updateTimeSlotPriOne
# 
#
# Updates the channel table with a priority one show.
###############################################################################
sub updateTimeSlotPriOne {

  my $inTimeSlot  = $_[0];  # time_slot  
  my $inShowTitle = $_[1];  # show_title
  printf("updateTimeSlotPriOne(): %s\t%s\n", $inTimeSlot, $inShowTitle);

  $sql = ("UPDATE channel4 set show_title = '$inShowTitle' where time_slot = '$inTimeSlot'");
  printf("updateTimeSlotPriOne(): %s\n", $sql);
  $sth = $dbh->prepare($sql);
  $sth->execute();

}

###############################################################################
# Subroutine: updateTimeSlotPriTwo
# 
#
# Updates the channel table with a priority two show.
###############################################################################
sub updateTimeSlotPriTwo {


}

###############################################################################
# Subroutine: updateTimeSlotPriThree
# 
#
# Updates the channel table with a priority three show.
###############################################################################
sub updateTimeSlotPriThree {


}

###############################################################################
# Subroutine: clearTimeSlot
# 
#
# Clears the input time_slot record.
###############################################################################
sub clearTimeSlot {

  my $inStr = $_[0];
  printf("clearTimeSlot(): %s\n", $inStr);
  $sql = ("UPDATE channel4 set show_title = ' ' where time_slot = '$inStr'");              
  $sth = $dbh->prepare($sql);
  $sth->execute();

}



###############################################################################
# Subroutine: clearAllTimeSlots
# 
#
# Clears the show_title and length.
###############################################################################
sub clearAllTimeSlots {

  $sql = ("UPDATE channel4 set show_title = ' '");              
  $sth = $dbh->prepare($sql);
  $sth->execute();

  $sql = ("UPDATE channel4 set length = ' '");              
  $sth = $dbh->prepare($sql);
  $sth->execute();
}

###############################################################################
# Subroutine: createChannelTable
# 
#
# Creates a channel table.
###############################################################################
sub createChannelTable {


}

###############################################################################
# Subroutine: bumpExistingTimeSlot
# 
#
# Bumps an existing show in the provided time_slot with a new show.
###############################################################################
sub bumpExistingTimeSlot {

  $sql = ("UPDATE channel4 set show_title = 'news at 13' 
                          where time_slot = 'slot_13'");
  $sth = $dbh->prepare($sql);
  $sth->execute();

}

###############################################################################
# Subroutine: showAllTimeSlots
# 
# Does a select * on the channel table.
#
###############################################################################
sub showAllTimeSlots {

  $sql = "SELECT * FROM channel4";
  $sth = $dbh->prepare($sql);
  # execute the query
  $sth->execute();
  while(@gRowArray = $sth->fetchrow_array()){      
      printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",
      $gRowArray[0], $gRowArray[1], $gRowArray[2], $gRowArray[3], 
      $gRowArray[4], $gRowArray[5], $gRowArray[6]);
  } 
  $sth->finish();

  #return (scalar @gRowArray);

}

###############################################################################
# Subroutine: showAllUsedTimeSlots
# 
#
# Does a select * where .
###############################################################################
sub showAllUsedTimeSlots {

  $sql = "SELECT * FROM channel4 where show_title != ''";
  $sth = $dbh->prepare($sql);
  my $choice = "";
  $sth->execute();
  while(@gRowArray = $sth->fetchrow_array()){      
      printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",
      $gRowArray[0], $gRowArray[1], $gRowArray[2], $gRowArray[3], 
      $gRowArray[4], $gRowArray[5], $gRowArray[6]);
  }
  $sth->finish();

}

###############################################################################
# Subroutine: showAllFreeTimeSlots
# 
#
# Does a select * where .
###############################################################################

sub showAllFreeTimeSlots {

  $sql = "SELECT * FROM channel4 where show_title = ''";
  $sth = $dbh->prepare($sql);
  my $choice = "";
  $sth->execute();
    while(@gRowArray = $sth->fetchrow_array()){
      printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\n",
      $gRowArray[0], $gRowArray[1], $gRowArray[2], $gRowArray[3], 
      $gRowArray[4], $gRowArray[5], $gRowArray[6]);
  }
  $sth->finish();

}

###############################################################################
# Subroutine: setProgramVariables
# 
#
# Sets or reset's the global program variables.
###############################################################################
sub setProgramVariables {

  return 0;
}












