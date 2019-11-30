/*
 * Filename: getLastFile.c
 *
 * cc getLastFile.c -o getLastFile
 *
 * Description: Reads .per files in the directory. The most current
 * of that file type (thisFile) is returned. The most current, meaning
 * the youngest file of c_time is returned.
 *
 * Author:  Frank Cermak
 *
 * Date: 17-Nov-2019
 *
 * Revisions:
 *
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <dirent.h>

char fileName[256];
char thisFile[256];

int main (int argc, char *argv[])
{

   struct dirent *entry;
   struct dirent *next;
   DIR           *dp;
   int           this = 0;
   int           prev = 0;

   struct stat sb;

   dp=(opendir("/home/frank/examples/c/"));
   if (dp == NULL)
   {
      return -1;
   }
   
   while((entry=readdir(dp)))
   {
      if(strstr(entry->d_name,".per"))
      {
         strcpy(fileName, entry->d_name);
         if(stat(fileName, &sb) == -1)
         {
            perror("stat");
         }
         else
         {
            printf("Filename is: %s %d %d %d\n", 
              entry->d_name, sb.st_ctime, sb.st_atime, sb.st_mtime);
         }
         this = sb.st_ctime;
         if((prev - this) < 0)
         {
            printf("The latest file is: %s %d\n", fileName,(prev-this));
            strcpy(thisFile, entry->d_name);
            prev = this;
         }
      }
   }
   closedir(dp);
   printf("File to use is %s\n", thisFile);

   return 0;
}

