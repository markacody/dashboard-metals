# Data Visualization in Python with Dash

## Set up and Run Project

1. Open in VSCode.
2. Change terminal to bash.
3. Look for (venv) or activate the venv. source/bin/activate
4. Type python app.py in the command line.

## Remove an out-of-sync git folder.

1. rm -rf .git //Remove the folder
2. ls -lah //Verify it's gone.

## Deploy to gcloud

Create a project on Google Cloud: "dashboard-metals." From the command line:

1. gcloud init
2. Select "Create a new configuration"
3. Give the configuation a name: "dashboard-metals"
4. Choose an account
5. Select the project, named above.
6. gcloud app deploy
   The service is created and a .gcloudignore file is added to the directory root automatically.
7. Agree to the service description.
8. Select the region, US-central, 17.
