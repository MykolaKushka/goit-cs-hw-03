from faker import Faker
import psycopg2

# Підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname="task_manager",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

fake = Faker()

# Заповнення таблиці users
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Заповнення таблиці tasks
cursor.execute("SELECT id FROM users")
user_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM status")
status_ids = [row[0] for row in cursor.fetchall()]

for _ in range(30):
    title = fake.sentence(nb_words=3)
    description = fake.text()
    status_id = fake.random.choice(status_ids)
    user_id = fake.random.choice(user_ids)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id)
    )

conn.commit()
cursor.close()
conn.close()
