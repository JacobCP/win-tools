import os
import pandas as pd

from tool_helpers import win_explorer

TESTING = False

if TESTING:
    events_file = "C:/Users/chaim/OneDrive/daily-manager/Computers/current projects/simchas notifications app/schema_using/testing_events.csv"
else:
    events_file = win_explorer.get_windows_file()
    print(events_file)

events_df = pd.read_csv(events_file)

if TESTING:
    chosen_date = "2021-10-30"
else:
    chosen_date = win_explorer.get_string(
        "Choose Date", "Events for which date? (yyyy-mm-dd format)"
    )
    print(chosen_date)

events_from_date_df = events_df.query(f"event_date=='{chosen_date}'")
events_from_date_df = events_from_date_df.sort_values("host")

output_string = ""

# get all the unique event_groups
all_event_groups = list(events_from_date_df["event_groups"])
all_event_groups = ",".join(all_event_groups).split(",")
all_event_groups = list(set(all_event_groups))
all_event_groups = ",".join(all_event_groups)


# create the general message HTML string
general_message_template = """*|INTERESTED:Kehillos:{all_event_groups}|*
Here are the simchos publicly posted in one or more Kehillos for this coming shabbos:
*|ELSE:|*
There are no simchos publicly posted in any Kehillos for this coming shabbos.
*|END:INTERESTED|*"""

output_string += general_message_template.format(all_event_groups=all_event_groups)
output_string += "\n\n"
output_string += "<ul>\n"

# create the individual HTML strings

list_item_template = """*|INTERESTED:Kehillos:{event_groups}|*
    <li>
        <b>Who: </b>{host} <b>Simcha: </b>{event_type} <b>Where: </b>{location} <b>Notes: </b>{notes} 
    </li>
*|END:INTERESTED|*"""

for _, event_from_date in events_from_date_df.iterrows():
    event_from_date = event_from_date.to_dict()
    event_formatted = list_item_template.format(**event_from_date)
    output_string += event_formatted
    output_string += "\n\n"
output_string += "</ul>\n"

with open(os.path.join(os.path.dirname(events_file), "html.txt"), "w") as f:
    f.write(output_string)
