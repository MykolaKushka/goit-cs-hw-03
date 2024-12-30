-- 4.1. Завдання конкретного користувача

SELECT * FROM tasks WHERE user_id = 1;

-- 4.2. Завдання за певним статусом

SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 4.3. Оновлення статусу завдання

UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

-- 4.4. Користувачі без завдань

SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- 4.5. Додавання нового завдання

INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New Task', 'Task description', 1, 1);

-- 4.6. Незавершені завдання

SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- 4.7. Видалення завдання

DELETE FROM tasks WHERE id = 1;

-- 4.8. Користувачі за email

SELECT * FROM users WHERE email LIKE '%@gmail.com';

-- 4.9. Оновлення імені користувача

UPDATE users SET fullname = 'Updated Name' WHERE id = 1;

-- 4.10. Кількість завдань за статусами

SELECT s.name, COUNT(t.id) FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

-- 4.11. Завдання за доменом email

SELECT t.* FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

-- 4.12. Завдання без опису

SELECT * FROM tasks WHERE description IS NULL;

-- 4.13. Завдання у статусі 'in progress'

SELECT u.fullname, t.title FROM users u
JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- 4.14. Кількість завдань для кожного користувача

SELECT u.fullname, COUNT(t.id) AS task_count FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;