#ifndef utils_hpp
#define utils_hpp

#include <fstream>
#include <vector>

void writeResultsToCSV(const std::string &filename, double ttcLidar, double ttcCamera, int frameID, int numLidarPoints, float xmin, float xw, float yw);

#endif