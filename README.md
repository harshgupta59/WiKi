# WiKi

## About
• Created a comprehensive blog web application enabling users to perform CRUD operations on posts, along with search functionality, and featuring a sidebar showcasing random posts.\
• Implemented user authentication functionalities including login, logout, registration, password reset, and profile management features such as updating username and profile picture with image compression capabilities

## Steps for running the application
### 1.Open django_project folder->django_project->settings.py  
	<br/>
	a.Enter your Gmail Account in EMAIL_HOST_USER(gmail-id should be two-step Authenticated for security, here to act as admin id which sends password reset link to users of WIKI.) <br/>
	b.Enter your Gmail App Password in EMAIL_HOST_PASSWORD
	
### 2.Open the whole django_project Folder in VSCODE terminal.

### 3.set terminal directory to django_project folder directory.

### 4.type following in terminal 
	python manage.py makemigrations 
	python manage.py migrate
	python manage.py runserver 

	
### 5.open the localhost in any webbrowser.



