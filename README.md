# Measuring-Litter-Cleanups

This project should take machine learning datasets as input and produce maps of where the objects within them are located. As long as EXIF metadata is included, the coordinates can be extracted. While this is limited by both the precision and accuracy. Precision varies accross devices, ranging from smartphones all the way to proper surveying equipment. 

For example:

![image](https://user-images.githubusercontent.com/39971693/205541629-9d265fdd-cec9-496f-abb3-277264610fcb.png)

Our images have 14 signifigant digits which are carried over to the extracted JSON 
```"longitude": -121.42020277777779, "latitude": 38.559355555555555```.
However, the accuracy isn't as easy to calculate, because many factors in the surrounding environment  affect signal strength. For the first test which was in a parking garage, mapping them showed multiple detections outside of the boundary. Previous research suggests we can expect a range of 5 - 20 meters, with some areas producing lots of outliers. A parking garage serves as a good first example, because the accuracy should be more difficult than the main usage which will be outside. It also highlights the limited scales that meaningful conclusions can be drawn. We will be covering a larger area next time but a grouping strategy could be used to cluster the trash to the correct buildings accross campus.

![Alt text](https://github.com/julianofhernandez/Measuring-Litter-Cleanups/blob/main/Parking%20Structure%20Clean%20up%2011-26/PSII%20Clean%20Up%20Map.png)

TODO: 
- [ ] Use clustering to predict which images correlate with each building
- [ ] Extract the OSM shapes of the building into the same coordinate space
- [ ] Encode actual building image in extracted JSON
- [ ] Verify OSM against satellite images
- [ ] Collect images of trash cans
