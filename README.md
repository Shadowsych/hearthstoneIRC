# Hearthstone IRC
A simple bot program that reads screen commands from the Twitch.tv channel chat window  
and responds with a macro onto the streamer's screen. 

# Heartstone IRC Credentials  
- Gmail: hearthstoneirc@gmail.com
- Twitch.tv Username: HearthstoneIRC
- Twitch.tv/Gmail Password: HearthstoneIRC2018

# Technologies and References
- [Twitch API](https://dev.twitch.tv/api)
- [Twitch Chat OAuth Password Generator](https://twitchapps.com/tmi/)
- [PyWin32](https://sourceforge.net/projects/pywin32/)
- [Python 2.7](https://www.python.org/download/releases/2.7/)
- [ASCII Table](https://www.systutorials.com/4670/ascii-table-and-ascii-code/)

# Set-up (Mandatory)
1. Go to config/config.py and replace the username and password with your Twitch bot's  
username and OAuth Password key  
2. Open the "HSIRC Macros.exe" application  
3. Install "pywin32" and run it with "python  v2.7"  
4. Open up your terminal or cmd and and "cd" into this repository's file directory  
then in the terminal or cmd type "python serve.py" (if your username or password was wrong, it will notify you)  
5. You are finished setting-up the Twitch bot!  

NOTE: Whilst the script is running make sure you have your emulator in focus as your primary window.  
If you click onto another window, the script won't work. If you're not able to stay focused on one window as
you need to do other things with your computer, you could try running all of this from within a virtual machine.  

# Default Chat Commands
"up" = Move up  
"down" = Move down  
"left" = Move left  
"right" = Move right  
"click" = Left mouse click  
"endturn" = End player's turn  
"play" = Clicks the "Play" button on the bottom-left screen  
"cancel" = Cancels actions  
"switchl" = Switch between enemy/player through the left-side  
"switchr" = Switch between enemy/player through the right-side  
"options" = Opens the options menu  

# Configuring Chat Commands (Optional)
1. Open the lib/game.py file  
2. Add or delete new indexes to the "keymap" array 
3. For each "keymap" array index, the key is the string command the viewer types and the  
value is the ASCII hexadecimal keyboard key (see the dependencies for information on the ASCII Table)

# Inspiration
This video inspired the idea to create this Twitch Plays Hearthstone IRC chat bot. 
https://www.youtube.com/watch?v=kExwHUQClYg"
