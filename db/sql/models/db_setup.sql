INSERT INTO role (id, name)
VALUES (1, "User"), (2, "Admin");
||
INSERT INTO user (id, role_id, email, first_name, password)
VALUES (1, 2, "testAdmin@email", "TestAdmin", "replace_password"), (2, 1, "test@email", "Test", "replace_password");