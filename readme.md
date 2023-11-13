# Github Searcher App

This project consists of a Django API for searching GitHub users and repositories, and a React app that interacts with the API to display search results.

## Django API

### Installation

Loom Demo Link: https://www.loom.com/share/a3cddcd67693464795efd10d9f57d3ec

1. Clone the repository:

```bash
git clone https://github.com/meghaSingh1/github_searcher.git
```

1. Navigate to the project directory:

```bash
cd github-searcher-api
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
```
3. Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
sudo apt-get install redis
```
Start Redis:

```bash
sudo systemctl restart redis.service
```

5. Navigate to github django project

```bash
cd github_search_project
python manage.py makemigrations
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

The API should be running at http://127.0.0.1:8000/.

API Endpoints
```bash
/github_search/api/search (POST): Search for GitHub users or repositories.
/github_search/api/clear-cache (POST): Clear Redis Cache 
```
React App

React App name: githhub-search-reactapp

1. Navigate to the react app directory:

```bash
cd github-search-reactapp
```
2. Install dependencies:
```bash
npm install
```
3. Start the React app:
```bash
npm start
```
The React app should be running at http://localhost:3000/.

Usage:

1. Access the React app in your browser.
2. Enter the search query and select the search type (Users or Repositories).
3. View the search results.

