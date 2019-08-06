// C++ program to find out execution time of 
// of functions 
#include <algorithm> 
#include <chrono> 
#include <iostream> 
#include <vector>
#include <list>

using namespace std; 
using namespace std::chrono; 

// For demonstration purpose, we will fill up 
// a vector with random integers and then sort 
// them using sort function. We fill record 
// and print the time required by sort function 
int main() 
{ 

	vector<int> arr(100000); 
    list<int> a(100000);

	// Generate Random values 
	auto f = []() -> int { return rand() % 10000; }; 

	// Fill up the vector 
	generate(a.begin(), a.end(), f);
    generate(arr.begin(), arr.end(), f);

	// Get starting timepoint 
	auto start = high_resolution_clock::now(); 

	// Call the function,
	for(int i = 0; i < 10000; i++){
        a.insert(a.end(),7);
    }; 

	// Get ending timepoint 
	auto stop = high_resolution_clock::now(); 

	// Get duration. Substart timepoints to 
	// get durarion. To cast it to proper unit 
	// use duration cast method 
	auto duration = duration_cast<milliseconds>(stop - start); 

	cout << "Time taken by function: "
		<< duration.count()/1000.0 << " seconds" << endl; 

	return 0; 
} 
