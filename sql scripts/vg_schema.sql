CREATE TABLE IF NOT EXISTS video_game_sales (
  ID            INT   PRIMARY KEY NOT NULL ,
  Name          TEXT              NOT NULL ,
  Platform      TEXT              NOT NULL ,
  Year          DATE              NOT NULL ,
  Genre         TEXT              NOT NULL ,
  Publisher     TEXT              NOT NULL ,
  NA_Sales      DECIMAL(10,5)     NOT NULL ,
  EU_Sales      DECIMAL(10,5)     NOT NULL ,
  JP_Sales      DECIMAL(10,5)     NOT NULL ,
  Other_Sales   DECIMAL(10,5)     NOT NULL ,
  Global_Sales  DECIMAL(10,5)     NOT NULL
);


