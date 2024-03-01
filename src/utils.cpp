#include "utils.hpp"

// Additional function to write results to a CSV file for further analysis
void writeResultsToCSV(const std::string &filename, double ttcLidar, double ttcCamera, int frameID, int numLidarPoints, float xmin, float xw, float yw) {
    std::ofstream outFile(filename, std::ios::app);
    
    // Check if we need to write the header (i.e., if the file is currently empty)
    bool writeHeader = (outFile.tellp() == 0);
    if (writeHeader) {
        outFile << "FrameID,TTC_Lidar,TTC_Camera,NumLidarPoints,xmin,xw,yw\n";
    }
    
    // Write data for the current frame
    outFile << frameID << "," << ttcLidar << "," << ttcCamera << "," << numLidarPoints << "," << xmin << "," << xw << "," << yw << "\n";
}