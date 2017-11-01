CREATE TABLE IF NOT EXISTS video_game_sales (

  Rank          INT   PRIMARY KEY   NOT NULL ,
  Name          TEXT                NOT NULL ,
  Platform      TEXT                NOT NULL ,
  Year          INT                NOT NULL ,
  Genre         TEXT                NOT NULL ,
  Publisher     TEXT                NOT NULL ,
  NA_Sales      DECIMAL             NOT NULL ,
  EU_Sales      DECIMAL             NOT NULL ,
  JP_Sales      DECIMAL             NOT NULL ,
  Other_Sales   DECIMAL             NOT NULL ,
  Global_Sales  DECIMAL             NOT NULL

);


