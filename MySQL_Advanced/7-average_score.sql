-- task 7: creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE average_score FLOAT;
    SET average_score := (
        SELECT AVG(score) FROM corrections WHERE user_id = user_id);
    INSERT INTO AverageScoreForUser (user_id, average_score)
    VALUES (user_id, average_score);
END //
