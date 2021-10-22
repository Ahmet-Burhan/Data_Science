SELECT	Sender_id, SUM(amount) AS send_amount
FROM	assignment1
GROUP BY Sender_id




SELECT	*
FROM	(
		SELECT	sender_id, SUM(amount) AS send_amount
		FROM	assignment1
		GROUP BY sender_id
		) S
FULL OUTER JOIN	
		(
		SELECT	receiver_id, SUM(amount) AS receive_amount
		FROM	assignment1
		GROUP BY receiver_id
		) R
ON		S.Sender_id = R.receiver_id





SELECT	COALESCE(S.sender_id, R.receiver_id) AS Account_ID,
		COALESCE(R.receive_amount, 0) - COALESCE(S.send_amount, 0) AS Net_Change
FROM	(
		SELECT	sender_id, SUM(amount) AS send_amount
		FROM	assignment1
		GROUP BY sender_id
		) S
FULL OUTER JOIN	
		(
		SELECT	receiver_id, SUM(amount) AS receive_amount
		FROM	assignment1
		GROUP BY receiver_id
		) R
ON		S.Sender_id = R.receiver_id
;