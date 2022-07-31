# Data Visualization in Python with Dash

## Set up project

- Dash looks for css, js, and favicon in a folder called assets.
- templates.py imports Dash stylesheets that can be applied to graphs. In this case, fig.update_layout(template='plotly_dark').

## Run Project

1. Open in VSCode.
2. Change terminal to bash.
3. Look for (venv) or activate the venv. source/bin/activate
4. Type python app.py in the command line.

## Remove an out-of-sync git folder.

1. rm -rf .git //Remove the folder
2. ls -lah //Verify it's gone.

## Set up gcloud

1. Create a project on Google Cloud: "dashboard-metals."
2. Link a billing account.
   NOTE: Everything that follows will fail, if a billing account is not linked, or if too many projects are linked to the billing account.
3. Enable cloud build.

## Deploy to gcloud

From the command line:

1. gcloud init
2. Select "Create a new configuration"
3. Give the configuation a name: "dashboard-metals"
4. Choose an account (associated with your email address)
5. Select the project, named above.
6. gcloud app deploy
   The service is created and a .gcloudignore file is added to the directory root automatically.
7. Agree to the service description.
8. Select the region, US-central, 17.

## Browse app

https://dashboard-metals.uc.r.appspot.com

## Error conditions

The deployment was successful after resolving two errors. The 502 Bad Gateway error is opaque, so checking gcloud error logs for specifice Notices and Errors is essential.

- 502 Bad Gateway => Rename app.py to main.py
  The gcloud default is to look for a file named main.py
- 502 Bad Gateway => Revised app.yaml
  Dash app yamls need to specify handlers: where to find static assets. The entrypoint is also helpful. And for your own advance planning, the service should be specified (because a project can have multiple services.)
  SUCCESS
