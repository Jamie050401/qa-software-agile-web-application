INSERT INTO user (id, role_name, email, first_name, password)
VALUES (1, "Admin", "admin@example.com", "Name", "replace_password"), (2, "User", "user@example.com", "Name", "replace_password"), (3, "Admin", "jamie@jnetworks.ovh", "Jamie", "replace_password");
||
UPDATE user
SET profile_image = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/baby-yoda-grogu-boba-fett-1643800811.jpg"
WHERE id = 3;