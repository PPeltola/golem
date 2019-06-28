# The database

The database is currelty as follows:

<img src="https://raw.githubusercontent.com/PPeltola/lel.png">

The skill table isn't related to any other tables at the moment. The idea was for it to be many-to-many related to character, since many skills should exist in the system and multiple characters should be able to be proficient in those skills. Unfortunately I didn't get SQLalchemy's many-to-many relation to work and ran out of time. The database is normalized (unless I understood something wrong).
