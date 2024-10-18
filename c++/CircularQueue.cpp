#include <iostream>
#define SIZE 5 // Size of Circular Queue

using namespace std;

class Queue {
   private:
    int items[SIZE], front, rear;

   public:
    Queue() {
        front = -1;
        rear = -1;
    }

    // Check if the queue is full
    bool isFull() {
        return (front == 0 && rear == SIZE - 1) || (front == rear + 1);
    }

    // Check if the queue is empty
    bool isEmpty() {
        return (front == -1);
    }

    // Adding an element
    void enQueue(int element) {
        if (isFull()) {
            cout << "Queue is full" << endl;
        } else {
            if (front == -1) front = 0; // First element
            rear = (rear + 1) % SIZE; // Circular increment
            items[rear] = element;
            cout << "Inserted " << element << endl;
        }
    }

    // Removing an element
    int deQueue() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return -1;
        } else {
            int element = items[front];
            if (front == rear) { // Queue has only one element
                front = -1;
                rear = -1;
            } else {
                front = (front + 1) % SIZE; // Circular increment
            }
            return element;
        }
    }

    void display() {
        // Function to display status of Circular Queue
        if (isEmpty()) {
            cout << "Empty Queue" << endl;
        } else {
            cout << "Front -> " << front << endl;
            cout << "Items -> ";
            int i = front;
            while (true) {
                cout << items[i] << " ";
                if (i == rear) break; // Stop when we reach the rear
                i = (i + 1) % SIZE; // Circular increment
            }
            cout << endl << "Rear -> " << rear << endl;
        }
    }
};

int main() {
    Queue q;

    // Fails because front = -1
    q.deQueue();

    q.enQueue(1);
    q.enQueue(2);
    q.enQueue(3);
    q.enQueue(4);
    q.enQueue(5);

    // Fails to enqueue because front == 0 && rear == SIZE - 1
    q.enQueue(6);

    q.display();

    int elem = q.deQueue();

    if (elem != -1)
        cout << "Deleted Element is " << elem << endl;

    q.display();

    q.enQueue(7);
    q.display();

    // Fails to enqueue because front == rear + 1
    q.enQueue(8);

    return 0;
}
