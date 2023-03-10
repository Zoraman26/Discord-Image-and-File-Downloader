# Discord file and Transcript Downloader

This script allows you to download all files or a transcript of all messages in a Discord channel.

## Requirements

- Python 3.8 or higher
- The `discord` and `requests` libraries (install with `pip install discord requests`)

## Configuration

The config.json file should be in the following format:

`{
  "allowed_filetypes": [
    "png",
    "jpg",
    "jpeg",
    "gif"
    ]}`

The allowed_filetypes field is a list of file types that the script should download. The script will only download files with file types that are included in this list.


## Usage

To use the script, run the following command:

``python bot.py CHANNEL_ID --token TOKEN --mode MODE``

Replace `CHANNEL_ID` with the ID of the Discord channel you want to download from, `TOKEN` with your Discord bot token, and `MODE` with either `files`, `transcript`

For example, to download all files from the channel with ID 12345 and a Discord bot token of `abcdefghijklmnopqrstuvwxyz`, you would run the following command:

``python bot.py 12345 --token abcdefghijklmnopqrstuvwxyz --mode files``

To download a transcript of all messages in the channel, use `transcript` as the value for `MODE`.

## Output

When running in `files` mode, the script will download all files from the specified channel and save them to a subfolder inside the `files` directory. The subfolder will be named after the user who sent the message containing the file.

For example, if the user "Alice" sent an file in the channel, the file would be saved to the following location: `files/Alice/image.png`

When running in `transcript` mode, the script will create a text file named `transcript.txt` in the current directory and save a transcript of all messages in the channel to the file. The transcript will include the date and time, user, and content of each message.


## Notes

- The script will download both files that are directly attached to messages in the channel and any linked files.
- The script may take a while to run, depending on the number of messages and files in the channel.
- The script may use up a lot of bandwidth, depending on the size of the files being downloaded.
- The script may use up a lot of disk space, depending on the number and size of the files being downloaded.

## Limitations

- The script does not download any messages that have been deleted or retrieve the original content of messages that have been edited.
- The script does not download any messages from private channels or direct messages.
- The script does not download any messages from channels that the bot does not have access to.
