from telethon.sync import TelegramClient, events
import config

# config.chats_name contains references on chats
# config.source contains reference on chat to forward messages

def start():
    client = TelegramClient('parser', config.api_id, config.api_hash)

    @client.on(events.NewMessage(chats=(config.chats_name)))
    async def normal_handler(event):
        # print(event.message.from_id)
        for key in config.keys:
            if key in event.message.to_dict()['message']:
                await client.forward_messages(config.source, event.message, event.message.from_id)

    client.start()
    client.run_until_disconnected()


if __name__ == '__main__':
    start()
