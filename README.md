# Pokémon Trading Card Game Inventory
This project is dedicated to displaying my personal collection of Pokémon cards in a more visual 
manner than a spreadsheet.

## Status
![Master Workflow](https://github.com/ashleawalker29/ptcg_inventory/workflows/Master%20Workflow/badge.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/ashleawalker29/ptcg_inventory/badge)](https://www.codefactor.io/repository/github/ashleawalker29/ptcg_inventory)
[![codecov](https://codecov.io/gh/ashleawalker29/ptcg_inventory/branch/master/graph/badge.svg)](https://codecov.io/gh/ashleawalker29/ptcg_inventory)

# Description
A production version of the project's webpage can be found at 
[https://ptcg-inventory.herokuapp.com/](https://ptcg-inventory.herokuapp.com/).

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
1 normal, reverse foil, or holo foil card so that they are differentiated from unowned cards.

#### Schema
The local database table's schema is as follows:

##### Local Table `card_inventory_cards`
| Column Name      | Column Type           | Column Use                                                             |
|------------------|-----------------------|------------------------------------------------------------------------|
| id               | integer               | Row ID for the database table, the primary key.                        |
| card_number      | text                  | The card's associated card number in a set.                            |
| card_name        | text                  | The card's name.                                                       |
| quantity_normal  | integer               | The number of normal cards owned.                                      |
| quantity_reverse | integer               | The number of reverse foil cards owned.                                |
| quantity_holo    | integer               | The number of holo foil cards owned.                                   |
| set_code_id      | character varying(10) | Foreign Key connecting to `set_code` from table `card_inventory_sets`. |

##### Local Table `card_inventory_sets`

| Column Name | Column Type            | Column Use                                                                      |
|-------------|------------------------|---------------------------------------------------------------------------------|
| set_name    | character varying(255) | The set's name. This is a unqiue value and also the Primary Key for this table. |
| set_code    | character varying(10)  | The set's associated short-hand code.                                           |
| max_cards   | integer                | The max number of cards that can be found within the set.                       |

##### Example `card_inventory_cards` and `card_inventory_sets` Rows

###### `card_inventory_cards`
| id | card_number |            card_name            | quantity_normal | quantity_reverse | quantity_holo | set_code_id |
|----|-------------|---------------------------------|-----------------|------------------|---------------|-------------|
|  1 | 8           | Machamp                         |               0 |                0 |             1 | base1       |

###### `card_inventory_sets`
| set_name | set_code | max_cards |
|----------|----------|-----------|
| Base     | base1    |       102 |

These example rows indicate that the collection includes one (1) holographic copy of a Machamp card with the set code of
`base1` within the first table, `card_inventory_cards`. This `base1` value is mapped to the set named Base that has the
maximum of 102 cards within the second table, `card_inventory_sets`.

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

## Testing
To run all tests locally, run the following command:
``` bash
$ python3 manage.py test
```
