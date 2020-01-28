/*
* Filename: README.txt
*/
Set this environment variables. The below command lines could just use $PWD but
that is not in keeping with Java.

CLASSPATH=$PWD
export CLASSPATH

Trouble I had was just running rmiregistry. Well, that is not in my $PATH. Did a
filesystem check for rmiregistry and running it with full pathname. It works ok.
/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.232.b09-0.el7_7.x86_64/jre/bin/rmiregistry &

Below is the command line to run both programs.
java -classpath $CLASSPATH -Djava.rmi.server.codebase=file:$CLASSPATH/ example.rmifunctions.Server  &
java -classpath $CLASSPATH -Djava.rmi.server.codebase=file:$CLASSPATH/ example.rmifunctions.Client
