#include <pthread.h> /* POSIX Threads */
#include <stdlib.h>
#include <stdio.h>
//#include <fstream>

#define numOfThreads 16

typedef struct args{
  unsigned long long* arrayptr;
  int thread_no;
}arg;
#define upperbound 1000
const unsigned long long maxSize =200000; // originally not a global variable, but I need it in functions, I don't think macros will work.
pthread_mutex_t lock;
void init_emptyAry(void *ptr);
void solve_problem(void *ptr);

pthread_mutex_t lock;

int main(){
  pthread_t threadArray[numOfThreads]; /* thread variables */
  //	std::ofstream dataOut("problem110_analysis.txt");
  arg lowOrdInter[numOfThreads];

  unsigned long long j=0;
	int i= 0;
	//	int upperbound = 1000;
	int answer = 0;
	//	unsigned long long maxSize = 100000000;
	unsigned long long* otherarray= NULL;
	otherarray= (unsigned long long*)malloc(maxSize * sizeof(unsigned long long));
	//  coordinates = (struct xy *)malloc(sizeof(struct xy) * EXPECTED_MAX);

	for(i=0 ; i<numOfThreads;i++){
	  lowOrdInter[i].thread_no = i;
	  lowOrdInter[i].arrayptr=&otherarray[0];
	}
	for( i=0; i<numOfThreads; i++){
    pthread_create(&threadArray[i], NULL,(void *) &init_emptyAry, (void *) &lowOrdInter[i]);
  }
printf("%llu \n", otherarray[1000]);


  for(i = 0; i<numOfThreads; i++){
    pthread_join(threadArray[i], NULL);
  }

for( i=0; i<numOfThreads; i++){
    pthread_create(&threadArray[i], NULL,(void *) &solve_problem, (void *) &lowOrdInter[i]);
  }

  for(i = 0; i<numOfThreads; i++){
    pthread_join(threadArray[i], NULL);
  }
    FILE *ofp;
    char outputfilename[]="output.txt";
    
    ofp = fopen(outputfilename,"w");
    if(ofp==NULL){
      fprintf(stderr,"can't open output file\n");
      return 1;
    }//endif
    for (j = 0; j<(maxSize/2); j++){
      fprintf(ofp, "%llu %llu \n",j , otherarray[j]);
    }
  return 0;
}
void init_emptyAry(void *ptr){
  arg *LOI;//low order interleaving
  LOI = (arg *) ptr;
  //  printf("%d \n", LOI->thread_no);
  int i=0;
  for(i=LOI->thread_no; i< maxSize; i+=numOfThreads){
    LOI->arrayptr[i]=0;
  }

}

void solve_problem(void* ptr){
  arg *LOI;//low order interleaving
  LOI = (arg *) ptr;
  unsigned long long i, j;
  unsigned long long value;  
  for (i = 2+LOI->thread_no; i <= maxSize; i+=numOfThreads){		
    
    for (j = i; j <= i*(i - 1); j++){
      if ((i+j) % (i * j) == 0){
	value = (i+j) / (i * j);

	printf("%llu %llu \n" , value, LOI->thread_no);
	
	pthread_mutex_lock(&lock);
	LOI->arrayptr[value]++;
	pthread_mutex_unlock(&lock);
	if(LOI->arrayptr[value]>upperbound){
  printf("Answer: %llu %llu \n", value , LOI->arrayptr[value]); 
	  return;
	}
      }

    }
 }
}
