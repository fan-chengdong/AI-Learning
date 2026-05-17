class TodoApp {
    constructor() {
        this.tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        this.currentFilter = 'all';
        this.init();
    }

    init() {
        this.taskInput = document.getElementById('taskInput');
        this.addBtn = document.getElementById('addBtn');
        this.taskList = document.getElementById('taskList');
        this.taskCount = document.getElementById('taskCount');
        this.clearCompleted = document.getElementById('clearCompleted');
        this.filterBtns = document.querySelectorAll('.filter-btn');

        this.bindEvents();
        this.render();
    }

    bindEvents() {
        this.addBtn.addEventListener('click', () => this.addTask());
        this.taskInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.addTask();
        });

        this.clearCompleted.addEventListener('click', () => this.clearCompletedTasks());

        this.filterBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.filterBtns.forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                this.currentFilter = e.target.dataset.filter;
                this.render();
            });
        });
    }

    addTask() {
        const text = this.taskInput.value.trim();
        if (!text) return;

        this.tasks.push({
            id: Date.now(),
            text: text,
            completed: false
        });

        this.taskInput.value = '';
        this.save();
        this.render();
    }

    toggleTask(id) {
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            task.completed = !task.completed;
            this.save();
            this.render();
        }
    }

    deleteTask(id) {
        this.tasks = this.tasks.filter(t => t.id !== id);
        this.save();
        this.render();
    }

    clearCompletedTasks() {
        this.tasks = this.tasks.filter(t => !t.completed);
        this.save();
        this.render();
    }

    getFilteredTasks() {
        switch (this.currentFilter) {
            case 'active':
                return this.tasks.filter(t => !t.completed);
            case 'completed':
                return this.tasks.filter(t => t.completed);
            default:
                return this.tasks;
        }
    }

    render() {
        const filteredTasks = this.getFilteredTasks();

        if (filteredTasks.length === 0) {
            this.taskList.innerHTML = '<li class="empty-message">暂无任务</li>';
        } else {
            this.taskList.innerHTML = filteredTasks.map(task => `
                <li class="task-item ${task.completed ? 'completed' : ''}" data-id="${task.id}">
                    <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''}>
                    <span class="task-text">${this.escapeHtml(task.text)}</span>
                    <button class="delete-btn">删除</button>
                </li>
            `).join('');
        }

        const activeCount = this.tasks.filter(t => !t.completed).length;
        this.taskCount.textContent = `${activeCount} 个待办任务`;

        this.bindTaskEvents();
    }

    bindTaskEvents() {
        this.taskList.querySelectorAll('.task-item').forEach(item => {
            const id = parseInt(item.dataset.id);

            item.querySelector('.task-checkbox').addEventListener('change', () => {
                this.toggleTask(id);
            });

            item.querySelector('.delete-btn').addEventListener('click', () => {
                this.deleteTask(id);
            });
        });
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    save() {
        localStorage.setItem('tasks', JSON.stringify(this.tasks));
    }
}

new TodoApp();