#include <bits/stdc++.h> 
using namespace std; 
void revers(string& str)   // Swap character starting from two cornrs 
{ 
	int n = str.length(); 
	for (int i = 0; i < n / 2; i++) 
		swap(str[i], str[n - i - 1]); 
}  
int main() 
{ 
	string str = "Hacktoberfest"; 
	revers(str); 
	cout << str; 
	return 0; 
} 
//Jinesh31082001
