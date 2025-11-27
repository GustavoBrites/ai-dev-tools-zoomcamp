from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import TodoItem

class TodoItemModelTest(TestCase):
    def test_create_todo_item(self):
        todo = TodoItem.objects.create(
            title="Test Task",
            due_date=timezone.now()
        )
        self.assertEqual(todo.title, "Test Task")
        self.assertFalse(todo.is_resolved)
        self.assertIsNotNone(todo.created_at)

    def test_str_representation(self):
        todo = TodoItem.objects.create(
            title="Test Task",
            due_date=timezone.now()
        )
        self.assertEqual(str(todo), "Test Task")

class TodoViewTest(TestCase):
    def setUp(self):
        self.todo = TodoItem.objects.create(
            title="Test Task",
            description="Test Description",
            due_date=timezone.now()
        )

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertTemplateUsed(response, 'todo/home.html')

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo-create'), {
            'title': 'New Task',
            'description': 'New Description',
            'due_date': timezone.now().isoformat()
        })
        self.assertEqual(response.status_code, 302) # Redirects after success
        self.assertEqual(TodoItem.objects.count(), 2)

    def test_todo_update_view(self):
        response = self.client.post(reverse('todo-update', args=[self.todo.pk]), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'due_date': timezone.now().isoformat(),
            'is_resolved': True
        })
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Task')
        self.assertTrue(self.todo.is_resolved)

    def test_todo_delete_view(self):
        response = self.client.post(reverse('todo-delete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TodoItem.objects.count(), 0)

    def test_todo_toggle_view(self):
        response = self.client.get(reverse('todo-toggle', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_resolved)
        
        # Toggle back
        response = self.client.get(reverse('todo-toggle', args=[self.todo.pk]))
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.is_resolved)
