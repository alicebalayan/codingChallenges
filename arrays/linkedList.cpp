#include <iostream>

using namespace std;

struct Node { 
   int data; 
   struct Node *next; 
}; 

struct Node* head = NULL;  

void insert_node (int n) { 
    struct Node *temp = new Node; 
    temp -> data = n; 
    temp -> next = head; 
    head = temp;
} 
void display_List() { 
   struct Node *pointer;
   pointer = head; 
   while (pointer != NULL) { 
     cout<<pointer -> data<<" "; 
     pointer = pointer -> next;
   }
}
int main() { 
   insert_node(5);
   insert_node(4);
   insert_node(3);
   cout<<"The linked list is: ";
   display_List(); 
   return 0; 
} 