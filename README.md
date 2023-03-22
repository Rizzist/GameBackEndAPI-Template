# GameBackEndAPI-Template
This is a template that can be used with the UE4 GraphQL Plugin in order to make a near complete backend for your videogame. A few steps are involved in setting this up.

## Step 1: Setting up your settings file*s*
On both your settings.py and your settings_dev.py, do the following:
A: Generate a secret key for your django app
![image](https://user-images.githubusercontent.com/12385263/227036543-17631723-369a-4e04-8052-148f9df5bb3d.png)
B: Setup your PostgresSQL Database. If you are using CPanel, you must follow a special format where the servername is part of the name of the postgres database
![image](https://user-images.githubusercontent.com/12385263/227036741-590b38e3-f8a5-472a-b221-c1ef2cf4fe96.png)
C: *SERVER ONLY* Set your static root and media root based on your server name
![image](https://user-images.githubusercontent.com/12385263/227036993-21924e14-7997-46b0-8a62-c1a972bb2496.png)
D: *ONLY IF YOU HAVE SETUP SMPT* Set up your smtp at the end of the settings files
![image](https://user-images.githubusercontent.com/12385263/227037151-e19f4697-e296-4e8d-85e3-fc0996dcec9f.png)
E: *ONLY WHEN LAUNCHING TO PRODUCTION* Change the settings file from the default one (settings_dev.py) to the server one (settings.py)
![image](https://user-images.githubusercontent.com/12385263/227037366-ca5e33ca-26a0-4153-9e1e-872370985a3b.png)

## Step 2: Uploading to your Provider (I use CPanel, steps shows below)
A: Upload your files and create a python app in the directory you uploaded. Make sure to copy the CMD command for step 2
![image](https://user-images.githubusercontent.com/12385263/227038278-4576cf0f-c135-405d-8798-3296c7d738a9.png)
B: Go to your terminal and paste the CMD Command. Then type the following:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py collectstatic
- python manage.py runserver
This will finish your server setup. 
C: Lastly check your url www.*MyURL*.com/graphql/ if it is working, success! If not, ask ChatGPT or google it bro 



