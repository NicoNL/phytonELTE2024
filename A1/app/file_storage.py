import json

class EventFileManager():
    FILE_PATH = "event.json"
    
    def read_events_from_file(self):
        with open(self.FILE_PATH, "r") as file:
            events= json.load(file)
        return events
    
    def write_events_to_file(self,newEvents):
        with open(self.FILE_PATH, "w") as file:
            json.dump(newEvents, file, indent=2)