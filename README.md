# Pokémon Trading Card Game Inventory
This project is dedicated to displaying my personal collection of Pokémon cards in a more visual 
manner than a spreadsheet.

# Description
A production version of the project's webpage can be found at 
[https://ptcg-inventory.herokuapp.com/](https://ptcg-inventory.herokuapp.com/)

My personal collection of cards is visually displayed on the homepage via the Pokémon card sets 
(eg. X & Y, Sun & Moon, etc.). 

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

##### Local Table card_inventory_cards
``` sql
ptcg_inventory=# \d card_inventory_cards

                                   Table "public.card_inventory_cards"
      Column      |    Type     | Collation | Nullable |                     Default                      
------------------+-------------+-----------+----------+--------------------------------------------------
 id               | integer     |           | not null | nextval('card_inventory_cards_id_seq'::regclass)
 set_name         | e_set_name  |           | not null | 
 card_number      | text        |           | not null | 
 card_name        | text        |           | not null | 
 card_type        | e_card_type |           | not null | 
 quantity_normal  | integer     |           |          | 
 quantity_reverse | integer     |           |          | 
 quantity_holo    | integer     |           |          | 
Indexes:
    "card_inventory_cards_pkey" PRIMARY KEY, btree (id)
```

`set_name` and `card_type` are of type ENUM. These ENUMs hold their own unique values to prevent typos and promote consistency.

##### ENUM `e_set_name`
This ENUM has 116 total different values that can be used for `set_name` within the `card_inventory_cards` database table. The following is a snippet of the values:

``` sql
ptcg_inventory=# 
    SELECT t.typname, e.enumlabel, e.enumsortorder 
    FROM pg_type t, pg_enum e
    WHERE t.oid = e.enumtypid AND t.typname = 'e_set_name'
    ORDER BY e.enumsortorder;
    
  typname   |          enumlabel          | enumsortorder 
------------+-----------------------------+---------------
 e_set_name | Wizards Black Star Promos   |             1
 e_set_name | Base                        |             2
 e_set_name | Jungle                      |             3
 e_set_name | Fossil                      |             4
 e_set_name | Base Set 2                  |             5
 e_set_name | Team Rocket                 |             6
 ...        | ...                         |           ...
 (116 rows)
```

##### ENUM `e_card_type`
This ENUM has 35 total different values that can be used for `card_type` within the `card_inventory_cards` database table. The following is a snippet of the values:
``` sql
ptcg_inventory=# 
    SELECT t.typname, e.enumlabel, e.enumsortorder
    FROM pg_type t, pg_enum e
    WHERE t.oid = e.enumtypid AND t.typname = 'e_card_type'
    ORDER BY e.enumsortorder;
    
   typname   |     enumlabel      | enumsortorder 
-------------+--------------------+---------------
 e_card_type | Grass              |             1
 e_card_type | Fire               |             2
 e_card_type | Water              |             3
 e_card_type | Lightning          |             4
 e_card_type | Psychic            |             5
 ...         | ...                |           ...
 (35 rows)
```

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
        
