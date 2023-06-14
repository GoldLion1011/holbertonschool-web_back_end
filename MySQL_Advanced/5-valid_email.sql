-- task 5: Trigger that resets attr valid_email if attr email is changed
CREATE TRIGGER reset_valid_email AFTER UPDATE ON users
FOR EACH ROW
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
```
