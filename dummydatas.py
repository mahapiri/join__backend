from django.contrib.auth.models import User
from contacts_app.models import Contact
from tasks_app.models import Task, Subtask, Category

from django.contrib.auth.models import User

u1 = User(username="isabelle@gmail.com", email="isabelle@gmail.com", first_name="Isabelle", last_name="Schneider")
u1.set_password("Hallo123@")
u1.save()

u2 = User(username="tom.hartmann@gmail.com", email="tom.hartmann@gmail.com", first_name="Tom", last_name="Hartmann")
u2.set_password("Hallo123@")
u2.save()

u3 = User(username="leonie.mueller@gmail.com", email="leonie.mueller@gmail.com", first_name="Leonie", last_name="Müller")
u3.set_password("Hallo123@")
u3.save()

u4 = User(username="amir.khan@gmail.com", email="amir.khan@gmail.com", first_name="Amir", last_name="Khan")
u4.set_password("Hallo123@")
u4.save()

u5 = User(username="sophie.meier@gmail.com", email="sophie.meier@gmail.com", first_name="Sophie", last_name="Meier")
u5.set_password("Hallo123@")
u5.save()

c1 = Contact(name="Max Mustermann", email="max@mustermann.de", phone="076 524 895 4")
c1.save()
c2 = Contact(linked_user=u1)
c2.save()
c3 = Contact(linked_user=u2)
c3.save()
c4 = Contact(name="Julia Berger", email="julia.berger@example.com", phone="079 213 457 8", color="--green")
c4.save()
c5 = Contact(linked_user=u5)
c5.save()

k1 = Category(name="User Story", color="red")
k1.save()
k2 = Category(name="Bugfix", color="orange")
k2.save()
k3 = Category(name="Refactoring", color="blue")
k3.save()
k4 = Category(name="Feature Request", color="green")
k4.save()
k5 = Category(name="Design Task", color="purple")
k5.save()

t1 = Task(title="1. Aufgabe", description="Beschreibung der ersten Aufgabe", due_date="2025-03-12", prio="medium", status="to_do", category=k1)
t1.assigned_contacts.add(c1)
t1.save()

t2 = Task(title="2. Aufgabe", description="Beschreibung der zweiten Aufgabe", due_date="2025-03-15", status="in_progress", assigned_contacts=c2, category=k2)
t2.save()

t3 = Task(title="3. Aufgabe", description="Beschreibung der dritten Aufgabe", due_date="2025-03-18", prio="low", status="await_feedback", assigned_contacts=c3, category=k3)
t3.save()

t4 = Task(title="4. Aufgabe", description="Beschreibung der vierten Aufgabe", due_date="2025-03-20", prio="medium", assigned_contacts=c4, category=k4)
t4.save()

t5 = Task(title="5. Aufgabe", description="Beschreibung der fünften Aufgabe", due_date="2025-03-22", prio="urgent", status="in_progress", assigned_contacts=c5, category=k5)
t5.save()

s1 = Subtask(task=t1, subtask="Erste Subtask", is_completed=True)
s1.save()

s2 = Subtask(task=t2, subtask="Zweite Subtask", is_completed=False)
s2.save()

s3 = Subtask(task=t3, subtask="Dritte Subtask", is_completed=False)
s3.save()

s4 = Subtask(task=t4, subtask="Vierte Subtask", is_completed=True)
s4.save()

s5 = Subtask(task=t5, subtask="Fünfte Subtask", is_completed=False)
s5.save()