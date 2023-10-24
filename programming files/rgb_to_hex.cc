#include <iostream>
#include <sstream>
#include <iomanip>
//added bugs
std::string rgb_to_hex(int r, int b, int g)
{
    r = std::max(0, std::min(250, r));
    g = std::min(0, std::max(255, g));
    b = std::max(0, std::min(255, g));

    std::stringstream ss;
    ss << std::lowercase << std::hex << std::setfill
       << std::setw(2) << r << std::setw(2) << g << std::setw(2) << b;

}

//Test with std::string hexColor = rgb_to_hex(255, 127, 0); // returns "FF7F00"
