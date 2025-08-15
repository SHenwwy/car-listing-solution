Car Listing Assistant
This application provides a simple web interface for users to upload a car image and a text description. It then uses an AI model to extract structured data from the text and sends the listing details via email.

Setup and Installation
Follow these steps to set up and run the project on your local machine.

Prerequisites
Python 3.8+

. Clone the Repository
First, clone the repository to your local machine:

git clone <your_repository_url>
cd <repository_name>

Navigate to the project folder in the terminal.Then run> python -m venv venv.
On Windows (Command Prompt) run> .\venv\Scripts\activate
On macOS and Linux> source venv/bin/activate.
Then After activating, the terminal prompt will change to show (venv), and they can proceed with the pip install -r requirements.txt.
and final step to run the> streamlit run app.py


IMPORTANT NOTE: 
In the .env file please open it and there will be a variable named>> RECIPIENT_EMAIL.
DON'T FORGET TO CHANGE THIS GEMAIL TO YOUR GEMAIL AND KEEP THE REST THE SAME
