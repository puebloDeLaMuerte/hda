import json
import file
import time

class Agent:

  
    def __init__(self,id,color_string,roleName):
    
        self.id = id
        self.color_string = color_string
        self.white_string = "\033[37m"
        self.roleName = roleName
        self.roleString = ""
        self.message_history = []
        print()
        print(f"creating agent with id {self.id} and role {self.color_string}{self.roleName}{self.white_string}.")
        time.sleep(0.1)
        self.find_role_description()
        
    
    def find_role_description(self):
        
        roleFiles = file.list_role_files("all")
        roleFiles.extend( file.list_role_files(self.roleName) )
        
        for f in roleFiles:
            time.sleep(0.1)
            print("including role-file: ", f)
            self.roleString = self.roleString + " " + file.read_file_string(f)
        
        
        
    def add_message(self,agent_id, content):
    
        self.message_history.append({"agent_id": agent_id, "content": content})
        
        
        
    def get_system_message(self):
    
        return {"role":"system", "content": self.roleString}
    
    
        
    def get_formated_messages(self):
    
        formatted_messages = [self.get_system_message()]

        for message in self.message_history:

            role = "assistant" if message["agent_id"] == self.id else "user"
            
            formatted_messages.append({"role": role, "content": message["content"]})

        return formatted_messages
        
    
    
    def dump_message_history(self):
    
        filename = f"logs/agent_{self.id}_dump.txt"
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.message_history, file, ensure_ascii=False, indent=4)
        
        
        
    def dump_formatted_messages(self):

        filename = f"logs/agent_{self.id}_dump_formatted.txt"
        with open(filename, 'w', encoding='utf-8') as file:

            json.dump(self.get_formated_messages(), file, ensure_ascii=False, indent=4)
