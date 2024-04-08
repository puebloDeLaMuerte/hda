```markdown
    __  ______  ___ 
   / / / / __ \/   |
  / /_/ / / / / /| |
 / __  / /_/ / ___ |
/_/ /_/_____/_/  |_|
human director actor
```
...is a little research project by blutgruppe digital that makes OpenAIs ChatGPT talk to itself.
Currently it is possible to define individual roles for two actors that will have a conversation.
We want to add capability for more actors and a channel for a human to be part of the conversation as well.

for now:

pip install openai

get an openAI api-key and put it in a file named api_key.txt inside ./data folder

define roles by adding text snippets as individual texfiles with one line of text in them to named role-folders in data/roles

all actors will be primed with text-snippets from ./data/roles/all plus the snippets found in their respective role-folder


