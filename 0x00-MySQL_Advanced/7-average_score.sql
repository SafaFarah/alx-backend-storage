-- Create the ComputeAverageScoreForUser stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;
    UPDATE users
    SET average_score = COALESCE(avg_score, 0)
    WHERE id = user_id;
END //

DELIMITER ;
