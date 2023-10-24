#include <iostream>
#include <cstdlib>
#include <string>

#include "youtube_searcher.hpp"
#include "youtube_searcher_utilities.hpp"

#include <boost/regex.hpp>

static bool contains_league_of_legends(const std::string& searchQuery) {
    // Check if the search query contains "League of Legends" or "LoL"
    boost::regex regex("(League of Legends|LoL)", boost::regex::icase); // Case-insensitive search
    return boost::regex_search(searchQuery, regex);
}

void search_youtube(const std::string& searchQuery) {
    // Check if the search query contains "League of Legends" or "LoL"
    if (contains_league_of_legends(searchQuery)) {
        std::cout << "No, quit now!" << std::endl;
        return;
    }

    // Construct the YouTube search URL
    std::string youtubeURL = "https://www.youtube.com/results?search_query=" + searchQuery;

    // Use platform-specific code to open the default web browser
    #ifdef _WIN32 // For Windows
        std::string command = "start " + youtubeURL;
    #elif __APPLE__ // For macOS
        std::string command = "open " + youtubeURL;
    #else // For Linux and other platforms
        std::string command = "xdg-open " + youtubeURL;
    #endif

    int result = std::system(command.c_str());

    // Check if the system command executed successfully
    if (result == 0) {
        std::cout << "YouTube search opened successfully." << std::endl;
    } else {
        std::cerr << "Failed to open YouTube search." << std::endl;
    }
}
