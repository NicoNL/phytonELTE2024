import json
from file_storage import EventFileManager

class EventAnalyzer():
    def get_joiners_multiple_meetings_method(self):

        storage = EventFileManager()
        events = storage.read_events_from_file()
        joiners = []
        repeatedJoiners = []
        for event in events:
            joiner = event.get("joiners")
            joiners.append(joiner)

        for i in range(len(joiners)):
            for j in range(i+1, len(joiners)):
                for k  in range(len(joiners[i])):
                    for m in range(len(joiners[j])):
                        if joiners[i][k].get("name")  == joiners[j][m].get("name"):
                            if joiners[j][m].get("name") not in repeatedJoiners:
                                repeatedJoiners.append(joiners[i][k].get("name"))
                            del joiners[j][m]
                            break

        return repeatedJoiners