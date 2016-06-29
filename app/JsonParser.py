def extract_file(filename):
    """ Returns the string equivalent of a file """

    string_output = None         #Placeholder

    with open(filename, "r") as file_contents:       #Opens the file in filename in read mode (r)
        string_output = file_contents.read().replace('\n','')   #Extract file and replace end lines with nothing

    return string_output

def extract_json(json_string):
    """ Returns a json object for the json string provided """

    json_output = None                      #Placeholder
    json_output = json.loads(json_string)   #Get json object

    return json_output

def get_json(filename):
    """ Returns a json object from the given file """

    json_object = None      #Placeholder
    json_string = None      #Placeholder

    json_string = extract_file(filename)
    json_object = extract_json(json_string)

    return json_object