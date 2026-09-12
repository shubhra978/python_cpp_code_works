#include <bits/stdc++.h>
using namespace std;
vector <pair<int,int>> find_pair(vector <int> &list_pair, int target){
    vector <pair<int,int>> result;
    int left=0;
    int right = list_pair.size()-1;
    
    while(left < right){
        int sum_target = list_pair[left] + list_pair[right]; // target sum
        
        if(sum_target == target){ //function to check if sum is matching
            result.push_back({list_pair[left], list_pair[right]}); //pushing pairs in to the vector array
            left++;
            right--;
        }
        else if(sum_target< target){
            left++;
        }
        else{
            right--;
        }
    }
    return result;
    
}


int main() {
	vector <int> my_list = {5,4,7,2,3,5,1};
	
	int target = 8;
	
	sort(my_list.begin(),my_list.end());	//sorting the list
	
	vector <pair<int,int>> pairs = find_pair(my_list,target);
	
	if(pairs.size()==0){
	    cout<< "not found";
	}
	else{
	   cout<< "pairs found"<< endl;
	    for (int i=0; i < pairs.size(); i++){
	        cout<< pairs[i].first << "+" <<pairs[i].second << endl;
	    }
	}
	
    
	
}
