#include<iostream>
using namespace std;

int Selection_Sort(int arr[],int n);
int Bubble_Sort(int arr[],int n);
int Insertion_Sort(int arr[],int n);


int Selection_Sort(int arr[],int n){

    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if(arr[j]<arr[i]){
                int temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }

        }
    }

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return(0);
}

int Bubble_Sort(int arr[],int n){
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(arr[j]<arr[j+1]){
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }

        }
    }

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return(0);
}

int Insertion_Sort(int arr[],int n){
    
    for(int i=1;i<n;i++){
        int current =arr[i];
        int j=i-1;
        while(arr[j]>current && j>=0){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=current;
    }

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    return(0);
}

int main(){

    int n;
    cout<<"Enter the number of elements: ";
    cin>>n;
    cout<<endl;
    int arr[n];
    cout<<"Enter the elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"\n1. Bubble Sort \n2. Selection Sort \n3. Insertion Sort \n4. Quick Sort \n5. Merg Sort \n6. Heap Sort  \nEnter the opption number:";
    cout<<"Using which method you want to sort the array: ";
    int choice;
    cin>>choice;
    switch (choice)
    {
    case 1:
        Bubble_Sort(arr,n);
        break;
    case 2:
         Selection_Sort(arr,n);
        break;
    case 3:
        Insertion_Sort(arr,n);
        break;
    
    default:
        break;
    }
    return(0);
}