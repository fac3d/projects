#!/usr/bin/perl -w
use Tk;
# http://www.perlmonks.org/?node_id=731610
# http://www.bin-co.com/perl/perl_tk_tutorial/perl_tk_tutorial.pdf
# http://www.perlmonks.org/?node_id=731610
# http://www.perlmonks.org/?node_id=178646
###############################################################################
#
# Program name: gs.pl (Ground System) Part of overall perl tk projects.
# 
# Date: 10-Jul-16
#
# Frank Cermak
#
###############################################################################
use Tk;
#
# Setup the main window.
#
my $mw = MainWindow->new;
# x, y
$mw->minsize(900, 500);
$mw->title("Test Program");
$mw->configure(-background => 'white');

#
# Setup the File menu_bar.    
#
my $menu = $mw->Frame(-relief => 'groove',
			-borderwidth => 3,
			-background => 'white',
			)->pack('-side' => 'top', -fill => 'x');

my $file_menu = $menu->Menubutton(-text => 'File', 
			#-background => 'white',
			#-activebackground => 'black',
			#-foreground => 'gray',
			)->pack('-side' => 'left');	

$file_menu->command(-label => 'Exit',
			#-activebackground => 'black',
			-command => sub{$mw->destroy});

$file_menu->separator();

#
# Setup the About Help.       
#
my $about_help = $menu->Menubutton(-text => 'Help',
                        #-background => 'purple',
                        #-activebackground => 'cyan',
                        #-foreground => 'white',
                        )->pack('-side' => 'right');

$about_help->command(-label => 'About',
                        #-activebackground => 'magenta',
                        -command => \&about);                

$about_help->command(-label => 'Help',
                        #-activebackground => 'magenta',
                        -command => \&help);                

$about_help->separator();

my $antennaButton = $mw->Button(-text => "Antenna Status",
                -width=>15,
		-command => \&antennaStatus)->pack(-side=>"top", -anchor=>'w');

my $networkButton = $mw->Button(-text => "Network Status",
                -width=>15,
		-command => \&networkStatus)->pack(-side=>"top", -anchor=>'w');

my $timeButton = $mw->Button(-text => "Time Generator",
                -width=>15,
		-command => \&timeStatus)->pack(-side=>"top", -anchor=>'w');

my $transmitterButton = $mw->Button(-text => "Transmitter Status",
	-width=>15,
	-command => \&transmitterStatus)->pack(-side=>"top", -anchor=>'w');

my $receiverButton = $mw->Button(-text => "Receiver Status",
	-width=>15,
	-command => \&receiverStatus)->pack(-side=>"top", -anchor=>'w');

my $telemetryButton = $mw->Button(-text => "Telemetry Status",
	-width=>15,
	-command => \&telemetryStatus)->pack(-side=>"top", -anchor=>'w');

my $viewSchedule = $mw->Button(-text => "View Schedule",   
	-width=>15,
	-command => \&viewSchedule)->pack(-side=>"top", -anchor=>'w');

my $createSchedule = $mw->Button(-text => "Create Schedule",   
	-width=>15,
	-command => \&createSchedule)->pack(-side=>"top", -anchor=>'w');

my $startAutonomy = $mw->Button(-text => "Start Autonomy",   
	-width=>15,
	-command => \&startAutonomy)->pack(-side=>"top", -anchor=>'w');

my $showBoat = $mw->Button(-text => "Show Boat",   
	-width=>15,
	-command => \&showBoat)->pack(-side=>"top", -anchor=>'w');

my $viewEvents = $mw->Button(-text => "View Events",   
	-width=>15,
	-command => \&viewEvents)->pack(-side=>"top", -anchor=>'w');

my $missionPlanner = $mw->Button(-text => "Mission Planner",   
	-width=>15,
	-command => \&missionPlanner)->pack(-side=>"top", -anchor=>'w');

my $txt = $mw->Scrolled('Text',
        -scrollbars=>'e',
        -width=>100, 
   	-height=>4,                 
   	-foreground=>'green',                                           
   	-background=>'black',                                           
   	-font=>'bold',
        )->pack(-side=>"bottom", -anchor=>'w');

