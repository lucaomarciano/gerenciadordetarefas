// Adicionar confirmação ao excluir tarefas
document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            const confirmDelete = confirm('Tem certeza que deseja excluir esta tarefa?');
            if (!confirmDelete) {
                event.preventDefault(); // Cancela a ação de exclusão
            }
        });
    });

    // Destacar tarefas concluídas
    const taskItems = document.querySelectorAll('.list-group-item');
    taskItems.forEach(item => {
        const isCompleted = item.querySelector('.btn-success').textContent.trim() === 'Undo';
        if (isCompleted) {
            item.style.textDecoration = 'line-through';
            item.style.backgroundColor = '#d4edda'; // Verde claro
        }
    });

    // Alterar dinamicamente o botão de conclusão
    const completeButtons = document.querySelectorAll('.btn-success');
    completeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const listItem = button.closest('.list-group-item');
            const isCompleted = button.textContent.trim() === 'Complete';

            if (isCompleted) {
                button.textContent = 'Undo';
                listItem.style.textDecoration = 'line-through';
                listItem.style.backgroundColor = '#d4edda'; // Verde claro
            } else {
                button.textContent = 'Complete';
                listItem.style.textDecoration = 'none';
                listItem.style.backgroundColor = ''; // Remove o estilo
            }
        });
    });
});
