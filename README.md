# Time Tracker

A simple time tracking tool for tracking tasks and summarizing time spent on each activity. Built with Python (Flask) for the backend and HTML/CSS/JavaScript for the frontend, it includes AI-powered task categorization for enhanced productivity.


## Features

- **Time Tracking**: Start and stop tracking time for a task.
- **Task Summary**: Provide a summary of tracked time for each task.
- **AI Categorization**: Categorize tasks based on their descriptions using a simple AI model.


## Setup

### Backend

1. **Create Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

2. **Install Requirements**:
    ```bash
    pip install -r backend/requirements.txt
    ```

3. **Run the Flask App**:
    ```bash
    python backend/app.py
    ```

**Warning**: If you encounter an sqlite3 module error, install the SQLite development libraries and recreate your virtual environment:

    ```bash
    sudo apt-get update
    sudo apt-get install libsqlite3-dev

# Recreate the virtual environment
    deactivate
    rm -rf venv
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt 

### Frontend

1. **Open `index.html`** in your browser to use the frontend.

## Usage

1. **Create Task**:
   - Enter the task description and click `Create Task`.
2. **Start Task**:
   - Click `Start` to begin tracking time for a task.
3. **Stop Task**:
   - Click `Stop` to end tracking time for a task.
4. **Task Summary**:
   - Click `Summary` to get a summary of tracked time and category of the task.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
