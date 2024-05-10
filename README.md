# DDOS_Finder
Welcome to the repository for "DDOS Finder - DDoS Detection and Prevention in IoT Devices (IP Cameras)."

This project is focused on providing a comprehensive software solution to detect and prevent Distributed Denial-of-Service (DDoS) attacks targeting Internet of Things (IoT) devices, particularly IP cameras. Leveraging scalable data ingestion techniques and adaptive machine learning models, the solution achieves high accuracy in detecting and preventing DDoS attacks.

Features:

•	 Scalable data ingestion from diverse IoT devices
•	Adaptive machine learning model for evolving attack patterns
•	High detection accuracy (99.55%) using RandomForestClassifier
•	Real-time telemetry data analysis and visualization
•	Comprehensive classification results and accuracy reports
•	Google Authentication integration via Firebase
•	User-friendly interface using Flask and HTML/CSS

Project Structure:

•	Scalable data ingestion from diverse IoT devices
•	Adaptive machine learning model for evolving attack patterns
•	High detection accuracy (99.55%) using RandomForestClassifier
•	Real-time telemetry data analysis and visualization
•	Comprehensive classification results and accuracy reports
•	Google Authentication integration via Firebase
•	User-friendly interface using Flask and HTML/CSS

--------------------------------------------------------

Installation Instructions:

Clone the repository:
 # git clone https://github.com/Lakiya7/DDOS_Finder.git

Navigate to the project directory:
#  cd ddos-finder

Create and activate a virtual environment:
#  python3 -m venv venv
#  source venv/bin/activate

Install the required Python libraries:
#  pip install -r requirements.txt

Set up Firebase Google Authentication:
#  Create a Firebase project and enable Google Authentication.
#  Download the firebase_config.json file and add it to the project root.

Start the Flask web application:
#  python app.py


Usage Instructions:
1.	Access the Web Application:
  •	Open a web browser and go to http://localhost:5000.
  •	Log in using your Google account via Firebase.
2.	Train the Model:
  •	Navigate to the "Train Model" section to train the DDoS detection model.
  •	Upload telemetry data, and the system will automatically train and save the model.
3.	Detect DDoS Attacks:
  •	Go to the "Detect DDoS" section to analyze new telemetry data.
  •	The system will classify traffic as "BENIGN" or "DDoS."
4.	View Alerts and Reports:
  •	Alerts are generated in real-time for detected DDoS attacks.
  •	Review detailed classification reports and feature importances.
Future Work:
  •	Integrate real-time alerts via email/SMS.
  •	Implement web hosting with No-IP DNS configuration.
  •	Develop a lightweight, hardware-based solution for IP cameras.
  •	Incorporate federated learning and blockchain-backed trust frameworks.

Contributors:
  •	Sasanka M.W.K.L.
  
License: This project is licensed under the MIT License.

