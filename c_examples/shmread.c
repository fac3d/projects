/*
 * Filename: shmread.c
 * gcc shmread.c -o shmread
 *
 */

#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{

   int shmid;
   key_t key=123456;
   char *shared_memory;

   shmid=shmget(key, 11, IPC_CREAT | 0666);
   for(int i=0; i<10; i++)
   {
      char *str=shmat(shmid, NULL, 0);
      printf("%s\n", str);
      sleep(1);
   }

   shmdt(shmid);
   shmctl(shmid, IPC_RMID, NULL);

return 0;
}
