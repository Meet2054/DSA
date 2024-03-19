#include<iostream>
using namespace std;

int Binary_Search(int arr[],int n,int ele);
int Linear_Search(int arr[],int n,int ele);


   
int Binary_Search(int arr[], int n, int ele) {
    int s = 0, e = n - 1; // Initialize end to n-1
    while (s <= e) {
        int mid = (s + e) / 2;
        if (arr[mid] == ele) {
            cout << "Yes the element is present in the array and it is at the " << mid + 1 << " position";
            return 0;
        } else if (arr[mid] > ele) {
            e = mid - 1;
        } else {
            s = mid + 1;
        }
    }
    return -1;
}



int Linear_Search(int arr[],int n,int ele){

    for(int i=0;i<n;i++){
        if(arr[i]==ele){
            cout<<"Yes the element is present in the array and it is at the "<<i+1<<" position";
            break;
        }
    }
    return(0);
}


int main(){
    cout<<"Enter the size of array :";
    int n;
    cin>>n;
    int arr[n];
    cout<<"Enter the elemants :";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    cout<<"This are Some method to search the element from the array Select it \n1. Binary Search \n2. Linear Search \n:-";
    int c,ele;
    cin>>c;
    cout<<"Select the element you want to search :";
    cin>>ele;
    switch (c){
        case 1:
            Binary_Search(arr,n,ele);
            break;
        case 2:
            Linear_Search(arr,n,ele);
            break;
        default:
            cout<<"Enter the valid option ";
    }
    return(0);
}