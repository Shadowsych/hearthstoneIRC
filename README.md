# Hearthstone IRC Chat Command
- This program was created for "Polite_Sociopath" (Black Desert Online NA) for $100 USD

# Technologies
- Twitch API: https://dev.twitch.tv/api
- Twitch Chat OAuth Password Generator: https://twitchapps.com/tmi/
- TMI Javascript (Node): https://www.tmijs.org/
- IRC Inputs: https://github.com/hzoo/TwitchPlaysX

# Design Specifications
1.) Accurately read in twitch.tv chat commands when a streamer runs the bot. So let's say a  
streamer types in !Position_1, then the bot would click wherever Position_1 is on the streamers   
screen.  

2.) The bot should be able to click on places on the screen based on what the twitch user types in.  
It doesn't matter where the bot clicks, as long as it is easily modifiable so that the bot could be  
changed to click in several different locations.  


3.) This is the only difficult part. It has to be able to compensate for lots of commands at once. It   
doesn't matter how you handle this, but if 100s of people are submitting different commands, it  
needs to ignore the vast majority of commands, or maybe pick the most used command. This  
doesn't need to be addressed yet, I'm more concerned with making the core functionality.  

This video is an example of the idea that I want to implement, but I'm mostly concerned with basic functionality.  
https://www.youtube.com/watch?v=kExwHUQClYg
