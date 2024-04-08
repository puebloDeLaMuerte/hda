from openai import OpenAI
from session import Session
from agent import Agent
import file
import greet
import sys


white_string = "\033[37m"

client = OpenAI(
    api_key=file.read_file_string("data/api_key.txt"),
)


def get_next_conversation_item(agent1,agent2):
    
    reply = request_completion( agent1.get_formated_messages())
    agent1.add_message(agent1.id,reply)
    agent2.add_message(agent1.id,reply)

    print( f"{white_string}agent",agent1.id,": ",agent1.color_string, reply )
    print()




def request_completion(messages_array):

    completion = client.chat.completions.create(
        model="gpt-4",
        frequency_penalty=1.8,
        n=1,
        #temperature=0.1,
        messages = messages_array,
    )
    
    return completion.choices[0].message.content



def wait_input():
    inp = input()
    if inp == 'd':
        for agent in session.agents:
            agent.dump_message_history()
    if inp == 'df':
        for agent in session.agents:
            agent.dump_formatted_messages()
    if inp == 'exit':
        sys.exit()


session = Session()
session.agents.append( Agent(1, "\033[35m", "hobbyist_vulcanologist") )
session.agents.append( Agent(2, "\033[36m", "expert_vulcanologist") )


print()
print("** how to use **")
print()
print("   press [enter] to trigger next conversation item")
print("   type 'd' [enter] to log the conversation history")
print("   type 'df' [enter] to log the conversation history formatted as sent to openAI via messages array")
print()
print()
print("** starting conversation now **")
print()
while True:

    get_next_conversation_item(session.agents[0],session.agents[1])
    wait_input()
    get_next_conversation_item(session.agents[1],session.agents[0])
    wait_input()
    



