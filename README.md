# watsapp2sqlite
Converts a WhatsApp exported chat `.txt` file into a SQLite database, so you can actually do something useful with your conversations.

## Why
WhatsApp lets you export chats but gives you a flat text file. This just drops it into SQLite so you can query it however you want.

## Usage
Edit the top of the script with your details:
```python
contact = "+55 00 0000 0000"  # who the chat is with
chat = "/path/to/chat.txt"
database = "/path/to/chat.db"
```
Then run it:
```sh
python main.py
```
## Notes
* Tested with Brazilian Portuguese WhatsApp exports. Date format might vary if your phone is set to a different locale
* Don't run it twice on the same database, it'll duplicate everything
* Multi-line messages are handled

## Querying the data
Once you have the .db file, you can open it with any SQLite tool. A few useful queries to get started:
```sql
-- messages per sender
SELECT sender, COUNT(*) FROM conversations GROUP BY sender;

-- most active days
SELECT date, COUNT(*) FROM conversations GROUP BY date ORDER BY COUNT(*) DESC;
```
