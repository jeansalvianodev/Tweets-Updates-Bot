import requests
import json
import configparser
import tweepy
import colorama
from colorama import Fore
from colorama import Style


colorama.init(convert=True)

def load_configs():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def responses():
    config = load_configs()
    telegram_token = config['telegram']['token']
    json_response = requests.get(f"https://api.telegram.org/bot{telegram_token}/getUpdates").json()

    def get_ids():
        users = json_response['result']
        users_ids = []

        for user in users:
            try:
                users_ids.append(user["message"]["chat"]["id"])

            except KeyError:
                users_ids.append(user["my_chat_member"]["chat"]["id"])  # doing tests i noticed that on some occasions the "message" key was not created, and in its place it would have the "my_chat_member" key

        users_set = list(set(users_ids))  # a set to remove repeated IDS
        return users_set
    return get_ids()
        
def save_ids():  # as the IDS disappear from getUpdates, it's feasible to write them in a json file
    users_dict = {'u_id': responses()}
    try:
        with open('users_ids.json', 'x') as bd_users:
            json.dump(users_dict, bd_users)  # checks if the file containing the IDS already exists and creates it if it doesn't
    except FileExistsError:
        with open('users_ids.json', 'r', encoding='utf-8') as bd_users:
            bd_users_json = json.load(bd_users)  # if it already exists, update the IDS in the key ['u_id']
            bd_users_json['u_id'] += users_dict['u_id']  # updating without losing old IDS
            set_bd_users = list(set(bd_users_json['u_id']))  
            bd_users_json['u_id'] = set_bd_users  # updating the file also without losing the old IDS and without repeating them

    try:
        with open('users_ids.json', 'w') as bd_users:
            json.dump(bd_users_json, bd_users)  # creating the updated file
    except UnboundLocalError:
        with open('users_ids.json', 'w') as bd_users:
            json.dump(users_dict, bd_users)

def saved_ids():
    id_responses = responses()
    with open('users_ids.json', 'r') as bd_users:
        bd_users_json = json.load(bd_users)

    load_ids = bd_users_json['u_id']
    for id in id_responses:
        load_ids.append(id)
    remove_repeated_ids = set(load_ids)
    return remove_repeated_ids

class BotShipping:    

    def __init__(self, users_ids, twitter_username):
        self.__twitter_username = twitter_username
        self.__users_ids = users_ids
        self.__config = load_configs()

    def send_to_users(self):
        telegram_token = self.__config['telegram']['token']
        consumer_key = self.__config['twitter']['consumer_key']
        consumer_secret = self.__config['twitter']['consumer_secret']
        access_token = self.__config['twitter']['access_token']
        access_token_secret = self.__config['twitter']['access_token_secret']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # (Cunsumer key, Consumer Secret)
        auth.set_access_token(access_token, access_token_secret)  # (Access Token, Access Token Secret)
        
        api = tweepy.API(auth)  # create the api
        
        telegram_users = []
        for user in self.__users_ids:
            telegram_users.append(user)

        class Listener(tweepy.Stream):

            print(Fore.GREEN + Style.BRIGHT + '################# Aguardando tweets do(s) usuário(os) #################')
            print(Fore.YELLOW + Style.BRIGHT + '        Você terá a opção de parar a execução a cada 10 tweets')
            tweets = []
            limit = 10

            def on_status(self, status):
                self.tweets.append(status)
                user_tweets = f"{status.user.screen_name}: {status.text}"
                print(Fore.LIGHTCYAN_EX + Style.BRIGHT + user_tweets)
                for user in telegram_users:
                    requests.get(f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={user}&text={user_tweets}")

                if len(self.tweets) == self.limit:
                    user_response = input(Fore.WHITE + Style.BRIGHT + 'Gostaria de desconectar? caso sim, digite' + Fore.RED + Style.BRIGHT + ' "exit"' + Fore.WHITE + Style.BRIGHT + ': ').lower().strip()

                    if user_response == 'exit':
                        self.disconnect()
                        print(Fore.GREEN + Style.BRIGHT + 'Tweets enviados com sucesso!' + Fore.RESET)
                    else:
                        self.limit += 10
                

        stream_tweet = Listener(consumer_key, consumer_secret, access_token, access_token_secret)

        first_users = self.__twitter_username.strip()
        users = first_users.split(',')
        user_ids = []
        for user in users:
            user_ids.append(api.get_user(screen_name=user).id)  # get the twitter username 

        stream_tweet.filter(follow=user_ids)
        
        return

def input_save():
    user_response = input(Fore.WHITE + Style.BRIGHT + 'Deseja salvar o usuário do Telegram?(Y/n): ').strip()

    if user_response == 'Y':
        save_ids()
        print(Fore.GREEN + Style.BRIGHT + 'IDs salvos com sucesso!' + Fore.RESET)
    else:
        pass
    
def init():
    user_input = input(Fore.WHITE + Style.BRIGHT + 'Digite o nome de usuário do twitter sem o "@" (caso seja mais de um, separe-os por vírgula): ' + Fore.RESET)
    input_save()
    try:
        send = BotShipping(saved_ids(), user_input)
        send.send_to_users()
    except FileNotFoundError:   
        send = BotShipping(responses(), user_input)
        send.send_to_users()

init()