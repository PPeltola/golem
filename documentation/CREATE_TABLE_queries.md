## SQL CREATE TABLE queries
The following tables are present in the current build of GOLEM

```
CREATE TABLE skill (
	id INTEGER NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	attribute VARCHAR(5) NOT NULL, 
	difficulty INTEGER NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(30) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);
CREATE TABLE campaign (
	id INTEGER NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	account_id INTEGER NOT NULL, 
	starting_points INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE character (
	id INTEGER NOT NULL, 
	name VARCHAR(40) NOT NULL, 
	active BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	campaign_id INTEGER NOT NULL, 
	strength INTEGER NOT NULL, 
	dexterity INTEGER NOT NULL, 
	intelligence INTEGER NOT NULL, 
	health INTEGER NOT NULL, 
	unspent_points INTEGER NOT NULL, 
	total_points INTEGER NOT NULL, 
	strength_spent INTEGER NOT NULL, 
	dexterity_spent INTEGER NOT NULL, 
	intelligence_spent INTEGER NOT NULL, 
	health_spent INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (active IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(campaign_id) REFERENCES campaign (id)
);

```
