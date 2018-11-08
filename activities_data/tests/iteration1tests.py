import unittest

# convert time from military time (string) to minutes after midnight (int)
# returns an int
def converttime_yelp(milittime):
    return 0

# validate the length of the business dict
def validate_dictlength(bizdict):
    return False

# validate the coordinates field of a business dict
def validate_coordinates(bizdict):
    return False

# validate the location field of a business dict
def validate_location(bizdict):
    return False

# validate the yelp-assigned ID of a business dict
def validate_yelpID(bizdict):
    return False

# SAMPLE DICTIONARIES FOR TESTING validate_dictlength

# right number of fields
sampledict = {
    "id": "WavvLdfdP6g8aZTtbBQHTw",
    "name": "Gary Danko",
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 0,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 1,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 2,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 3,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 4,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 5,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 6,
                    "start": "1730"
                }
            ],
        "is_open_now": False
        }
    ],
    "categories": [
        {
            "alias": "newamerican",
            "title": "American (New)"
        }
    ],
    "coordinates": {
        "latitude": 37.80587,
        "longitude": -122.42058
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
        "display_address": [
            "800 N Point St",
            "San Francisco, CA 94109"
        ],
        "cross_streets": "Hyde St & Larkin St"
    },
}

# wrong number of fields
sampledict2 = {
    "id": "WavvLdfdP6g8aZTtbBQHTw",
    "name": "Gary Danko",
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 0,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 1,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 2,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 3,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 4,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 5,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 6,
                    "start": "1730"
                }
            ],
        "is_open_now": False
        }
    ],
    "categories": [
        {
            "alias": "newamerican",
            "title": "American (New)"
        }
    ],
    "coordinates": {
        "latitude": 37.80587,
        "longitude": -122.42058
    },
}

# wrong number of fields
sampledict3 = {}

# wrong number of fields
sampledict4 = {
    "id": "WavvLdfdP6g8aZTtbBQHTw",
    "dummy_field": "dummy_value",
    "extra_dummy_field": "extra_dummy_value",
    "name": "Gary Danko",
    "hours": [
        {
            "hours_type": "REGULAR",
            "open": [
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 0,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 1,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 2,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 3,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 4,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 5,
                    "start": "1730"
                },
                {
                    "is_overnight": False,
                    "end": "2200",
                    "day": 6,
                    "start": "1730"
                }
            ],
        "is_open_now": False
        }
    ],
    "categories": [
        {
            "alias": "newamerican",
            "title": "American (New)"
        }
    ],
    "coordinates": {
        "latitude": 37.80587,
        "longitude": -122.42058
    },
}



# VALIDATION SAMPLE DICTIONARIES: for validate_coordinates,
# validate_location, and validate_yelpID



# coord: missing latitude
# location: missing address line 1
# id: missing id
sampledict5 = {
    "coordinates": {
        "longitude": -122.42058
    },
    "location": {
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
    },
}

# coord: missing longitude
# location: missing city
# id: wrong type
sampledict6 = {
    "coordinates": {
        "latitude": 37.80587,
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
    },
    "id": 17,
}

# coord: latitiude out of range - upper
# location: missing state
# id: wrong type
sampledict7 = {
    "coordinates": {
        "latitude": 95.0,
        "longitude": -122.42058
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "zip_code": "94109",
        "country": "US",
    },
    "id": 34.67,
}

# coord: latitiude out of range - lower
# location: missing zip code
# id: wrong type
sampledict8 = {
    "coordinates": {
        "latitude": -100.5,
        "longitude": -122.42058
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "country": "US",
    },
    "id": True,
}

# coord: longitude out of range - lower
# location: missing county
sampledict9 = {
    "coordinates": {
        "latitude": 37.805,
        "longitude": -186.7
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
    },
}

# coord: longitude out of range - upper
# location: address 1 wrong type
sampledict10 = {
    "coordinates": {
        "latitude": 37.805,
        "longitude": 194.25
    },
    "location": {
        "address1": 7,
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
    },
}

# coord: latitude wrong type
# location: city wrong type
sampledict11 = {
    "coordinates": {
        "latitude": "a",
        "longitude": -122.42058
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": 54,
        "state": "CA",
        "zip_code": "94109",
        "country": "US",
    },
}

# coord: longitude wrong type
# location: state wrong type
sampledict12 = {
    "coordinates": {
        "latitude": 37.805,
        "longitude": False
    },
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": False,
        "zip_code": "94109",
        "country": "US",
    },
}

# location: zip code wrong type
sampledict13 = {
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": 94109,
        "country": "US",
    },
}

# location: country wrong type
sampledict14 = {
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94109",
        "country": 3.5,
    },
}

class TestTimeConversion(unittest.TestCase):
    def test_converttime_yelp(self):
        self.assertEqual(converttime_yelp("0000"), 0)
        self.assertEqual(converttime_yelp("0200"), 120)
        self.assertEqual(converttime_yelp("0215"), 135)
        self.assertEqual(converttime_yelp("1000"), 600)
        self.assertEqual(converttime_yelp("2359"), 1439)
        self.assertEqual(converttime_yelp("2400"), 0)
        with self.assertRaises(TypeError):
            converttime_yelp("0")
        with self.assertRaises(TypeError):
            converttime_yelp("00")
        with self.assertRaises(TypeError):
            converttime_yelp("000")
        with self.assertRaises(TypeError):
            converttime_yelp("2500")
        with self.assertRaises(TypeError):
            converttime_yelp("2401")

class TestDictProperties(unittest.TestCase):
    def test_validate_dictlength(self):
        self.assertTrue(validate_dictlength(sampledict))
        self.assertFalse(validate_dictlength(sampledict2))
        self.assertFalse(validate_dictlength(sampledict3))
        self.assertFalse(validate_dictlength(sampledict4))

class TestBizProperties(unittest.TestCase):
    def test_validate_coordinates(self):
        self.assertFalse(validate_coordinates(sampledict3))
        self.assertFalse(validate_coordinates(sampledict5))
        self.assertFalse(validate_coordinates(sampledict6))
        self.assertFalse(validate_coordinates(sampledict7))
        self.assertFalse(validate_coordinates(sampledict8))
        self.assertFalse(validate_coordinates(sampledict9))
        self.assertFalse(validate_coordinates(sampledict10))
        self.assertFalse(validate_coordinates(sampledict11))
        self.assertFalse(validate_coordinates(sampledict12))
        self.assertTrue(validate_coordinates(sampledict))
    def test_validate_location(self):
        self.assertFalse(validate_location(sampledict5))
        self.assertFalse(validate_location(sampledict6))
        self.assertFalse(validate_location(sampledict7))
        self.assertFalse(validate_location(sampledict8))
        self.assertFalse(validate_location(sampledict9))
        self.assertFalse(validate_location(sampledict10))
        self.assertFalse(validate_location(sampledict11))
        self.assertFalse(validate_location(sampledict12))
        self.assertFalse(validate_location(sampledict13))
        self.assertFalse(validate_location(sampledict14))
        self.assertTrue(validate_location(sampledict))
    def test_validate_yelpID(self):
        self.assertFalse(validate_yelpID(sampledict5))
        self.assertFalse(validate_yelpID(sampledict6))
        self.assertFalse(validate_yelpID(sampledict7))
        self.assertFalse(validate_yelpID(sampledict8))
        self.assertTrue(validate_yelpID(sampledict))


if __name__ == '__main__':
    unittest.main()
