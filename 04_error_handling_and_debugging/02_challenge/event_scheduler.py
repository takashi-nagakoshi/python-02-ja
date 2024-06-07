class Event:
    def __init__(self, name, start_hour):
        self.name = name
        self.start_hour = start_hour


def schedule_events(event_list):
    schedule = {}
    for event in event_list:
        if event.start_hour < 0 or event.start_hour > 24:
            print(f"Invalid time for event {event.name}")
        else:
            if event.start_hour in schedule:
                schedule[event.start_hour].append(event.name)
            else:
                schedule[event.start_hour] = [event.name]
    return schedule


def print_schedule(schedule):
    for hour, events in sorted(schedule.items()):
        print(f"{hour}:00 - {', '.join(events)}")


events = [
    Event("Python Workshop", 19),
    Event("This should not be happening", 30),
    Event("Data Science Meetup", 14),
    Event("Web Dev Seminar", 18),
]
schedule = schedule_events(events)
print_schedule(schedule)
