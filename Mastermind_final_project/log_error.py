import datetime


def log_error(error_type):
    """
    Function -- log_error
        log errors occurred to a file
    Parameters:
        error_type (str) -- the name of the error type
    Returns None
    """
    # get the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # build the error message
    error_message = f"{current_time}   Error Type: {error_type}\n"

    # write the error message to the file
    with open("mastermind_errors.err", "a") as out_file:
        out_file.write(error_message)