document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const tasksList = document.getElementById('tasks');

    // Load tasks when the page loads
    loadTasks();

    // Event listener for form submission
    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const description = document.getElementById('description').value;

        // Send POST request to create a new task
        const response = await fetch('http://127.0.0.1:5000/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description })
        });

        if (response.ok) {
            const task = await response.json();
            addTaskToList(task);
            taskForm.reset();
        } else {
            const error = await response.json();
            alert(error.error);
        }
    });

    // Function to load tasks from the backend
    async function loadTasks() {
        const response = await fetch('http://127.0.0.1:5000/tasks');
        const tasks = await response.json();
        tasks.forEach(task => addTaskToList(task));
    }

    // Function to add a task to the task list
    function addTaskToList(task) {
        const li = document.createElement('li');
        li.innerHTML = `
            ${task.description} (Category: ${task.category})
            <button onclick="startTask(${task.id})">Start</button>
            <button onclick="stopTask(${task.id})">Stop</button>
            <button onclick="getTaskSummary(${task.id})">Summary</button>
        `;
        tasksList.appendChild(li);
    }

    // Function to start a task
    window.startTask = async function (taskId) {
        const response = await fetch(`http://127.0.0.1:5000/tasks/${taskId}/start`, { method: 'POST' });
        if (!response.ok) {
            const error = await response.json();
            alert(error.error);
        }
    }

    // Function to stop a task
    window.stopTask = async function (taskId) {
        const response = await fetch(`http://127.0.0.1:5000/tasks/${taskId}/stop`, { method: 'POST' });
        if (!response.ok) {
            const error = await response.json();
            alert(error.error);
        }
    }

    // Function to get a task summary
    window.getTaskSummary = async function (taskId) {
        const response = await fetch(`http://127.0.0.1:5000/tasks/${taskId}/summary`);
        if (response.ok) {
            const summary = await response.json();
            alert(`Task: ${summary.description}\nDuration: ${summary.duration}\nCategory: ${summary.category}`);
        } else {
            const error = await response.json();
            alert(error.error);
        }
    }
});
