# Final Project README

## Introduction
This README provides a comprehensive overview of the methods and processes implemented in this project to meet the criteria set forth in the Project Rubric specifications.

## FP.1 Match 3D Objects

Implemented the `matchBoundingBoxes` method, located at `camFusion.cpp`, that takes both the previous and the current data frames as input and outputs the IDs of the matched regions of interest with the highest number of keypoint correspondences.

## FP.2 Compute Lidar-based TTC

Computed the time-to-collision for all matched 3D objects using only Lidar measurements. The method calculates the TTC based on Lidar points using the median of the detected points in the cloud, in a robust way to handle outliers.

## FP.3 Associate Keypoint Correspondences with Bounding Boxes

Prepared TTC computation based on camera measurements by associating keypoint correspondences to bounding boxes. The method in `matching2D.cpp` adds keypoint correspondences to the "kptMatches" property of bounding boxes and removes outliers.

## FP.4 Compute Camera-based TTC

Computed the TTC for all matched 3D objects using keypoint correspondences. The method computes the TTC using keypoint correspondences from matched bounding boxes in a statistically robust way.

## FP.5 Performance Evaluation 1

For this section, a function was implemented to write relevant data to a csv file, `analysis/results.csv` and a python script (`analysis/analysis.py`) was created to create interesting visualizations on top of this data. This way, it was able to analyze the performance of the Lidar sensor TTC estimates and provide explanations for implausible values.

The graph indicates instances where the Lidar-based TTC estimates are not plausible (marked in red). These instances correspond to frame IDs where the number of Lidar points is significantly lower, potentially indicating outlier data affecting the TTC calculation.

![TTC Lidar Changes Between Consecutive Frames](/images/results1.png)

As can be seen in the graph, the first 4 frames have increasing TTC measurements, and all of them have also increasing xw (width of the vehicle, in the X-Axis - front of the sensor). Since the width is increasing, the median of the points in data gets pushed further from the sensor, which in turn increases the value of the computed TTC. At frame 5, the xw value decreases and the TTC also decreases. This same pattern appears for other frames, such as 10, 11 and 12.

## FP.5 Performance Evaluation 2

Similarly, for this section a function was implemented to write relevant data to a csv file, `analysis/results_desc.csv`. Each row corresponds to a pair Detector-Descritpr, with each TTC calculate for all given frames. The last two columns correspond to the mean and the standard deviation of these values.

The file shows many Detector-Descriptor pairs with inf/-inf TTC values for some frames, which indicates some kind of misbehavior or problem, caused by distances too low and consequent divisions with denominators close to zero.

By analyzing the results, one can conclude that the best combinations are those with Shi-Tomasi as the Detector method. Among these, the best Detector-Descriptor pair was the Shi-Tomasi/Freak. It provided consistent values and a very low standard deviation.

## Conclusion

The methods and analyses performed in this project highlight the robustness and functionality of the code in computing time-to-collision metrics using both Lidar and camera data. Each rubric point has been addressed with clear evidence and methodologies that fulfill the project's success criteria.
