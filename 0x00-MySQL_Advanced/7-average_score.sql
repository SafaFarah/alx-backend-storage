-- Create the stored procedure to compute and store the average score for a user
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE num_scores INT DEFAULT 0;
    SELECT SUM(score), COUNT(*)
    INTO total_score, num_scores
    FROM corrections
    WHERE user_id = user_id;
    IF num_scores > 0 THEN
        UPDATE users
        SET average_score = total_score / num_scores
        WHERE id = user_id;
    ELSE
        UPDATE users
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END //
DELIMITER ;
