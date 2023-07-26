import streamlit as st
import datetime
import pytz
from utils.predicthq import get_api_key, get_predicthq_client
from utils.code_examples import get_code_example
from typing import Iterable

def show_sidebar_options():
    locations = [

        {
            "id": "melbourne",
            "name": "Melbourne, AU",
            "address": "452 Flinders Street",
            "lat": -37.8187466,
            "lon": 144.9583122,
            "tz": "Australia/Melbourne",
            "units": "metric",
        }
    ]

#     # Work out which location is currently selected
#     index = 2

#     if "location" in st.session_state:
#         for idx, location in enumerate(locations):
#             if st.session_state["location"]["id"] == location["id"]:
#                 index = idx
#                 break

#     location = st.sidebar.selectbox(
#         "Hotel",
#         locations,
#         index=index,
#         format_func=lambda x: x["name"],
#         help="Select the hotel location.",
#         disabled=get_api_key() is None,
#         key="location",
#     )

#     # Prepare the date range (today + 30d as the default)
#     tz = pytz.timezone(location["tz"])
#     today = datetime.datetime.now(tz).date()
#     date_options = [
#         {
#             "id": "next_7_days",
#             "name": "Next 7 days",
#             "date_from": today,
#             "date_to": today + datetime.timedelta(days=7),
#         },
#         {
#             "id": "next_30_days",
#             "name": "Next 30 days",
#             "date_from": today,
#             "date_to": today + datetime.timedelta(days=30),
#         },
#         {
#             "id": "next_90_days",
#             "name": "Next 90 days",
#             "date_from": today,
#             "date_to": today + datetime.timedelta(days=90),
#         },
#     ]

#     # Work out which date is currently selected
#     index = 0  # Default to next 90 days

#     if "daterange" in st.session_state:
#         for idx, date_option in enumerate(date_options):
#             if st.session_state["daterange"]["id"] == date_option["id"]:
#                 index = idx
#                 break

#     st.sidebar.selectbox(
#         "Date Range",
#         date_options,
#         index=index,
#         format_func=lambda x: x["name"],
#         help="Select the date range for fetching event data.",
#         disabled=get_api_key() is None,
#         key="daterange",
#     )

#     # Use an appropriate radius unit depending on location
#     radius_unit = (
#         "mi" if "units" in location and location["units"] == "imperial" else "km"
#     )

#     st.session_state.suggested_radius = fetch_suggested_radius(
#         location["lat"], location["lon"], radius_unit=radius_unit
#     )

#     # Allow changing the radius if needed (default to suggested radius)
#     # The Suggested Radius API is used to determine the best radius to use for the given location and industry
#     st.sidebar.slider(
#         f"Suggested Radius around hotel ({radius_unit})",
#         0.0,
#         10.0,
#         st.session_state.suggested_radius.get("radius", 2.0),
#         0.1,
#         help="[Suggested Radius Docs](https://docs.predicthq.com/resources/suggested-radius)",
#         key="radius",
#     )


# @st.cache_data
# def fetch_suggested_radius(lat, lon, radius_unit="mi", industry="accommodation"):
#     phq = get_predicthq_client()
#     suggested_radius = phq.radius.search(
#         location__origin=f"{lat},{lon}", radius_unit=radius_unit, industry=industry
#     )

#     return suggested_radius.to_dict()


# def show_map_sidebar_code_examples():
#     st.sidebar.markdown("## Code examples")

#     # The code examples are saved as markdown files in docs/code_examples
#     examples = [
#         {"name": "Suggested Radius API", "filename": "suggested_radius_api"},
#         {
#             "name": "Features API (Predicted Attendance aggregation)",
#             "filename": "features_api",
#         },
#         {"name": "Count of Events", "filename": "count_api"},
#         {"name": "Demand Surge API", "filename": "demand_surge_api"},
#         {"name": "Search Events", "filename": "events_api"},
#         {"name": "Python SDK for PredictHQ APIs", "filename": "python_sdk"},
#     ]

#     for example in examples:
#         with st.sidebar.expander(example["name"]):
#             st.markdown(get_code_example(example["filename"]))

    # st.sidebar.caption(
    #     "Get the code for this app at [GitHub](https://github.com/predicthq/streamlit-accommodation-demo)"
    # )
    # Work out which location is currently selected
    index = 0

    if "location" in st.session_state:
        for idx, location in enumerate(locations):
            if st.session_state["location"]["id"] == location["id"]:
                index = idx
                break

    location = st.sidebar.selectbox(
        "Location",
        locations,
        index=index,
        format_func=lambda x: x["name"],
        help="Select the location.",
        disabled=get_api_key() is None,
        key="location",
    )

    # Prepare the date range (today + 30d as the default)
    tz = pytz.timezone(location["tz"])
    today = datetime.datetime.now(tz).date()
    date_options = [
        {
            "id": "next_7_days",
            "name": "Next 7 days",
            "date_from": today,
            "date_to": today + datetime.timedelta(days=7),
        },
        {
            "id": "next_30_days",
            "name": "Next 30 days",
            "date_from": today,
            "date_to": today + datetime.timedelta(days=30),
        },
        {
            "id": "next_90_days",
            "name": "Next 90 days",
            "date_from": today,
            "date_to": today + datetime.timedelta(days=90),
        },
    ]

    # Work out which date is currently selected
    index = 2  # Default to next 90 days

    if "daterange" in st.session_state:
        for idx, date_option in enumerate(date_options):
            if st.session_state["daterange"]["id"] == date_option["id"]:
                index = idx
                break

    st.sidebar.selectbox(
        "Date Range",
        date_options,
        index=index,
        format_func=lambda x: x["name"],
        help="Select the date range for fetching event data.",
        disabled=get_api_key() is None,
        key="daterange",
    )

    # Use an appropriate radius unit depending on location
    radius_unit = (
        "mi" if "units" in location and location["units"] == "imperial" else "km"
    )

    st.session_state.suggested_radius = fetch_suggested_radius(
        location["lat"], location["lon"], radius_unit=radius_unit
    )

    # Allow changing the radius if needed (default to suggested radius)
    # The Suggested Radius API is used to determine the best radius to use for the given location and industry
    st.sidebar.slider(
        f"Suggested Radius around location ({radius_unit})",
        0.0,
        10.0,
        2.0,
        0.1,
        help="[Suggested Radius Docs](https://docs.predicthq.com/resources/suggested-radius)",
        key="radius",
    )


@st.cache_data
def fetch_suggested_radius(lat, lon, radius_unit="mi", industry="retail"):
    phq = get_predicthq_client()
    suggested_radius = phq.radius.search(
        location__origin=f"{lat},{lon}", radius_unit=radius_unit, industry=industry
    )

    return suggested_radius.to_dict()


# def show_map_sidebar_code_examples():
#     st.sidebar.markdown("## Code examples")

#     # The code examples are saved as markdown files in docs/code_examples
#     examples = [
#         {"name": "Suggested Radius API", "filename": "suggested_radius_api"},
#         {
#             "name": "Features API (Predicted Attendance aggregation)",
#             "filename": "features_api",
#         },
#         {"name": "Count of Events", "filename": "count_api"},
#         {"name": "Demand Surge API", "filename": "demand_surge_api"},
#         {"name": "Search Events", "filename": "events_api"},
#         {"name": "Python SDK for PredictHQ APIs", "filename": "python_sdk"},
#     ]

# for example in examples:
#     with st.sidebar.expander(example["name"]):
#         st.markdown(get_code_example(example["filename"]))