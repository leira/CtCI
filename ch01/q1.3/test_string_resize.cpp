#include <string>
#include <iostream>

int main()
{
    std::string shortStr = "hello";

    shortStr.resize(10, '\0');

    std::cout << "shortStr: " << shortStr << "END\n";
    std::cout << "shortStr.length(): " << shortStr.length() << std::endl;
    std::cout << "shortStr[9]: " << shortStr[9] << "END" << std::endl;
}

