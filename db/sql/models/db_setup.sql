INSERT INTO users (id, role_name, email, first_name, password)
VALUES (1, "Admin", "admin@example.com", "AdminFirstName", "replace_password"), (2, "User", "user@example.com", "UserFirstName", "replace_password"), (3, "Admin", "jamie@jnetworks.ovh", "Jamie", "replace_password");
||
UPDATE users
SET profile_image = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/baby-yoda-grogu-boba-fett-1643800811.jpg"
WHERE id = 3;
||
INSERT INTO tickets (id, creator_id, assignee_id, team, issue_type, issue_desc, time_created, time_updated)
VALUES (1, 3, 3, "IT", "Software", "Description of issue 1", "2023-04-01 00:00:00", "2023-04-01 00:00:00"), (2, 3, 3, "IT", "Hardware", "Description of issue 2", "2023-04-03 00:00:00", "2023-04-03 00:00:00"), (3, 1, 1, "HR", "Hardware", "Description of issue 3", "2023-03-03 00:00:00", "2023-03-03 00:00:00");