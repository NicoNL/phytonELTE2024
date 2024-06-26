from fastapi import APIRouter, HTTPException
from typing import List
from .models import Event
from file_storage import EventFileManager
from event_analyzer import EventAnalyzer


router = APIRouter()


@router.get("/events", response_model=List[Event])
async def get_all_events():
    storage = EventFileManager()
    events = storage.read_events_from_file()
    return events


@router.get("/events/filter", response_model=List[Event])
async def get_events_by_filter(date: str = None, organizer: str = None, status: str = None, event_type: str = None):
    storage = EventFileManager()
    events = storage.read_events_from_file()
    newEvents = []

    if date:
        for event in events:
            if event.get("date") == date:
                newEvents.append(event)

    if organizer:
        for event in events:
            if event.get("organizer").get("name") == organizer or  event.get("organizer").get("email") == organizer:
                newEvents.append(event)
    
    if status:
        for event in events:
            if event.get("status") == status:
                newEvents.append(event)

    if event_type:
        for event in events:
            if event.get("type") == event_type:
                newEvents.append(event)

    return newEvents


@router.get("/events/{event_id}", response_model=Event)
async def get_event_by_id(event_id: int):
    storage = EventFileManager()
    events = storage.read_events_from_file()
    if event_id:
        for event in events:
            if event.get("id") == event_id:
                return event
            
    raise HTTPException(status_code=200, detail="Event not found")



@router.post("/events", response_model=Event)
async def create_event(event: Event):
    storage = EventFileManager()
    index = 0
    events = storage.read_events_from_file()
    for tempEvent in events:
        if tempEvent.get("id")  == event.id:
            event = tempEvent
            raise HTTPException(status_code=200, detail="Event ID already exists")
        index += 1
    events.append(event)
    events[index] = event.dict()
    storage.write_events_to_file(events)

    return event


@router.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: int, event: Event):
    event = event.dict()
    storage = EventFileManager()
    events = storage.read_events_from_file()
    notFound = True
    i = 0
    for tempEvent in events:
        if tempEvent.get("id")  == event_id:
            if event_id != event.get("id"):
                raise HTTPException(status_code=201, detail="The given ID should match with the new event's ID")
            notFound= False
            events[i] = event
        i += 1
    if(notFound):
        raise HTTPException(status_code=201, detail="Event does not exist")
    
    storage.write_events_to_file(events)
    return event


@router.delete("/events/{event_id}")
async def delete_event(event_id: int):
    storage = EventFileManager()
    events = storage.read_events_from_file()
    delEvent = None
    notFound = True
    i = 0
    for tempEvent in events:
        if tempEvent.get("id")  == event_id:
            notFound= False
            delEvent = events[i]
            del events[i]
            break
        i += 1
    if(notFound):
        raise HTTPException(status_code=201, detail="Event does not exist")
    
    storage.write_events_to_file(events)
    return delEvent


@router.get("/events/joiners/multiple-meetings")
async def get_joiners_multiple_meetings():

    analyzer = EventAnalyzer()
    joiners = analyzer.get_joiners_multiple_meetings_method()

    if len(joiners) == 0:
        raise HTTPException(status_code=202, detail="No joiners attending at least 2 meetings")

    return joiners

