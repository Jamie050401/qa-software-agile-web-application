INSERT INTO role (name)
VALUES ("User"), ("Admin");
||
INSERT INTO user (id, role_name, email, first_name, password)
VALUES (1, "Admin", "testAdmin@email", "TestAdmin", "replace_password"), (2, "User", "test@email", "Test", "replace_password");