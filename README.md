# API_Mekorot

## Intro
This program is HIT project for load files from mekorot API service.
Used for loading data to local DB.
config.json (not in the repository due to saftey issues) includes key, Mekorot url and data folder (for possible changes).
This file is private and will not load to Git.
Raw data will be in 'Data' folder for different usage.
For duplicating and loading more then 1 system duplicate this project and change the key (every key for different system). 

## How It Works
This is an implementation to Realiteq.pdf attached to this Repo.
The workflow is:
- Get history data by this order: 
  1. Get all subnodes exist.
  2. For each subnode get the history data by the time period from config.json (default is 1 hour).
  3. Write all the data to the folder as csv file with unique file name.

History data will be taken:
1. Searches for last update ("lastUpdate" key) in config file.
2. If not exist/ contains None, get the history data by the time period key from config.
3. If exist, take from the lastUpdate value with the time period (only if not higher then current time).
###* TIME ON THE SEVER MUST BE ACCURATE!

## Help
This project is only for HIT usage but given as a open source.
If changes needed you are welcome to clone the project and use by your own.
