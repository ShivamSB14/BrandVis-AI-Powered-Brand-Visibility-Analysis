To execute load the project on VS Code
1.Open your terminal or command prompt.
2.Navigate to your project directory: Use the cd command to navigate to the Logo_Detection folder.
3.Activate your virtual environment: If you're using one, activate it (e.g., .venv\Scripts\activate).
4.Run the app: Execute the following command: streamlit run streamlit_app.py

if having issues in entering virtual env.
1.Search Windows Powershell on Windows and run on administrator, use commands: Get-ExecutionPolicy, then use commands: Set-ExecutionPolicy RemoteSigned, put Y and go ahead. Try to enter virtual env. again
2. use this code directly to create and start the new virtual environment: (remember that u should be in the right directory before execution)
	rm -r .venv
	python -m venv .venv
	.\.venv\Scripts\activate  
	pip install -r requirements.txt

