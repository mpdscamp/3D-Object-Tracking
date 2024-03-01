#ifndef utils_hpp
#define utils_hpp

#include <fstream>
#include <vector>
#include <numeric>
#include <cmath>

void writeResultsToCSV(const std::string &filename, double ttcLidar, double ttcCamera, int frameID, int numLidarPoints, float xmin, float xw, float yw);
std::pair<double, double> computeMeanAndStd(const std::vector<double>& v);

void writeResultsToCSVDesc(const std::string &filename, const std::string &detectorType, 
                       const std::string &descriptorType, const std::vector<double> &ttcCameraValues);

#endif