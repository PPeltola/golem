# User stories

## Regular user

1. A new user wants to register into the system, and does so by using the reigster functionality:
```
INSERT INTO account (username, password) 
VALUES ('Joe', 'joespassword');
```

2. The user is then redirected to the user index page which queries all of their campaigns:
```
SELECT * FROM Campaign 
WHERE account_id = joes_id;
```

Here joes_id is his account id. The page also queries the counts of active characters in his campaigns:
```
SELECT Campaign.id, COUNT(Character.id) 
FROM Campaign 
LEFT JOIN Character ON Character.campaign_id = Campaign.id 
WHERE Campaign.account_id = joes_id 
GROUP BY Campaign.id;
```

It also queries all of his active characters:
```
SELECT Campaign.id, Campaign.name, Character.id, Character.name FROM Character 
LEFT JOIN Campaign ON Campaign.id = Character.campaign_id 
WHERE (Character.active = 1 AND Character.account_id = joes_id)
```

The index page then shows the characters to Joe by campaign thorugh some python dictionary magic.

3. The user wants to see the campaigns they could create a character in:
```
SELECT campaign.id AS campaign_id, campaign.name AS campaign_name, campaign.account_id AS campaign_account_id, campaign.starting_points AS campaign_starting_points FROM campaign;
```
4. The user selects a campaign and goes to the campaign's user index page. It lists all their characters in the campaign:
```
SELECT Character.id, Character.name FROM Character WHERE (Character.active = 1 AND Character.account_id = joes_id AND Character.campaign_id = campaignid);
```

This queries all their active characters, campaignid being the campaign's id. It also queries their inactive characters separately:
```
SELECT Character.id, Character.name FROM Character WHERE (Character.active = 0 AND Character.account_id = joes_id AND Character.campaign_id = campaignid);
```

5. The user wants to create a new campaign themselves:
```
INSERT INTO campaign (name, account_id, starting_points) VALUES ("Joe's cowboy adventure", joes_id, 100);
```

6. Bill wants to create a character in Joe's campaign:
```
INSERT INTO character (name, active, account_id, campaign_id, strength, dexterity, intelligence, health, unspent_points, total_points, strength_spent, dexterity_spent, intelligence_spent, health_spent) VALUES ('Bob', 1, bills_id, joes_campaigns_id, 10, 10, 10, 10, 100, 100, 0, 0, 0, 0);
```

7. Bill wants to check his new character out:
```
SELECT character.id AS character_id, character.name AS character_name, character.active AS character_active, character.account_id AS character_account_id, character.campaign_id AS character_campaign_id, character.strength AS character_strength, character.dexterity AS character_dexterity, character.intelligence AS character_intelligence, character.health AS character_health, character.unspent_points AS character_unspent_points, character.total_points AS character_total_points, character.strength_spent AS character_strength_spent, character.dexterity_spent AS character_dexterity_spent, character.intelligence_spent AS character_intelligence_spent, character.health_spent AS character_health_spent 
FROM character 
WHERE character.id = bills_characters_id
```

As a side note, I don't really know why SQLalchemy makes so long queries, they are not the prettiest sight :p

8. Bill modifies his character's stats:
```
UPDATE character SET intelligence = 11, unspent_points = 80, intelligence_spent = 20 WHERE character.id = bills_character_id;
```

9. And then suddenly Bill realizes that roleplaying is not for him, and first he deactivates his character:
```
UPDATE character SET active = 0 WHERE character.id = bills_character_id
```

10. And then deletes it:
```
DELETE FROM character WHERE character.id = bills_character_id;
```

## Admin

1. The admin wants to see the admin view, which then loads all skills:
```
SELECT skill.id AS skill_id, skill.name AS skill_name, skill.attribute AS skill_attribute, skill.difficulty AS skill_difficulty, skill.description AS skill_description 
FROM skill;
```

2. And then makes a new one:
```
INSERT INTO skill (name, attribute, difficulty, description) VALUES ("Stealth", "DX", 2, "How good you are at going unnoticed");
```
