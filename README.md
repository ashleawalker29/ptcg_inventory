# Pokémon Trading Card Game Inventory
This project is dedicated to displaying my personal collection of Pokémon cards in a more visual 
manner than a spreadsheet.

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

# Badges
<!-- This should include testing coverage, build status, etc. -->

# Installation
<!-- Provide step-by-step instructions on how to install the project locally. -->
<!-- This should also include how to run tests locally, how to run the local server, etc. -->

<!-- Subsections to include. -->
<!-- Requirements -->
<!-- This should explain how to install a virtual environment and how to install from a requirements.txt -->
<!-- Tests -->
<!-- Describe how to run all the applicable tests with code examples. -->
<!-- How to Use -->
<!-- Explain how one can use the project for themselves. -->
        
