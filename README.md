# Hearthstone IRC  
A simple bot program that reads screen commands from the Twitch.tv channel chat window  
and responds with a macro within the streamer's screen.  

# Heartstone IRC Credentials  
- Gmail: hearthstoneirc@gmail.com
- Twitch.tv Username: HearthstoneIRC
- Twitch.tv/Gmail Password: HearthstoneIRC2018

# Dependencies
- Twitch API: https://dev.twitch.tv/api
- Twitch Chat OAuth Password Generator: https://twitchapps.com/tmi/
- PyWin32: https://sourceforge.net/projects/pywin32/
- Python 2.7.x: https://www.python.org/download/releases/2.7/

# Design Specifications
"1.) Accurately read in twitch.tv chat commands when a streamer runs the bot. So let's say a  
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
https://www.youtube.com/watch?v=kExwHUQClYg"
