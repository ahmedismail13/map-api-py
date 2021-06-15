# map-api-py

A free map location API, where you send a get request to the url with the lat/long values and it returns the exact address details of this location.

Example:
http://ahmedismail13.pythonanywhere.com/?lat=37.791703201220216&long=-122.42454634979369

Response:
{
  address: {
    city: "San Francisco",
    country: "United States",
    country_code: "us",
    county: "San Francisco",
    house_number: "1845",
    neighbourhood: "Japantown",
    postcode: "90214",
    road: "Franklin Street",
    state: "California"
  },
  boundingbox: [
    "37.7916565",
    "37.7918654",
    "-122.4247641",
    "-122.4244009"
  ],
  display_name: "1845, Franklin Street, Japantown, San Francisco, San Francisco City and County, San Francisco, California, 90214, United States",
  lat: "37.791761",
  licence: "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
  lon: "-122.42458269675265",
  osm_id: 256989698,
  osm_type: "way",
  place_id: 153828663
}
