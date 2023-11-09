# Github Searcher App

This project consists of a Django API for searching GitHub users and repositories, and a React app that interacts with the API to display search results.

## Django API

### Installation

Loom Demo Link: https://www.loom.com/share/a3cddcd67693464795efd10d9f57d3ec

1. Clone the repository:

   ```bash
git clone https://github.com/meghaSingh1/github_searcher.git

1. Navigate to the project directory:

cd github-searcher-api

2. Create a virtual environment (recommended):

python -m venv venv

3. Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt
sudo apt-get install redis

Start Redis:

sudo systemctl restart redis.service

5. Navigate to github django project

cd github_search_project
python manage.py makemigrations
python manage.py migrate

6. Run the development server:

python manage.py runserver

The API should be running at http://127.0.0.1:8000/.

API Endpoints
/github_search/api/search (POST): Search for GitHub users or repositories.
/github_search/api/clear-cache (POST): Clear Redis Cache 

React App

React App name: githhub-search-reactapp

1. Navigate to the react app directory:
cd github-search-reactapp

2. Install dependencies:
npm install

3. Start the React app:
npm start

The React app should be running at http://localhost:3000/.

Usage:

1. Access the React app in your browser.
2. Enter the search query and select the search type (Users or Repositories).
3. View the search results.

