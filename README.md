# Cam - Sudoku

## YOLO-based object detection
* Detect Sudoku grid in image using object detector.
* Pass the cropped Sudoku grid to extract smaller boxes that contain the digits.
* Pass the digit boxes to a simple CNN for digit detection.
* Create & display virtual generated Sudoku grid.
* Solve and display the solved grid.

## Sub-Modules

### Data-Set Creation
* Image Downloader
* Image Annotation GUI
* Image Augmentation

### CNN Model Data Flow
* Grid Cell creation
* Keras-TensorFlow model
* IOU, NMS, Bounding Box creation
* Confidence Scoring
* Scoring Metric

### Train
* Loss Function
* Training script

### Test/Production
