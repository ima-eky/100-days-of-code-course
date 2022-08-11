# Deploying Your Web Application with Heroku
## Publishing Flask website onto the Internet
- Sign up for a free account on [https://dashboard.heroku.com](https://dashboard.heroku.com)
- Create a new application on Heroku (Leave the region as US )
- Connect Heroku to your GitHub project. Under the Deploy tab, select Connect to GitHub
- Sign in to your GitHub account where your blog project repository exists.
- Click on Enable Automatic Deploys,scrolling further down the page on the deploy pane
- On manual deploys, click on Deploy Branch to deploy for the first time.
- Click View to see your web app(it wouldn't work yet)
  ##### Output expected

![deploying_flask](https://user-images.githubusercontent.com/101118595/184251346-d95a792c-7516-41df-99f9-11b4a1dbeb7f.png)

-You need to install [gunicorn](https://docs.gunicorn.org/en/stable/install.html)
- Add the newly installed package to the requirements.txt file on a new line (gunicorn==<version number>)
- Create a new file in the project top-level folder called Procfile ( and type `web: gunicorn main:app` in file)
- Click View app to see your web app(it should work now)
###  Upgrade SQLite Database to PostgreSQL
- Go to your app's dashboard on Heroku and go to the Resources tab. Then search for Heroku Postgres.
- Next, you will see a popup, keep the free-tier and click Submit. 
- Go to Settings -> Reveal Config Vars
- To connect Postgres Database to app,Update the app config to use "DATABASE_URL" environment variable if provided (for example,os.environ.get("DATABASE_URL",  "sqlite:///blog.db"))
- SQLite is pre-installed for all Python projects but Postgres isn't installed.You'll need to install[https://pypi.org/project/psycopg2-binary/](https://pypi.org/project/psycopg2-binary/) and add new package to requirements.txt
