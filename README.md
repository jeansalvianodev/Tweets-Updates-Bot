<h1 align="center">
<br>
  <img src="https://icons.iconarchive.com/icons/lboi/tweetscotty/128/twitter-bot-icon.png" alt="Twitter Updates Bot" width="120">
<br>
<br>
Twitter Updates Bot
</h1>

<p align="center">Application that sends tweets from a specified user to Telegram.</p>



[//]: # (Add your gifs/images here:)
<div align="center">
  <img src="https://i.imgur.com/QPsuSR4.gif" width="900px">
</div>

<hr />

## <b>What does it do?</b> 
The Tweets Updates Bot, using a telegram bot, sends real-time tweets from a specified twitter user, to a telegram user who messaged the bot.

## <b>Getting started</b>

~ First of all you will need to configure your Telegram and Twitter API tokens in the config.ini file.
<div>
  <img src="https://i.imgur.com/2y2rmNu.png" alt="config" height="250">
</div>
in the <b>[twitter]</b> tab goes the information of the Twitter API and in the <b>[telegram]</b> tab goes the token of your Telegram bot.

### - <b>Now you need to install some libraries</b>

All features that were used:

-  **Tweepy** — An easy-to-use Python library for accessing the Twitter API.
-  **Requests** —  An elegant and simple HTTP library for Python to receive Telegram user data.


``` 
pip install requests
pip install tweepy
```
### <b>Notes</b>: 

- You must send some message to the telegram bot for it to get your user id.
- If you choose to save the user IDs, the tweets will be sent to the IDs that are saved and also to the ones that are not but sent a message to the bot.
