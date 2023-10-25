#include <iostream>
#include <string>


int main(){
    std::string input;
    std::string smiley = ":)";
    std::string frowny = ":(";
    std::getline(std::cin, input);  // Use getline to read the whole line including spaces


    if (input.find(smiley) != std::string::npos) {
        if (input.find(frowny) != std::string::npos){
        std::cout << "double agent";
        return 0;
    } 
    else {
        std::cout << "alive";
        return 0;
        }}
    if (input.find(frowny) != std::string::npos){
        std::cout << "undead";
        return 0;
    }
    else {
        std::cout << "machine";
        return 0;
    }}
