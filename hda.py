from openai import OpenAI
from session import Session
from agent import Agent
import file
import greet



client = OpenAI(
    api_key=file.readFileString("data/api_key.txt"),
)


def get_next_conversation_item(agent1,agent2):
    
    reply = request_completion( agent1.get_formated_messages())
    agent1.add_message(agent1.id,reply)
    agent2.add_message(agent1.id,reply)

    print( "\033[37magent",agent1.id,": ",agent1.color_string, reply )
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



session = Session()

session.agents.append( Agent(1,"\033[35m","We're roleplaying. this is your role: You are an interrested hobbyist in the field of Vulcanology. You hear Volcanos sometimes produce rings of smoke and you wonder if that means that they are homes to silicate based lifeforms, living deep in their bellies, but you also have read some bits and pieces of actual Volcano-science here and there. You are in a colloquial discussion, so you talk in shorter sentences, being in a fast paced a conversation rather than elaborately explaining concepts or your views. please engage in a fluid conversation with me. With each reply you only state your next part of the conversation. don't give me whole back-and-forth conversational fragments. only play your role and let me talk to you instead of outputting whole conversations.") )
session.agents.append( Agent(2,"\033[36m","We're roleplaying. this is your role: You are an experienced researcher in the Fields of Geology specializing on the science around Volcanos. You are an absolute expert on this and you dispise misinformation and unscientific talk. You work as science communicator to educate the public about the process of science itself as well as the specifics of your field of expertise. You are in a colloquial discussion, so you talk in shorter sentences, being in a fast paced a conversation rather than elaborately explaining concepts or your views.  please engage in a fluid conversation with me. With each reply you only state your next part of the conversation. don't give me whole back-and-forth conversational fragments. only play your role and let me talk to you instead of outputting whole conversations.") )


while True:

    get_next_conversation_item(session.agents[0],session.agents[1])
    inp = input()
    if inp == 'd':
        session.agents[0].dump_message_history()
    if inp == 'df':
        session.agents[0].dump_formatted_messages()
    get_next_conversation_item(session.agents[1],session.agents[0])
    inp = input()
    if inp == 'd':
        session.agents[1].dump_message_history()
    if inp == 'df':
        session.agents[1].dump_formatted_messages()


