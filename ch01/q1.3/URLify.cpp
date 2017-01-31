#include <string>
#include <algorithm>

#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"

std::string& URLify(std::string &url)
{
    auto len = url.length();
    for (auto c : url)
        if (c == ' ')
            len += 2;

    auto loc = url.length() - 1;
    auto newLoc = len - 1;
    url.resize(len);

    for (; loc >= 0; --loc) {
        if (loc == newLoc)  // no space left
            break;

        if (url[loc] == ' ') {
            newLoc -= 2;
            url.replace(newLoc--, 3, "%20");
        } else {
            url[newLoc--] = url[loc];
        }
    }

    return url;
}

TEST_CASE("spaces replaced by %20", "[URLify]")
{
    std::string str = "Mr John Smith";
    REQUIRE(URLify(str) == "Mr%20John%20Smith");

    str = "  Mr John";
    REQUIRE(URLify(str) == "%20%20Mr%20John");

    str = "Mr John  ";
    REQUIRE(URLify(str) == "Mr%20John%20%20");
}

