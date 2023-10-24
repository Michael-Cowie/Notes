#include <iostream>

#include "youtube_searcher.hpp"

int main(int argc, char* argv[]) {
    // Check if there are enough command-line arguments
    if (argc < 2) {
        std::cerr << "You did not provide me anything to search." << std::endl;
        return 1;
    }

    // Combine the command-line arguments to form the search query
    std::string searchQuery;
    for (int i = 1; i < argc; i++) {
        searchQuery += argv[i];
        if (i < argc - 1) {
            searchQuery += " ";
        }
    }

    search_youtube(searchQuery);

    return 0;
}