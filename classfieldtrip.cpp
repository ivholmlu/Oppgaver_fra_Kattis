#include <iostream>
#include <string>
#include <algorithm>

int main(){

    std::string s1;
    std::string s2;
    std::cin >> s1;
    std::cin >> s2;
    std::string comb = s1 + s2;
    std::sort(comb.begin(), comb.end());
    std::cout << comb << '\n';
}