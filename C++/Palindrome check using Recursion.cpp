#include <iostream>
using namespace std;

bool isPalindrome(string &str, int start, int end)
{
    if (start >= end)
        return true;
    else
        return (str[start] == str[end]) && isPalindrome(str, start + 1, end - 1);
}

int main()
{
    string str;
    cin >> str;
    if (isPalindrome(str, 0, str.length() - 1))
        cout << "Yes";
    else
        cout << "No";
    return 0;
}

//It has time complexity as O(n) and space complexity of O(n)
