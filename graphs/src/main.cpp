#include "GraphResourceFactory.h"
#include "GraphServiceSettingsFactory.h"
#include "GraphService.h"

#include <iostream>
#include <vector>
#include <sstream>

// Helper function to deserialize the adjacency matrix
std::vector<std::vector<int>> deserializeMatrix(const std::string& serializedMatrix) {
    std::vector<std::vector<int>> matrix;
    std::istringstream iss(serializedMatrix);
    std::string row;
    
    while (std::getline(iss, row, '\n')) {
        std::istringstream row_iss(row);
        std::vector<int> row_vector;
        std::string cell;
        
        while (std::getline(row_iss, cell, ',')) {
            if (!(cell != "[" && cell != "]"))
            row_vector.push_back(std::stoi(cell));
        }
        
        matrix.push_back(row_vector);
    }
    
    return matrix;
}

int main() {
    // Read the serialized adjacency matrix from Python backend
    std::string serializedMatrix;
    std::getline(std::cin, serializedMatrix);

    // Deserialize the matrix
    std::vector<std::vector<int>> adjacencyMatrix = deserializeMatrix(serializedMatrix);

    // Process the adjacency matrix (add your C++ logic here)

    // Optionally, send back the result to Python backend using cout



    // Restbed
    auto resource_factory = make_shared<GraphResourceFactory>();
    auto setting_factory = make_shared<GraphServiceSettingsFactory>();
    GraphService service (resource_factory, setting_factory);

    service.start();


    return 0;
}
