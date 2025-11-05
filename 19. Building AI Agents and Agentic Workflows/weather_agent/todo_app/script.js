let todos = []; 
const app = document.getElementById('app'); 
function renderTodos() { 
    app.innerHTML = '<ul>' + todos.map((todo, index) => `
    <li>${todo} <button onclick='removeTodo(${index})'>Delete</button>
    <button onclick='editTodoPrompt(${index})'>Edit</button>
    </li>`).join('') + '<form id=\'addTodoForm\' onsubmit=\'event.preventDefault(); addTodo();\'><input type=\'text\' id=\'newTodo\' placeholder=\'Add new todo\'/><button type=\'submit\'>Add</button></form></ul>';
} 

function addTodo() { 
    const newTodo = document.getElementById('newTodo').value; 
    if (newTodo.trim()) { 
        todos.push(newTodo); 
        document.getElementById('newTodo').value = ''; 
        renderTodos(); 
    }
}

function removeTodo(index) { 
    todos.splice(index, 1); 
    renderTodos();
}

function editTodoPrompt(index) { 
    const newTodo = prompt('Edit Todo:', todos[index]); 
    if (newTodo !== null) { 
        todos[index] = newTodo; renderTodos(); 
    }
} 

renderTodos(); 
