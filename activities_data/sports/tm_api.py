# make calls to ticketmaster to find sporting events
import requests
import geohash2
import time
import json
# this is the credential file and is not in the repository
from tm_auth import *
from tm_tests import *


# URI format
# https://app.ticketmaster.com/{package}/{version}/{resource}.json?apikey={key}
# 200 - successful operation
# maximum page size is 200
# check rate limit by:
# r = requests.get(URI)
# r.headers["Rate-Limit-Available"] <- will give back the number as a string
URI = "https://app.ticketmaster.com/%s.json"
EVENTS = "discovery/v2/events"
VENUES = "discovery/v2/venues"
CLASS_ID = {
                "Sports":       {"id": "KZFzniwnSyZfZ7v7nE",
                                 "name": "Sports"},
                "Music":        {"id": "KZFzniwnSyZfZ7v7nJ",
                                 "name": "Music"},
                "ArtsTheatre":  {"id": "KZFzniwnSyZfZ7v7na",
                                 "name": "Arts & Theatre"},
                "Film":         {"id": "KZFzniwnSyZfZ7v7nn",
                                 "name": "Film"}
}
CITY_LOCS = {
                "Chicago": {"lat": 41.8781,
                            "lon": -87.6298}
}
# we need to append a unique code in front of each id to ensure that our ids
# for each api are actually unique when we combine them all together
TM_ID = "TMAPI"


# around 30 mile range seems reasonable
def get_tm_venues(city, range):
    '''
    finds venues by city and range around that city by miles

    inputs:
        city (str) - city, will use CITY_LOCS to get lat and lon values
        range (int) - miles around city to look for venues

    outputs:
        venues (list) - dictionary of venues that follows structure in
                        tm_tests.py
    '''
    print("Running get_venues...")
    # URL base to use
    venues_url = URI % VENUES
    # check city validity
    if city not in CITY_LOCS:
        print("ERROR: city is not valid")
        return -1
    city = CITY_LOCS[city]
    # payload to use for our request
    payload = {
        "apikey": switch_key(),
        "radius": range,
        "unit": "miles",
        "size": 200,
        "page": 0,
        "geoPoint": geohash2.encode(city["lat"], city["lon"], precision=9)
    }
    # data structures to hold the responses
    venues = []
    cont = True
    # now we can make the request to get venues
    while cont:
        r = requests.get(venues_url, params=payload)
        if check_r_status(r):
            print("SOLUTION: switching api keys and trying again")
            payload["apikey"] = switch_key()
        else:
            # process the data that was requested
            data = r.json()
            v_list = process_tm_venues(data)
            print("%d venues found on this page" % len(v_list))
            for v in v_list:
                if tm_venue_check(v):
                    venues.append(v)
                else:
                    print("ERROR: venue did not pass the venue check")
                    print("Printing here and dropping the venue:")
                    print(v)
            # now we need to check whether or not to continue
            print("completed page: %d" % (data["page"]["number"] + 1))
            print("out of: %d" % data["page"]["totalPages"])
            if data["page"]["number"] < (data["page"]["totalPages"] - 1):
                payload["page"] += 1
                print("going to next page")
                # should pause for a sec to not get rate limited
                time.sleep(3)
            else:
                print("done running")
                cont = False

    return venues


def process_tm_venues(data):
    '''
    takes a request response and extracts the relevant data and puts it into
    a dictionary

    inputs:
        data (dict) - response from the venue request

    outputs:
        venue_list (list) - list of dicts of venues
    '''
    venue_list = []
    # get to the actual list of venues
    venues_raw = data["_embedded"]["venues"]
    # iterate through and extract relevant data
    for v in venues_raw:
        tmp = {}
        tmp["venue_id"] = TM_ID + v["id"]
        tmp["venue_name"] = v["name"]
        tmp["latitude"] = float(v["location"]["latitude"])
        tmp["longitude"] = float(v["location"]["longitude"])
        tmp["address1"] = v.get("address", {}).get("line1", "")
        tmp["address2"] = v.get("address", {}).get("line2", "")
        tmp["address3"] = v.get("address", {}).get("line3", "")
        tmp["city"] = v["city"]["name"]
        tmp["state"] = v["state"].get("stateCode", v["state"]["name"])
        tmp["zip_code"] = v.get("postalCode", "")
        # done getting info, add to list
        venue_list.append(tmp)

    return venue_list


