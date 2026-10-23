# VFSTR Campus Search Assistant

## Project Overview

The VFSTR Campus Search Assistant is an AI Mini-Capstone project designed to help students find information about campus facilities through natural-language queries.

The system uses keyword-based query understanding, TF-IDF vectorization, and cosine similarity to identify relevant campus information and display search results with source links.

## Features

* Search campus information using questions written in natural language.
* Search across 11 campus information categories.
* Use keyword matching to identify relevant topics.
* Rank results using TF-IDF and cosine similarity.
* Display relevant information and source links.
* Provide a web interface built with HTML, CSS, and Flask.
* Display a message when no matching information is found.

## Technologies Used

* Python
* Flask
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity
* HTML
* CSS

## Campus Information Categories

1. Green Campus
2. Administrative Block
3. Hostel
4. Cafeteria
5. Medical Facility
6. Transport
7. Library
8. Campus Safety
9. Banking
10. Internet and Network
11. Sports

## Project Structure

```text
CampusSearchAssistant/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Open the project folder

```bash
cd CampusSearchAssistant
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open the website

Visit:

http://127.0.0.1:5000

Keep the terminal running while using the application.

## Current Project Status

The basic search engine and local web interface have been implemented. Testing, validation of source information, and further improvements are ongoing.

## Limitations

* Search results depend on the available campus dataset and recognized keywords.
* The system may not understand every possible question or paraphrase.
* Displayed information should be verified against official university sources.
* A locally running website is not publicly accessible until deployed.

## Future Improvements

* Expand and validate the campus information dataset.
* Improve query understanding and search ranking.
* Add more campus-related information.
* Improve usability and accessibility.
* Deploy the application for public testing.

## Project Purpose

This project demonstrates the application of information retrieval techniques and web development to campus information search.

**Project:** Intelligent Search Assistant for Campus Information with Query Understanding and Ranking

**Project Type:** AI Mini-Capstone
