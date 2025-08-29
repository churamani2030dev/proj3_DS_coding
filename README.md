# proj3_DS_coding
Employee Events Dashboard Project
This project is a dashboard to visualize employee events and assess potential risks.

Project Setup
Clone the repository:
!git clone https://github.com/udacity/dsnd-dashboard-project
%cd dsnd-dashboard-project
Set up a virtual environment and install dependencies:
!python -m venv .venv
!source .venv/bin/activate # Windows: .venv\Scripts\activate
!pip install -r requirements.txt
# Note: python-package/requirements.txt caused an error, review if needed.
# !pip install -r python-package/requirements.txt
Install nice-to-have packages:
!pip install -q pytest pyngrok
Running the Dashboard
To run the dashboard application, execute the following command from the project root directory:bash !PYTHONPATH=$PYTHONPATH:. python report/dashboard.py

Note: There was an IndentationError in the report/dashboard.py file during a previous execution attempt. This needs to be resolved for the dashboard to run correctly.

Testing
You can run the project tests using pytest:bash !pytest -q

Note: Currently, the test execution shows "no tests ran". This might indicate an issue with test discovery or configuration.

Accessing the Dashboard (via ngrok)
If you have ngrok set up and an auth token configured (e.g., as a Colab secret), you can expose the dashboard to the internet. However, the attempt to get the ngrok auth token failed in the notebook.python !pip install -q pyngrok from pyngrok import ngrok from google.colab import userdata

