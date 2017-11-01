CREATE TABLE IF NOT EXISTS ign_reviews (

  ID              INT    PRIMARY KEY    AUTOINCREMENT   NOT NULL ,
  Score_Phrase    TEXT                                  NOT NULL ,
  Title           TEXT                                  NOT NULL ,
  Url             TEXT                                  NOT NULL ,
  Platform        TEXT                                  NOT NULL ,
  Score           DECIMAL                               NOT NULL ,
  Genre           TEXT                                  NOT NULL ,
  Editors_Choice  BOOLEAN                               NOT NULL ,
  Release_Date    DATE                                  NOT NULL

);