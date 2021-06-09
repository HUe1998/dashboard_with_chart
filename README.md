# Dashboard Template using Django

Using Django as backend, two views are provided:
* Login View: Login using username and password. This is matched with User Objects in the SQLite Database. If the user credentials matches, redirect to the dashboard view.
* create a dashboard displaying various charts using Chart.js and also provide a button to automatically generate and save the main body of the dashboard.

On local deployment, go to localhost:8000/login to access login view. After login, you will be redirected to localhost:8000/dashboard

Live site is deployed at: </br>
https://chart-dashboard-django.herokuapp.com/login