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

// Function to compute mean and standard deviation
std::pair<double, double> computeMeanAndStd(const std::vector<double>& v) {
    double sum = std::accumulate(v.begin(), v.end(), 0.0);
    double mean = sum / v.size();

    double sq_sum = std::inner_product(v.begin(), v.end(), v.begin(), 0.0,
        [](double const& x, double const& y) { return x + y; },
        [mean](double const& x, double const& y) { return (x - mean) * (y - mean); });
    double stdev = std::sqrt(sq_sum / v.size());

    return {mean, stdev};
}

// Modified function to write results to CSV
void writeResultsToCSVDesc(const std::string &filename, const std::string &detectorType, 
                       const std::string &descriptorType, const std::vector<double> &ttcCameraValues) {
    // Open file
    std::ofstream outFile(filename, std::ios::app);

    // Check if we need to write the header (i.e., if the file is currently empty)
    outFile.seekp(0, std::ios::end); // Move to the end of the file
    bool writeHeader = outFile.tellp() == 0;
    if (writeHeader) {
        outFile << "Detector,Descriptor,";
        for (size_t i = 0; i < ttcCameraValues.size(); ++i) {
            outFile << "Frame_" << i << "_" << i+1 << ",";
        }
        outFile << "Mean,StDev\n";
    }

    // Write detector and descriptor types
    outFile << detectorType << "," << descriptorType << ",";

    // Write TTC values for each frame pair
    for (const auto& ttc : ttcCameraValues) {
        outFile << ttc << ",";
    }

    // Calculate and write mean and standard deviation
    auto [mean, stdev] = computeMeanAndStd(ttcCameraValues);
    outFile << mean << "," << stdev << "\n";

    // Close file
    outFile.close();
}