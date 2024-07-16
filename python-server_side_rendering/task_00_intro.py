""""
simple templating program
"""

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
        raise TypeError(f"Invalid input type: {type(template)} template must be a string")
    
    if not isinstance(attendees, list):
        raise TypeError(f"Invalid input type: {type(attendees)} attendees must be a list of dictionaries")
    
    if not all(isinstance(elem, dict) for elem in attendees):
        raise ValueError("No data provided, no output files generated.")

    if template == "":
        raise ValueError("Template is empty, no output files generated.")
    
    input = template
    keys = ["name", "event_title", "event_date", "event_location"]
    index = 1

    for attendee in attendees:
        for key in attendee:
            replacement = attendee[key]
            expression = "{" + key + "}"

            if key not in keys:
                replacement = "N/A"

            if replacement in ["", None]:
                replacement = "N/A"

            input = input.replace(expression, replacement)
        with open("input_" + str(index) + ".txt", "w", encoding="utf-8") as file:
            file.write(input)
        index += 1