my $exitButton = $mw->Button(-text => "Exit",          
        -width=>15,
	-command => sub{$mw->destroy})->pack(-side=>"bottom", 
        -anchor=>'w');

MainLoop();

sub antennaStatus {
   updateTextArea("Antenna status is green.");      
}

sub networkStatus {
   updateTextArea("Network status is green.");
}

sub timeStatus {
   updateTextArea("Time Generator status is green.");

   # Example for loading an image. Open a new window.
   #my $image = "21-Apr-07.gif";
   #my $sw = MainWindow->new; 
   #$sw->geometry("600x400");
   #$sw->title($image);
   #my $shot = $sw->Photo(-file => "$image");
   #my $btn = $sw->Button(-image => $shot)->pack();
   #$btn->update;
}

sub transmitterStatus {
   updateTextArea("Transmitter status is green.");
}

sub receiverStatus {
   updateTextArea("Receiver status is green.");
}

sub telemetryStatus {
   updateTextArea("Telemetry status is green.");
}

sub viewSchedule {
   updateTextArea("Viewing Schedule.");             
   my $outStr = "12-Jul-16 22:00:00 AOS begin main procedure.\n";
$outStr = $outStr."12-Jul-16 22:10:00 Main procedure complete.\n";
$outStr = $outStr."12-Jul-16 22:10:00 Battery Recharge step 1, voltage 26.5.\n";
$outStr = $outStr."12-Jul-16 22:20:00 Battery Recharge step 2, voltage 27.5.\n";
$outStr = $outStr."12-Jul-16 22:30:00 Battery Recharge step 3, voltage 28.1.\n";
$outStr = $outStr."12-Jul-16 22:40:00 Battery Recharge logic testing complete.\n";

   my $sw = MainWindow->new; 
   $sw->geometry("600x400");
   $sw->title("View Schedule");

   my $closeButton = $sw->Button(-text => "Close",          
        -width=>15,
	-command => sub{$sw->destroy})->pack(-side=>"bottom", 
        -anchor=>'w');

   my $txt = $sw->Scrolled('Text',
        -scrollbars=>'e',
        -width=>100,
        -height=>40,
        -foreground=>'green',    
        -background=>'black',    
        -font=>'bold',
        )->pack(-side=>"bottom", -anchor=>'w');
   $txt->insert('end',$outStr);                                      
   $txt->see('end');

}

sub createSchedule {
   updateTextArea("Create Schedule.");                  
}

sub startAutonomy {
   updateTextArea("Start Autonomy.");                   
}

sub viewEvents {
   updateTextArea("View Events.");                      
}
sub missionPlanner {
   updateTextArea("Mission Planner");                      
}


sub showBoat {

   # Example for loading an image. Open a new window.
   # When the boat is pressed, the window is destroyed.
   my $image = "21-Apr-07.gif";
   my $sw = MainWindow->new; 
   $sw->geometry("600x400");
   $sw->title($image);
   my $shot = $sw->Photo(-file => "$image");
   my $btn = $sw->Button(-image => $shot,
	-command => sub{$sw->destroy})->pack();
   $btn->update;
}

sub about {
}

sub help {

}


#
#
#
sub updateTextArea {
   my $inStr = $_[0];
   my $dateStr = "";
   my $timeStr = "";
   #($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime();
   ($sec,$min,$hour,$mday,$mon,$year) = gmtime();
   $dateStr = sprintf("%02d-%02d-%02d", $mday, $mon+1, $year+1900);
   $timeStr = sprintf("%02d:%02d:%02d", $hour, $min, $sec);
   my $outStr=$txt->get('1.0', 'end');
   $txt->delete('1.0', 'end');
   chomp($dateStr);
   chomp($timeStr);
   chomp($inStr);
   #$outStr=$dateStr." ".$timeStr." ".$outStr." ".$inStr;
   $outStr=$outStr." ".$dateStr." ".$timeStr." ".$inStr;
   $txt->insert('end',$outStr);                                      
   $txt->see('end');
}

