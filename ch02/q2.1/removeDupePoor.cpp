#include <list>

#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"

template<typename T, typename A>
void removeDupe(std::list<T, A> &inList)
{
    auto cur = inList.begin();
    auto end = inList.end();
    while(cur != end) {
        auto value = *cur;
        ++cur;
        end = std::remove_if(cur, end,
                       [value](auto i){return i == value;});
    }
    inList.erase(end, inList.end());
}

TEST_CASE("remove duplications", "[removeDupe]")
{
    std::list<int> l1{1, 2, 1, 2, 3, 3};
    std::list<int> expect1{1, 2, 3};
    removeDupe(l1);
    CHECK(l1 == expect1);
}

