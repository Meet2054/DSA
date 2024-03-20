#include <iostream>
#include <vector> // for vector
#include <algorithm> // for swap

using namespace std;

void Bubble_Sort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void Selection_Sort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            swap(arr[i], arr[minIndex]);
        }
    }
}

void Insertion_Sort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int current = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = current;
    }
}

int partition(vector<int>& arr, int l, int r) {
    int pivot = arr[r];
    int i = l - 1;
    for (int j = l; j < r; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[r]);
    return i + 1;
}

void QuickSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int pi = partition(arr, l, r);
        QuickSort(arr, l, pi - 1);
        QuickSort(arr, pi + 1, r);
    }
}

int Merge(vector<int>& arr,int l,int mid,int r){
      int n1 = mid - l + 1;
    int n2 = r - mid;

    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++) {
        L[i] = arr[l + i];
    }

    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + j + 1];
    }

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    return 0;
}

int MergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int mid = l + (r - l) / 2;
        MergeSort(arr, l, mid);
        MergeSort(arr, mid + 1, r);
        Merge(arr, l, mid, r);
    }
    return 0;
}
int CountSort(vector<int>& arr) {
    int n = arr.size();

    // Find the maximum element in the array
    int k = *max_element(arr.begin(), arr.end());

    // Create a count array and initialize all elements as 0
    vector<int> count(k + 1, 0);

    // Store the count of each element
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // Modify the count array such that each element at each index
    // stores the sum of previous counts
    for (int i = 1; i <= k; i++) {
        count[i] += count[i - 1];
    }

    // Output array
    vector<int> output(n);

    // Build the output array
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    // Copy the output array to arr, so that arr now contains sorted numbers
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }

    return 0;
}

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    vector<int> arr(n);
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << "\n1. Bubble Sort \n2. Selection Sort \n3. Insertion Sort \n4. Quick Sort \n5. Merge Sort \n6. Count Sort \nEnter the option number: ";
    int choice;
    cin >> choice;
    switch (choice) {
        case 1:
            Bubble_Sort(arr);
            break;
        case 2:
            Selection_Sort(arr);
            break;
        case 3:
            Insertion_Sort(arr);
            break;
        case 4:
            QuickSort(arr, 0, n - 1);
            break;
        case 5:
            MergeSort(arr,0,n-1);
            break;
        case 6:
            CountSort(arr);
            break;
        default:
            cout << "Invalid option!";
            break;
    }
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
