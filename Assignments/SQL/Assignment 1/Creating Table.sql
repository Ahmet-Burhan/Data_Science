CREATE SCHEMA my_schema;
go

CREATE TABLE my_schema.transactions (
	Sender_ID INT IDENTITY (1, 1) PRIMARY KEY,
	Receiver_ID INT NOT NULL,
	Amount INT NOT NULL,
	Transaction_Date Date NOT NULL
);