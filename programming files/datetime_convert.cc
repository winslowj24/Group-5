#include <iostream>
#include <iomanip>
#include <sstream>
#include <chrono>

int main()
{
    // Create a string containing date
    std::string date_str = "2022-03-17 10:45:30";

    // Create structure containing date and time elements
    std::tm date_obj = {};

    // Create input string called ss containing the date time string
    std::istringstream ss(date_str);

    // Input the time from the reference pointing to the date time object and input it into ss
    ss >> std::get_time(&date_obj, "%Y-%m-%d %H:%M:%S");

    // Create a string stream called formatted_date_ss
    std::stringstream formatted_date_ss;

    // Put the string from date object into the string stream
    formatted_date_ss << std::put_time(&date_obj, "%m/%d/%Y %H:%M:%S");

    // Convert string stream object to a string
    std::string formatted_date = formatted_date_ss.str();

    // Print the string containing formatted date
    std::cout << formatted_date << std::endl;

    return 0;
}
