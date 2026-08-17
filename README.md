# AkashDristi

##### AI-powered post-disaster damage mapping and relief prioritization.

## 

###### 

#### AkashDristi Backend:



Backend service for the AkashDristi project.

###### 

###### Requirements:



\- Python 3.13+

\- Git



###### Setup:



From the project root, enter the backend directory:



bash

cd backend





###### AkashDristi Backend:



Backend service for the AkashDristi project.



###### Requirements:



\- Python 3.13+

\- Git



###### Setup:



*From the project root, enter the backend directory:*

cd backend



*Create a Python virtual environment:*

python -m venv .venv



*Activate the virtual environment on Windows:*

.venv\\Scripts\\activate



*Install the backend dependencies:*

pip install -r requirements.txt



*Run the Backend*

*From the backend directory:*

uvicorn src.main:app --reload



*The backend will run at:*

http://127.0.0.1:8000



###### 

###### Health Check:



*The backend provides a health endpoint:*

*GET /health open:*

http://127.0.0.1:8000/health



Expected response:



{

&#x20; "status": "ok"

}





###### API Documentation:



FastAPI provides interactive API documentation at:

http://127.0.0.1:8000/docs



###### Running Tests



*Activate the virtual environment:*

.venv\\Scripts\\activate



*Run the tests:*

pytest

*IMPORTANT*
Important Setup Note: Do not use the .venv folder provided in the repository. Virtual environments contain hardcoded absolute paths that will break on different machines. Always delete it, create a fresh .venv locally using python -m venv .venv, and install dependencies from scratch.








