# Django Starter

Jason's opinionated starting codebase for Django.

To run:
1. Create a virtual environment in the root directory: `python3 -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install the requirements: `pip3 install -r requirements.txt`
4. I included an example app to demonstrate how the Ninja router + UUID models work. You can use this for inspiration, but ultimately should create apps that reflect the use cases you're building. To create your own sub apps, either copy the directory and rename the relevant parts to include the infrastructure for models/routing, or create one from scratch using `python manage.py startapp appname`.
5. Once you create your own subapp (or can test using mine), create your migrations `python manage.py makemigrations`
6. Migrate the database using `python manage.py migrate`. This will create a local sqlite database for development. The django settings are already modified to use postgres on heroku once deployed instead of sqlite.
7. Start the repo using `python manage.py runserver`
8. You can now hit your example API endpoints to see everything in action - visit `localhost:8000/api/v1/brand/brands` to see the example endpoint in action.