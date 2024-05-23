CREATE TABLE enshu.transport
(date Date,
 seq INT,
 departure VARCHAR(20),
 arrival VARCHAR(20),
 via VARCHAR(20),
 amount INT,
 PRIMARY KEY(date, seq) 
);
