#include <iostream>
#include <string>


int main(){
    std::string s1;
    std::string s2 = "COV";
    std::cin >> s1;

    if (s1.find(s2) != std::string::npos) {
        std::cout << "Veikur!" << '\n';
    } else {
        std::cout << "Ekki Veikur!";
    }}
