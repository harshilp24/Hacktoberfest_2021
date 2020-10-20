#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int value[10], front = -1, rear = -1, MAX = 10;
int i;

bool is_full() {
	bool x = true;
	
	for(i=0 ; i < MAX; i++) {
		if(value[i] != NULL) { 
			x = true; 
		}
		
		else {
			x = false;
			break;
		}
	}
	
	return x;
}

void circularQueue(int num) {
	if(front == -1 && rear == -1) {
		front = 0; rear = 0;
		
	}
	
	if(rear == MAX) {
		rear = 0;
		
	}
	
	if(!is_full()) { 
		value[rear] = num; 
		rear++; 
	}
	
	else {
		printf("OVERFLOW!\n");
	}
	
}

void dequeue() {
	value[front] = 0;
	front++;
	
}

void print() {
	int i;
	for(i = 0; i < MAX; i++) {
		printf("%d ", value[i]);
		
	}
	
}

int main(int argc, char *argv[]) {
	circularQueue(1);
	circularQueue(2);
	circularQueue(3);
	circularQueue(4);
	circularQueue(5);
	circularQueue(6);
	circularQueue(7);
	circularQueue(8);
	circularQueue(9);
	circularQueue(10);
	dequeue();
	circularQueue(11);
	
	print();
	return 0;
}
