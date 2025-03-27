This project presents an intelligent parking management system utilizing computer vision to
detect parking space availability in real time. By processing a video feed, the system
dynamically identifies whether parking spaces in a designated zone are free or occupied. The
zones are pre-defined by the user and stored for persistent monitoring. The system uses image
processing techniques, such as Gaussian blur and adaptive thresholding, to identify available
spaces. The goal of this project is to improve parking efficiency, reduce the time spent
searching for parking, and offer a scalable solution adaptable to various parking structures.

Introduction :
The increasing demand for parking space in urban areas has created significant challenges in
managing parking spaces effectively. Traditional systems, which rely on manual monitoring,
are often inefficient, leading to wasted time and resources. This project proposes a solution
using computer vision to automate parking space management. By processing a real-time
video feed, the system detects whether parking spaces are occupied or free, tracking
availability across designated zones. This dynamic system offers the potential to minimize
time spent searching for parking, improve user experience, and optimize the utilization of
parking spaces.

The proposed work focuses on integrating zone-based parking management with dynamic
space availability tracking using real-time video feeds. The novelty of the system lies in its
combination of multiple zones with customized tracking and displaying available spaces in
real time. The unique approach involves using a pixel-counting method in pre-defined zones
to detect free spaces, while the interactivity feature allows the manual addition and removal
of zones based on user input.
Additionally, the system is designed to be scalable for deployment in various parking areas,
adaptable to different parking layouts, and capable of operating under different environmental
conditions, making it more versatile than existing solutions.
Methodology with Diagram :
Methodology Overview:
Step 1: Define parking zones on an image or video feed using a user interface. Zones
are saved in a pickle file for persistent storage.
Step 2: Capture a real-time video feed using a camera.
Step 3: Process the captured video feed to identify parking spaces using image
processing techniques such as Gaussian blur, adaptive thresholding, and median blur.
Step 4: Count the non-zero pixels in each parking space to determine if it's occupied
or free.
Step 5: Display real-time parking space status and zone-wise availability
