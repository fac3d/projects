/*
 * Filename: shmwrite.c
 * gcc shmwrite.c -o shmwrite
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
   shared_memory=shmat(shmid, NULL, 0);

   for(int i=0; i<20; i++)
   {
      shmid=shmget(key, 11, IPC_CREAT | 0666);
      shared_memory=shmat(shmid, NULL, 0);
      memcpy(shared_memory, "Hello", sizeof("Hello"));
      sleep (1);
      memcpy(shared_memory, "There", sizeof("There"));
      sleep (1);
   }

   shmdt(shmid);
   shmctl(shmid, IPC_RMID, NULL);

return 0;
}
