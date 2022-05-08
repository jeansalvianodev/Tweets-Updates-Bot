<h1 align="center">
<br>
  <img src="https://icons.iconarchive.com/icons/lboi/tweetscotty/128/twitter-bot-icon.png" alt="Twitter Updates Bot" width="120">
<br>
<br>
Twitter Updates Bot (PT-BR)
</h1>

<p align="center">Application that sends tweets from a specified user to Telegram.</p>



[//]: # (Add your gifs/images here:)

![save1](https://user-images.githubusercontent.com/59858254/167220602-7935b411-5229-45b7-9517-cf6d24f455e1.gif)


<hr />

## <b>What does it do?</b> 
The Tweets Updates Bot, using a Telegram bot, sends real-time tweets from a specified Twitter user, to a Telegram user who messaged the bot.

## <b>Getting started</b>

### First of all you will need to configure your Telegram and Twitter API tokens in the config.ini file.
<div>
  <img src="https://i.imgur.com/2y2rmNu.png" alt="config" height="250">
</div>

<b>Detail: do not put quotes (")!!</b>

in the <b>[twitter]</b> tab goes the information of the Twitter API and in the <b>[telegram]</b> tab goes the token of your Telegram bot.

### - <b>Now you need to install some libraries</b>

-  **Tweepy** — An easy-to-use Python library for accessing the Twitter API.
-  **Requests** —  An elegant and simple HTTP library for Python to receive Telegram user data.
-  **Colorama** — Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.


``` 
pip install colorama
pip install requests
pip install tweepy
```
### <b>Notes</b>: 

- You must send some message to the Telegram bot for it to get your user id.
- If you choose to save the user IDs, the tweets will be sent to the IDs that are saved and also to the ones that are not but sent a message to the bot.
- Your twitter api must have elevated access
