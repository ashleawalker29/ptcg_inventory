# Pokémon Trading Card Game Inventory
This project is dedicated to displaying my personal collection of Pokémon cards in a more visual 
manner than a spreadsheet.

## Status
![Master Workflow](https://github.com/ashleawalker29/ptcg_inventory/workflows/Master%20Workflow/badge.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/ashleawalker29/ptcg_inventory/badge)](https://www.codefactor.io/repository/github/ashleawalker29/ptcg_inventory)

# Description
A production version of the project's webpage can be found at 
[https://ptcg-inventory.herokuapp.com/](https://ptcg-inventory.herokuapp.com/)

My personal collection of cards is visually displayed on the homepage via the Pokémon card sets 
(X & Y, Sun & Moon, etc.). 

## Features
### Homepage
[Production Link](https://ptcg-inventory.herokuapp.com/)

An overview of my personal collection is displayed on this page, organized by the Pokémon card sets. 
Each set has three bubbles that give a quick glance into the number of cards owned in that set. The 
bubbles, from left to right on each set, represent the total number of normal, reverse foil, and holo 
foil cards.

### Subpages
[Production Link for Base Set](https://ptcg-inventory.herokuapp.com/Base/)

There is a subpage for each set that includes a table of owned cards. As of publishing this README, the 
tables do not include cards that are unowned. In the future, these subpages should visually display the 
collection using the cards' images instead of the tables. 

### Local Database
The local database holds all of the information for cards that I currently own. Each entry has at least
1 normal, reverse foil, or holo foil card.

#### Schema
The local database table's schema is as follows:

##### Local Table `card_inventory_cards`
| Column Name      | Column Type      | Column Use                                      |
|------------------|------------------|-------------------------------------------------|
| id               | integer          | Row ID for the database table, the primary key. |
| set_name         | enum e_set_name  | The card's associated set name.                 |
| card_number      | text             | The card's associated card number in a set.     |
| card_name        | text             | The card's name.                                |
| card_type        | enum e_card_type | The card's type.                                |
| quantity_normal  | integer          | The number of normal cards owned.               |
| quantity_reverse | integer          | The number of reverse foil cards owned.         |
| quantity_holo    | integer          | The number of holo foil cards owned.            |

`set_name` and `card_type` are of type ENUM. These ENUMs hold their own unique values to prevent typos 
and promote consistency.

##### ENUM `e_set_name`
This ENUM has 116 total different values that can be used for `set_name` within the `card_inventory_cards` 
database table. These are all of the Pokémon card sets published as of writing this README. Some of these 
set names include `Base`, `Fossil`, `Base Set 2`, etc.

##### ENUM `e_card_type`
This ENUM has 35 total different values that can be used for `card_type` within the `card_inventory_cards` 
database table. These are all of the types of Pokémon cards published as of writing this README. Some of 
these types include `Grass`, `Fire`, `Water`, etc.

##### Example `card_inventory_cards` Row

| id | set_name | card_number | card_name | card_type | quantity_normal | quantity_reverse | quantity_holo |
|----|----------|-------------|-----------|-----------|-----------------|------------------|---------------|
| 1  | Base     | 1/102       | Alakazam  | Pyschic   | 1               | 0                | 0             |

This example row indicates that the collection includes one (1) normal copy of a Psychic Alakazam card from
the Base set.

# Installation
Clone this repository locally. Navigate to the root directory and then run through the following steps.

## Virtual Environment
Running this Django project will require setting up a virtual environment (venv). This is a tool that helps to keep this project's dependencies separate from your other projects.

To create a venv, run the following from the root directory:
``` bash
$ sudo pip3 install virtualenv
$ virtualenv ptcg_env
```
This creates a venv named `ptcg_env`.

### Activate the Virtual Environment
To actually use the venv, activate it using the following command:
``` bash
$ source ptcg_env/bin/activate
```

### Deactivate the Virtual Environment
To leave the venv, deactivate it using the following command:
``` bash
$ deactivate
```

## Requirements
All requirements are included in `requirements.txt`. Within your venv run the following:
``` bash
$ pip3 install -r requirements.txt
```
This installs the required packages within your venv.

## Testing
To run all tests locally, run the following command:
``` bash
$ python3 manage.py test
```

## Local Database
You will need your own local database to connect to the django framework. To set this up, run the following commands:
``` sql
$ psql
$ CREATE DATABASE ptcg_inventory;
$ CREATE USER <username> WITH PASSWORD <password>;
$ GRANT ALL PRIVLEGES ON DATABASES ptcg_inventory TO <username>;
$ \q
$ python3 manage.py migrate
```
