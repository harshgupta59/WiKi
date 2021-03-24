# WiKi_django

1.Open django_project folder->django_project->settings.py 
	a.Enter your Gmail Account in EMAIL_HOST_USER(gmail-id should be two-step Authenticated for security, here to act as admin id which sends password reset link to users of WIKI.)
	b.Enter your Gmail App Password in EMAIL_HOST_PASSWORD
	
2.Open the whole django_project Folder in VSCODE terminal.

3.set terminal directory to django_project folder directory.

4.type following in terminal
	a.python manage.py makemigrations
	b.python manage.py migrate
	c.python manage.py runserver.
	
5.open the localhost in any webbrowser.(or  http://127.0.0.1:8000/ in webbrowser)

