document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const tasksList = document.getElementById('tasks');

    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const description = document.getElementById('description').value;

        const response = await fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description })
        });

        const task = await response.json();
        addTaskToList(task);
    });

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

    window.startTask = async function (taskId) {
        await fetch(`/tasks/${taskId}/start`, { method: 'POST' });
    }

    window.stopTask = async function (taskId) {
        await fetch(`/tasks/${taskId}/stop`, { method: 'POST' });
    }

    window.getTaskSummary = async function (taskId) {
        const response = await fetch(`/tasks/${taskId}/summary`);
        const summary = await response.json();
        alert(`Task: ${summary.description}\nDuration: ${summary.duration}\nCategory: ${summary.category}`);
    }
});
