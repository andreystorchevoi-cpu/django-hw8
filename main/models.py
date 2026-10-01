from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    # Ваши остальные поля модели Category...

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'  # Или 'Category', если требуется жестко совпадение с 'Category'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category_name')
        ]


class Task(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # Поле даты создания
    # Ваши остальные поля модели Task...

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']  # Сортировка по убыванию даты создания
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_task_title')
        ]


class SubTask(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # Поле даты создания
    # Ваши остальные поля модели SubTask...

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']  # Сортировка по убыванию даты создания
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_subtask_title')
        ]
