# testing file for ticketmaster api calls
# activities that use the ticketmaster api:
# - sports
# - music
# NOTE: none of the events that we are getting from the ticketmaster api will
#       be put into the permanent events table; everything is going into the
#       one time event table


# check that single venue data is valid
# structure of data to be put into venue database:
# {
#     "venues": [
#         {
#             "venue_id": (int),
#             "venue_name": (str),
#             "latitude": (float),
#             "longitude": (float),
#             "address": (string)
#         },
#         {
#             "venue_id": (int),
#             "venue_name": (str),
#             "latitude": (float),
#             "longitude": (float),
#             "address": (string)
#         },
#         ...
#     ]
# }
def venue_check(venue):
    '''
    check an individual venue dict to make sure that all of the components are
    there and are the correct type before adding it into dictionary
    NOTE: this check is being performed constantly as we process venue data and
          add it into the json file before pushing it all into the database

    intput:
        venue (dict) - holds venue data
    ouput:
        valid (boolean) - True or False
    '''
    valid = True
    if not venue.get("venue_id", 0) == int:
        print("TYPE ERROR: venue_id should be int")
        valid = False
    if not venue.get("venue_name", 0) == str:
        print("TYPE ERROR: venue_name should be str")
        valid = False
    if not venue.get("latitude", 0) == float:
        print("TYPE ERROR: latitude should be float")
        valid = False
    if not venue.get("longitude", 0) == float:
        print("TYPE ERROR: longitude should be float")
        valid = False
    if not venue.get("address", 0) == str:
        print("TYPE ERROR: address should be str")
        valid = False

    return valid


# check that single event data is valid
# structure of data to be put into one time events database:
# {
#     "events": [
#         {
#             "event_id": (int),
#             "event_name": (str),
#             "venue_id": (int),
#             "start": (int)(minutes),
#             "end": (int)(minutes),
#             "event_date": (date),
#             "tags": (str)(list),
#             "price": (int)
#         },
#         {
#             "event_id": (int),
#             "event_name": (str),
#             "venue_id": (int),
#             "start": (int)(minutes),
#             "end": (int)(minutes),
#             "event_date": (date),
#             "tags": (list),
#             "price": (float)
#         },
#         ...
#     ]
# }
def event_check(event):
    '''
    check an individual event dict to make sure that all of the components are
    there and are the correct type
    NOTE: similar to the venue_check, this check is done every time we process
          a new event and before we put it into the file to be pushed to the
          database

    input:
        event (dict) - holds all data for a single event
    output:
        valid (boolean) - True or False
    '''
    valid = True
    if not event.get("event_id", 0) == int:
        print("TYPE ERROR: event_id should be int")
        valid = False
    if not event.get("event_name", 0) == str:
        print("TYPE ERROR: event_name should be str")
        valid = False
    if not event.get("venue_id", 0) == int:
        print("TYPE ERROR: venue_id should be int")
        valid = False
    if not event.get("start", 0) == int:
        print("TYPE ERROR: start should be int")
        valid = False
    if not event.get("end", 0) == int:
        print("TYPE ERROR: end should be int")
        valid = False
    # still need to standardize our date formats across apis
    # if not event.get("event_date", 0) == date:
    #     print("TYPE ERROR: event_date should be date")
    #     valid = False
    if not event.get("tags", 0) == int:
        print("TYPE ERROR: tags should be list")
        valid = False
    if not event.get("price", 0) == float:
        print("TYPE ERROR: price should be float")
        valid = False

    return valid


# check that all events have a valid venue id
def check_all_venue_id(events, venues):
    '''
    before pushing the data that we just processed into the database, we need
    to confirm that all of the events that we processed have a valid venue_id

    input:
        events (dict) - the final dict that we plan to push into the database
        venues (list) - a list of venues that are in our database or are going
                        to be added into the database
    output:
        valid (boolean) - True or False
    '''
    venues = set(venues) # make it faster to check if an id exists
    valid = True

    for event in events["events"]:
        venue_id = event["venue_id"]
        if not venue_id in venues:
            event_id = event["event_id"]
            print("EVENT ERROR: event %d has invalid venue_id" % event_id)
            valid = False

    return valid
