""""
simple templating program
"""
import logging
import sys

def generate_invitations(template, attendees):
    """
    generates personalized invitations

    attr:
        input (str) - template
        keys (object) - list of keys
        index (int) - index of attendees starting from one

    args:
        template (str) - template
        attendees (object) - list of attendees
    """

    if not isinstance(template, str):
        logging.error(f"invalid input type: {type(template)}")
        sys.exit()
    
    if not isinstance(attendees, list):
        logging.error(f"invalid input type: {type(attendees)}")
        sys.exit()
    
    if not all(isinstance(elem, dict) for elem in attendees):
        logging.error("No data provided, no output files generated.")
        sys.exit()

    if template == "":
        logging.error("Template is empty, no output files generated.")
        sys.exit()
    
    keys = ["name", "event_title", "event_date", "event_location"]
    index = 1

    for attendee in attendees:
        input = template
        for key in keys:
            try:
                expression = "{" + key + "}"
                replacement = attendee[key]

                if key not in attendee:
                    replacement = "N/A"

                if replacement in ["", None]:
                    replacement = "N/A"
            except KeyError:
                replacement = "N/A"

            input = input.replace(expression, replacement)
        with open("output_" + str(index) + ".txt", "w", encoding="utf-8") as file:
            file.write(input)
        index += 1