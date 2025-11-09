from todo.models import Task

print('Создание 3х объектов Task')
print('Готовим список для кверисетов')
tasks = []

print('Создаем кверисеты и добавляем в список')
for i in range(1, 4):
    t = Task(
        title=f"Название {i}-ой задачи",
        description=f"Описание {i}-ой задачи"
    )
    tasks.append(t)

print('Выполняем список кверисетов (эффективно)')
Task.objects.bulk_create(tasks)


print('Получаем все созданные задачи')
all_tasks = Task.objects.all()

for task in all_tasks:
    print(task.pk, task.title, task.description, task.completed, sep=', ')


print('Изменение статуса одной из задач на «Выполнено».')
first_task = Task.objects.all().first()
first_task.completed = True
first_task.save()

print('Проверяем:')
for task in Task.objects.all():
    print(task.pk, task.title, task.description, task.completed, sep=', ')

print('Удаляем другую задачу')
task_for_removing = Task.objects.filter(title='Название 2-ой задачи')
task_for_removing.delete()

print('Проверяем:')
for task in Task.objects.all():
    print(task.pk, task.title, task.description, task.completed, sep=', ')

print('С удовольствием удаляем все задачи')
Task.objects.all().delete()

print('Проверяем:')
for task in Task.objects.all():
    print(task.pk, task.title, task.description, task.completed, sep=', ')