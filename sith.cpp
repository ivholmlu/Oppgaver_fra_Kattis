
#include <iostream>
#include <string>

int main() {
    std::string name;
    std::cin >> name;

    int a, b, c;

    std::cin >> a >> b >> c;

    if (a - b >= 0) {
        std::cout << "VEIT EKKI\n";
    } 
    else {
        if (c < 0) {
            std::cout << "jedi\n";
        } else {
            std::cout << "sith\n";
        }
    }

    return 0;
}





