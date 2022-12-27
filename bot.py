import argparse
import discord
import asyncio
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def download_files(channel_id):
    print('download_files function started')
    channel = client.get_channel(channel_id)
    messages = []
    async for message in channel.history(limit=None):
        messages.append(message)

    print(f'{len(messages)} messages found')

    # Download all files from the channel
    for message in messages:
        if message.attachments:
            attachment = message.attachments[0]
            user = message.author

            # Create a subfolder for the user if it doesn't already exist
            user_folder = os.path.join("files", user.name)
            if not os.path.exists(user_folder):
                os.makedirs(user_folder)

            # Construct the file path for the image
            file_path = os.path.join(user_folder, attachment.filename)

            print(f'Saving image {attachment.filename} from message {message.id} with content "{message.content}"')
            # Download and save the image
            await attachment.save(file_path)
        else:
            print(f'No attachments in message {message.id} with content "{message.content}"')

        # Add a small delay to avoid overloading the Discord API
    
        await asyncio.sleep(0.5)

    print('download_files function finished')



async def download_transcript(channel_id):
    print('download_transcript function started')
    channel = client.get_channel(channel_id)
    messages = []
    async for message in channel.history(limit=None):
        messages.append(message)

    print(f'{len(messages)} messages found')

    # Save the transcript to a file
    transcript_file = f'{channel_id}-transcript.txt'
    with open(transcript_file, 'w') as f:
        # Write the messages to the file in reverse order (oldest messages first)
        for message in reversed(messages):
            f.write(f'{message.created_at} | {message.author} | {message.content}\n')

        print(f'Transcript saved to {transcript_file}')
    
    # Add a small delay to avoid overloading the Discord API
    await asyncio.sleep(0.5)
    print('download_transcript function finished')





@client.event
async def on_ready():
    await download_files(args.channel_id)
    print(args.channel_id)
@client.event
async def on_ready():
    if args.mode == 'files':
        await download_files(args.channel_id)
    elif args.mode == 'transcript':
        await download_transcript(args.channel_id)


if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Download all files or a transcript from a Discord channel")
    parser.add_argument("channel_id", type=int, help="ID of the Discord channel to download from")
    parser.add_argument("--token", required=True, help="Discord bot token")
    parser.add_argument("--mode", required=True, choices=['files', 'transcript'], help="Mode to run the bot in (either 'files', 'transcript')")
    args = parser.parse_args()

    # Run the Discord bot
    try:
        client.run(args.token)
        if args.mode == 'files':
            download_files(args.channel_id)
        elif args.mode == 'transcript':
            download_transcript(args.channel_id)
    except Exception as e:
        print("Error:", e)
