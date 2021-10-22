

#           Tablo kurma


CREATE TABLE assignment1
(
Sender_ID int,
Receiver_ID int,
Amount int,
Transaction_Date date
)
;



### tablo doldurma


SELECT	*
FROM	assignment1;
INSERT INTO assignment1 (Sender_id, Receiver_id, Amount, Transaction_date)
VALUES (10, 100, 1000, '2021-10-22')
;


SELECT	*
FROM	assignment1;
INSERT INTO assignment1 (Sender_id)
VALUES (10),(11),(12),(13) # tek seferde birine veri verme



# Droplama

DROP TABLE assignment1;


