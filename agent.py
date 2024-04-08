import json

class Agent:

  
    def __init__(self,id,color_string,role):
    
        self.id = id
        self.color_string = color_string
        self.role = role
        self.message_history = []
        
        
    def add_message(self,agent_id, content):
    
        self.message_history.append({"agent_id": agent_id, "content": content})
        
        
        
    def get_system_message(self):
    
        return {"role":"system", "content": self.role}
    
    
        
    def get_formated_messages(self):
    
        formatted_messages = [self.get_system_message()]

        for message in self.message_history:

            role = "assistant" if message["agent_id"] == self.id else "user"
            
            formatted_messages.append({"role": role, "content": message["content"]})

        return formatted_messages
        
    
    
    def dump_message_history(self):
    
        filename = f"agent_{self.id}_dump.txt"
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.message_history, file, ensure_ascii=False, indent=4)
        
        
        
    def dump_formatted_messages(self):

        filename = f"agent_{self.id}_dump_formatted.txt"
        with open(filename, 'w', encoding='utf-8') as file:

            json.dump(self.get_formated_messages(), file, ensure_ascii=False, indent=4)