def tm_venue_demo():
    '''
    '''
    venues = get_tm_venues("Chicago", 30)
    if venues == -1:
        print("ERROR: get_tm_venues did not run successfully")
        return -1
    with open("venues_11122018.json", "w") as fp:
        json.dump(venues, fp)

    return 0


# use same range as venues search ~30
def get_tm_events(type, city, range):
    '''
    searches city for events of a given type within a range around the city

    inputs:
        type (str) - looks ups the type in CLASS_ID and uses that id
        city (str) - city lat and lon to use from CITY_LOCS dict
        range (int) - range to search around the city

    outputs:
        tm_events (list) - list of dicts, each dict is a sporting event
    '''
    print("Running get_tm_events...")
    # URL base to use
    events_url = URI % EVENTS
    # check city validity
    if city not in CITY_LOCS:
        print("ERROR: city is not valid")
        return -1
    city = CITY_LOCS[city]
    # check type validity
    if type not in CLASS_ID:
        print("ERROR: type is not valid")
        return -1
    type_id = CLASS_ID[type]["id"]
    # payload to use for our request
    payload = {
        "apikey": switch_key(),
        "classificationId": type_id,
        "radius": range,
        "unit": "miles",
        "size": 200,
        "page": 0,
        "geoPoint": geohash2.encode(city["lat"], city["lon"], precision=9)
    }
    # data structures to hold the responses
    tm_events = []
    cont = True
    # now we can make the request to get events
    while cont:
        r = requests.get(events_url, params=payload)
        if check_r_status(r):
            print("SOLUTION: switching api keys and trying again")
            payload["apikey"] = switch_key()
        else:
            # process the data that was requested
            data = r.json()
            e_list = process_tm_events(data)
            print("%d events found on this page" % len(e_list))
            for e in e_list:
                if tm_event_check(e):
                    tm_events.append(e)
                else:
                    print("ERROR: event did not pass the event check")
                    print("Printing here and dropping the event:")
                    print(e)
            # now we need to check whether or not to continue
            print("completed page: %d" % (data["page"]["number"] + 1))
            print("out of: %d" % data["page"]["totalPages"])
            if data["page"]["number"] < (data["page"]["totalPages"] - 1):
                payload["page"] += 1
                print("going to next page")
                # should pause for a sec to not get rate limited
                time.sleep(3)
            else:
                print("done running")
                cont = False

    return tm_events


def process_tm_events(data):
    '''
    takes the data from the request response and extracts the relevant data

    inputs:
        data (dict) - contains all the data from the request
    outputs:
        event_list (list) - list of dicts that each describe an event
    '''
    event_list = []
    # get to the actual list of venues
    events_raw = data["_embedded"]["events"]
    # iterate through and extract relevant data
    for e in events_raw:
        tmp = {}
        tmp["event_id"] = TM_ID + e["id"]
        tmp["event_name"] = e["name"]
        # may need to handle the potential for multiple venues
        tmp["venue_id"] = TM_ID + e["_embedded"]["venues"][0]["id"]
        # need to edit start time and convert to minutes from midnight
        start = e["dates"]["start"].get("localTime", -10)
        if start == -10:
            tmp["start"] = -10
        else:
            start = start.split(":")
            tmp["start"] = int(60 * int(start[0]) + int(start[1]))
        tmp["end"] = -10
        # need to edit date to MM-DD-YY
        # may need to account for events that span multiple dates
        date = e["dates"]["start"]["localDate"]
        date = date.split("-")
        tmp["date"] = date[1] + "-" + date[2] + "-" + date[0]
        tmp["tags"] = get_event_tags(e)
        # may need to handle the potential for different ticket types
        # -10 code if cannot find a price
        tmp["price"] = float(e.get("priceRanges", [{}])[0].get("min", -10))
        # done getting info, add to list
        event_list.append(tmp)

    return event_list


def get_event_tags(e):
    '''
    given an event, find relevant tags to put into the tags field

    inputs:
        e (dict) - a single event, contains information for that event
    outputs:
        tags (list) - list of tags relating to the event
    '''
    tags = []
    # look in classifications for tags
    for c in e["classifications"][0].values():
        if type(c) == dict:
            tags.append(c["name"])

    return tags


def tm_events_demo():
    '''
    '''
    events = get_tm_events("Sports", "Chicago", 30)
    if events == -1:
        print("ERROR: get_tm_venues did not run successfully")
        return -1
    with open("events_11132018.json", "w") as fp:
        json.dump(events, fp)

    return 0
