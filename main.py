import config.botconfig as cfg
import requests


def send_message_to_tg_channels(message):
    bot_token = cfg.tg_bot['tg-token']
    base_url = 'https://api.telegram.org/bot{botToken}/sendMessage?chat_id={channel}&parse_mode=Markdown&text={message}'

    for channel in cfg.tg_bot['tg-channels']:
        url = base_url.format(botToken=bot_token, channel=channel, message=message)
        try:
            response = requests.get(url)
            print(response.json())
        except Exception as e:
            print('exception while sending message to channel: ' + channel + ' ' + str(e))


send_message_to_tg_channels("Testing Telegram bot")
