#include <list>
#include <unordered_set>

#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"

template<typename T, typename A>
void removeDupe(std::list<T, A> &inList)
{
    std::unordered_set<T> values;

    auto it = inList.begin();
    while(it != inList.end()) {
        if (values.find(*it) != values.end()) {
            it = inList.erase(it);
        } else {
            values.insert(*it);
            ++it;
        }
    }
}

TEST_CASE("remove duplications", "[removeDupe]")
{
    std::list<int> l1{1, 2, 1, 2, 3, 3};
    std::list<int> expect1{1, 2, 3};
    removeDupe(l1);
    CHECK(l1 == expect1);
}

