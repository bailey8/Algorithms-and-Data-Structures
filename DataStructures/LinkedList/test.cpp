#include<iostream>
using namespace std;

//create node class
struct node{
    int data;
    node* next;

};

//create List class
class List{
    public:
        node * head = nullptr;
        node *tail = nullptr;
        List(){
            head = NULL;
            tail=NULL;
        }
   
 
    void prepend(int value){
        node* fresh = new node;
        fresh -> data = value;
        fresh -> next = nullptr;
        if(head == nullptr){
            head = fresh;
            tail = fresh;

        }
        else{
        node *temp = head;
        head = fresh;
        head -> next = temp;
        }
    }
        
    
    void append(int value){
        node * fresh;
        fresh -> next = nullptr;
        fresh -> data = value;
        node * temp = tail;
        tail = fresh;
        temp -> next = fresh;
    }
        
    

    // void insert(int pos, int value)
      


    // void delete_first()

    // void delete_position(int pos)

    // void delete_last()
void insert_start(int value)
		{
			node *temp=new node;
			temp->data=value;
			temp->next=head;
			head=temp;
		}

    void display(node * ptr){
        if(ptr -> next ==  NULL){
           cout << ptr -> data;
           return;
       }
       cout << ptr -> data << endl;
       display(ptr -> next);
    }

};

int main(int argc, char const *argv[])
{
    List obj;
     obj.prepend(44);
     obj.prepend(66);

    obj.display(obj.head);





    return 0;
}

		 