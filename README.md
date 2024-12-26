
# BrandVis-AI Powered Brand Visibility Analysis
Brands need to understand how their logo appears and performs in video content across various platforms.  Traditional methods of manual analysis are time-consuming, inefficient, and prone to human error. This limits the ability to gain accurate and timely insights into brand visibility, measure the effectiveness of marketing campaigns, and protect brand reputation.

This project addresses this problem by developing an automated system for detecting and analyzing brand logos in video content using the YOLOv8 object detection model. By providing accurate and efficient logo detection, the project aims to enable:

1. **Automated Brand Tracking**: Automatically monitor video content for the presence of specific logos, eliminating the need for manual analysis.
2. **Quantitative Brand Visibility Metrics**: Measure key metrics such as logo appearance count, screen time, and prominence to gain a comprehensive understanding of brand visibility.
3. **Efficient Content Analysis**: Facilitate efficient analysis of large volumes of video data, enabling faster and more informed decision-making.
4. **Potential for Real-time Applications**: Explore the possibility of real-time logo detection in live video streams for immediate insights and applications.

By addressing these needs, the project aims to empower brands with a powerful tool for managing their presence in the ever-growing landscape of video content.



## 

**TECHNOLOGIES USED:** YOLOv8, OpenCV, Python, Streamlit, Pandas, Numpy, Ultralytics.



## Roadmap

1. **Define Project Goals:**
   - Objective: Build an application to detect and count logo appearances in video frames.
   - Deliverables: Web application for uploading videos, detecting logos, and displaying performance metrics.

2. **Data Collection and Preparation:**
   - Identify sources for collecting video and image datasets containing logos.
   - Label the dataset to annotate logos for training the detection model.
   - Split the dataset into training, validation, and testing sets.

3. **Set Up Environment:**
   - Install necessary libraries (Streamlit, OpenCV, Ultralytics, etc.).
   - Prepare the development environment with Python and the required dependencies.

4. **Model Selection and Training:**
   - Select YOLOv8 for logo detection.
   - Train the YOLO model on the prepared dataset to detect specific logos.
   - Save the trained model weights (e.g., `best.pt`).

5. **Develop Core Functionality:**
   - Integrate the YOLO model for inference in the application.
   - Write code to upload and process video frames using OpenCV.
   - Implement logic for detecting logos in each frame and counting appearances.

6. **Build the User Interface:**
   - Create an intuitive interface using Streamlit.
   - Add sidebar options for selecting functionalities (e.g., "Use Model," "Performance Details").
   - Display results in real-time (video frames with bounding boxes and logo counts).

7. **Performance Metrics and Visualization:**
   - Include performance metrics from model training (e.g., precision, recall, mAP@0.5).
   - Display performance-related images from the training phase.

8. **Testing and Debugging:**
   - Test the application with various video formats and content.
   - Handle edge cases (e.g., unsupported file types or empty video frames).

9. **Optimization:**
   - Optimize the application for speed and resource efficiency.
   - Ensure the application handles large videos without significant performance degradation.

10. **Deployment:**
   - Host the application using Streamlit sharing, Heroku, or any other suitable platform.
   - Test deployment for stability and performance.


## Run Locally

Download the Project and extract them and keep with other available files

```bash
  Install other necessary folders and dataset using https://drive.google.com/file/d/1ZmpfWJ3KGeNqPf4U787kifF3HA6fYo4Z/view?usp=sharing
```

Load on the VSCode

```bash
  Activate the virtual environment in the terminal under the saved directory
.venv/Scripts/activate
```

Note: If facing issue while activating virtual environment

```bash
1.Search Windows Powershell on Windows and run on administrator, use commands: Get-ExecutionPolicy, 
then use commands: Set-ExecutionPolicy RemoteSigned, put Y and go ahead. Try to enter virtual environment again.
2.Use this code directly to create and start the new virtual environment:
(remember that u should be in the right directory before execution)
	rm -r .venv
	python -m venv .venv
	.\.venv\Scripts\activate  
	pip install -r requirements.txt
 
```

Run the streamlit file when in virtual environment

```bash
  streamlit run streamlit_app.py
```


## Authors

- [@ShivamSB14](https://www.github.com/ShivamSB14)

