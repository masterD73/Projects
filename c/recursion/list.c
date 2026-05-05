#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} node;

node* FlipList(node* curr)
{
	node* new_head = NULL;
	if(!curr || !curr->next)
	{
		return curr;
	}
	
	new_head = FlipList(curr->next);
	curr->next->next = curr;
	curr->next = NULL;
	
	return new_head;
}

node* createNode(int new_data) {
    node* new_node = (node*)malloc(sizeof(node));
    new_node->data = new_data;
    new_node->next = NULL;
    return new_node;
}

void printList(node* node) {
    while (node != NULL) {
        printf(" %d", node->data);
        node = node->next;
    }
    printf("\n");
}

int main() {
  
    node* head = createNode(1);
    head->next = createNode(2);
    head->next->next = createNode(3);
    head->next->next->next = createNode(4);
    head->next->next->next->next = createNode(5);
    
    printf("Given Linked List:");
    printList(head);
    head = FlipList(head);

    printf("Reversed Linked List:");
    printList(head);

    return 0;
}
