# Battle-Buddy
## 5E Dungeons and Dragons Game Masters Assistant 

Dungeons and Dragons is the most well known table top RPG, over the years new editions have become more inclusive and an audiance has grown to a player base of over 13.7 million. With the influx of new players game masters are in short supply and often run multiple games. Becoming a game master requires a large investment of mental energy and pre planning. Becoming a new  game master is intemidating.  a Game Master must, create a compelling naritive to engage players,  organize play and turn order, and track complex battle simulations, provide judgement rulelings.
Traditionaly this would be done by cross referencing a serries of books and hastily scrawled notes.

Battle buddy is suite of features designed to remove barriers to inclusive gaming and assist Game Masters.  
- Traditional rule books can are heavy and physicaly encombering 
- Cross refereinceing of physical books creates a User Hostil expereince and sensory overload or Information saturation. 
- Encounters contain numerous variables and turn orders that may be difficult to track. 



### Functionality:


#### Offline Libary: 
- An augument to physical books Battle Buddy comes preloaded with a starter pack of monsters and the ability to add new monsters. 
- This libary is searchable or explorable and is intended for offline play. 
- Monsters may be added to a collection to make them easily accesable for a particular campaign or world setting.



#### Features: Turn Tracker
 - Ordered initive tracker keeps track of all encounter participants and helps keep Game masters organized and Players engaged and ready. 
- Battle log allows for turn tracking 
- Status tracker

- Status board:tracks health and status of combatants:


#### Battle resolution
- amount of xp 
- randomly generated rewards

### Stretch Goals:

#### Personality and Tactics:
- randomly generated battle stratagys for each monster. 

#### Quick reference:
- A quick reference for some of the most commonly referenced and forgoten combat rules such as deathsaves, sneak atack, prone, 


 
## libaries
 Django
 Vue
 Python
 
 
 
 
 ## Data Model


  ##### monster: Monster is a  catch all term for enemy 
  Encounter: exists of players place holders, allies and monsters and revelent information. 
  

  
 
##### monster: Monster is a  catch all term for enemy  
index: '',
name: '',
size:"",
type:"",
subtype:"",
alignment:"",
armor_class:0,
hit_points:0,
hit_dice:0,
speed:0,
strength:0,
dexterity:0,
constitution:0,
intelligence:0,
wisdom:0,
charisma:0,
proficiencies:[],
damage_vulnerabilities:[],
damage_resistances:[],
damage_immunities:[],
condition_immunities:[],
senses:[],
languages:[],
special_abilities:[],
actions:[],
challenge_rating: '0',
url: '', 
notes:"
prefered_tactics:

 
 
##### Encounter.
battle_name:[],
initive_order:[],
combatants:[];
initiave:[];
turn:[];
status tracking:;


  
 
 ## Schedule
 
 #### June 28 
 Pre Planning
 
 
 #### June 30 ##### Monster data structure
 - local Json storage from API cache
 - add custom monsters
 - add remove edit monster
- auto generated monster profile pages
 - pagination
 
 
 #### July2 battle instances
 - add remove from combat
 - initive tracking

 
 #### July 6 play testing
 - add remove health
 - add/ remove notes
 
 #### July 9 turn actions:
 - add a status,

####  July 12
- battle resolution 
- personality system

#### July 16 Deadline
 
 ### Design Goals
 
 - Buttons should mimic physical buttons and have a tactile expereince
 - Buttons should be large enough to allow for a touch screen expereince. 
 - Battle will be single page expereince that can be saved and returned to at any time. 
 
 
