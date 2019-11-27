#
# bash functions. Copy paste into .bashrc
#
# To see the list of bash functions run
# declare -F at the command prompt.
#

function get_posix()
{
   echo `date +%s`
}

function get_dd-mmm-yy()
{
   echo `date +%d-%b-%y`
}

function get_hhmmss()
{
   echo `date +%H:%M:%S`
}

function mkbak()
{
   echo "Backing up $1"
   if [ -f "$1" ]; then
      echo $1 found, making a backup"
      B0=`echo $1_b0`
      B1=`echo $1_b1`
      B2=`echo $1_b2`
      
      if [ -f $B1 ]; then
         cp $B1 $B2
      fi
      
      if [ -f $B0 ]; then
         cp $B0 $B1
      fi  
      
      cp -p $1 $B0

}
