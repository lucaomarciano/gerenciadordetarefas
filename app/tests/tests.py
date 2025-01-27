import unittest
from app import app, db
from app.models import Task

class TaskManagerTestCase(unittest.TestCase):
    def setUp(self):
        """Configuração antes de cada teste."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco de dados em memória para testes
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Limpeza após cada teste."""
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        """Testa se a página inicial carrega corretamente."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gerenciador de Tarefas', response.data)

    def test_add_task(self):
        """Testa a adição de uma nova tarefa."""
        response = self.app.post('/add', data={'title': 'Nova Tarefa'})
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.assertIsNotNone(Task.query.filter_by(title='Nova Tarefa').first())

    def test_edit_task(self):
        """Testa a edição de uma tarefa."""
        task = Task(title='Tarefa Original')
        db.session.add(task)
        db.session.commit()
        response = self.app.post(f'/edit/{task.id}', data={'title': 'Tarefa Editada'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.query.get(task.id).title, 'Tarefa Editada')

    def test_delete_task(self):
        """Testa a exclusão de uma tarefa."""
        task = Task(title='Tarefa a Ser Deletada')
        db.session.add(task)
        db.session.commit()
        response = self.app.post(f'/delete/{task.id}')
        self.assertEqual(response.status_code, 302)
        self.assertIsNone(Task.query.get(task.id))

    def test_mark_as_complete(self):
        """Testa marcar uma tarefa como concluída."""
        task = Task(title='Tarefa Não Concluída', completed=False)
        db.session.add(task)
        db.session.commit()
        response = self.app.post(f'/complete/{task.id}')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.query.get(task.id).completed)

if __name__ == '__main__':
    unittest.main()
