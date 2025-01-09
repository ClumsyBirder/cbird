# CBird

## Features

- Asynchronous API with FastAPI
- Asynchronous database operations with SQLAlchemy
- User creation and retrieval endpoints
- Environment variable configuration
- Logging setup

## Requirements

- Python 3.7+
- pip
- virtualenv (recommended)

## Project Structure

```
CBird
├── main.py          # Main application file
├── models.py        # Database models
├── schemas.py       # Pydantic schemas
└── ...
```

## Setup and Installation

1. Clone the repository: `git clone <repository_url>`
2. Create a virtual environment: `python3 -m venv .venv`
3. Activate the virtual environment: `. .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`


## Running the Application

To run the application:

```bash
uvicorn main:app
```

## Development

To run the application in development mode with auto-reload:

```bash
uvicorn main:app --reload
```

This will start the server and automatically restart it when you make changes to the code.

