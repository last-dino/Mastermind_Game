import turtle
import random
from Point import Point
from Marble import Marble
from Button import Button
from GuessBoard import GuessBoard
from BullsAndCows import BullsAndCows
from log_error import log_error
import GUI

NUMBER_OF_COLOR = 6
ROW = 10
COLUMN = 4
COLORS = ["blue", "red", "green", "yellow", "purple", "black"]
LEADERBOARD_FILENAME = "leaderboard.txt"
ERROR_LOG_FILENAME = "mastermind_errors.err"


def main():
    """
    Function -- main
        calls the mastermind_game function to play the Mastermind game
    Parameters: None
    Returns: None
    """
    mastermind_game()


def mastermind_game():
    """
    Function -- mastermind_game
        initializes game GUI and game components, gets player's name,
        generates the secret code, and start running the game by
        calling the making_guesses function
    Parameters: None
    Returns: None
    """
    turtle.hideturtle()

    # create graphics
    GUI.create_canvas()
    GUI.draw_frames()
    GUI.create_leaderboard(LEADERBOARD_FILENAME)

    # create game components
    buttons = create_control_panel()
    game = GuessBoard(ROW, COLUMN)
    checker = BullsAndCows(ROW, COLUMN)

    player_name = get_player_name()  # get player's name
    secret_code = generate_secret_code()  # generate code

    # start running the game
    making_guesses(game, checker, player_name, buttons, secret_code)


def generate_secret_code() -> list:
    """
    Function -- generate_secret_code
        generates a random secret code for the game.
    Parameters: None
    Returns a list of strings representing the
        colors in the secret code
    """
    secret_code = []

    # generate a list of non-repetitive numbers
    indices = random.sample(range(NUMBER_OF_COLOR), COLUMN)

    # append the corresponding colors at the indices to the secret code
    for i in indices:
        secret_code.append(COLORS[i])

    return secret_code


def get_player_name() -> str:
    """
    Function -- get_player_name
        prompts the player to enter their name
    Parameters: None
    Returns a str of the player's name
    """
    player_name = ""
    valid = False

    while not valid:  # keep prompting if input is invalid
        player_name = turtle.textinput("Welcome to Mastermind!", "Your name:")
        if player_name:
            valid = True

    return player_name


def create_control_panel() -> list:
    """
    Function -- create_control_panel
        creates the control panel with interactive buttons
    Parameters: None

    Returns a list that's made of button objects and marble objects
        representing all the buttons in the control panel
    """
    # add three decision buttons to the list
    buttons = [Button(Point(60, -325), "checkbutton.gif"),
               Button(Point(150, -325), "xbutton.gif"),
               Button(Point(300, -325), "quit.gif", 40)]

    x_spacing = 65  # spacing between the color buttons
    x, y = -350, -330  # position of the first color button

    for i in range(NUMBER_OF_COLOR):  # add color buttons to the list
        buttons.append(Marble(Point(x, y), COLORS[i]))
        x += x_spacing

    for each in buttons:  # render the buttons
        each.draw()

    return buttons


def making_guesses(game: GuessBoard, checker: BullsAndCows, player_name: str, buttons: list, secret_code: list):
    """
    Function -- making_guesses
        processes player interactions of the game
    Parameters:
        game (GuessBoard) -- representing all the guesses allowed in the game
        checker (BullsAndCows) -- bulls and cows for all the guesses
        player_name (str) -- the player's name
        buttons (list) -- a list of buttons of the control panel
        secret_code (list) -- a list of strings representing the secret code
    Returns None
    """
    # keep listening to onclick event while the game is still going
    while game.get_guesses() < ROW and not game.get_won_status() and not game.get_quit_status():
        # subscribe to the button click event
        turtle.onscreenclick(lambda x, y: button_clicker(x, y, game, checker, buttons, secret_code), 1)
        turtle.update()  # Update the window

    if game.get_guesses() >= ROW or game.get_won_status() or game.get_quit_status():

        # display winner and add player to leaderboard when win
        if game.get_won_status():
            GUI.display_gif("winner.gif")
            add_to_leaderboard(game.get_guesses(), player_name)

        # display quit message when quit
        elif game.get_quit_status():
            GUI.display_gif("quitmsg.gif")

        # display lose and reveal the secret code when lose
        else:
            GUI.display_gif("Lose.gif")
            show_secret_code(secret_code)

    turtle.bye()  # exit the game


def button_clicker(x, y, game: GuessBoard, checker: BullsAndCows, buttons: list, secret_code: list):
    """
    Function -- button_clicker
        Handles button clicks during the game
    Parameters:
        x (float) -- the x-coordinate of the click
        y (float) -- the y-coordinate of the click
        game (GuessBoard) -- representing all the guesses allowed in the game
        checker (BullsAndCows) -- bulls and cows for all the guesses
        buttons (list) -- a list of buttons of the control panel
        secret_code (list) -- a list of strings representing the secret code
    Returns None
    """
    # only process the click if the game is still going
    if game.get_guesses() < ROW and not game.get_won_status():
        selection = ""
        
        for button in buttons:  # find out which button is clicked
            if button.clicked_in_region(x, y):
                selection = button.get_color()

        # process base on what the player clicked on
        selection_engine(selection, game, checker, buttons, secret_code)


def selection_engine(selection: str, game: GuessBoard, checker: BullsAndCows, buttons: list, secret_code: list):
    """
    Function -- selection_engine
        processes what the player clicked on
    Parameters:
        selection (str) -- what the player clicked on
        game (GuessBoard) -- representing all the guesses allowed in the game
        checker (BullsAndCows) -- bulls and cows for all the guesses
        buttons (list) -- a list of buttons of the control panel
        secret_code (list) -- a list of strings representing the secret code
    Returns None
    """
    if selection in COLORS:  # if the player click on a color button
        for button in buttons:

            # find the button and check if it's already been clicked
            if button.get_color() == selection and not button.get_empty_state():
                success = game.on_color_click(selection)

                # if the click is successful, empty the button
                # to indicate it has already been clicked
                if success:
                    button.draw_empty()

    # if it's a legal checkbutton click
    elif selection == "checkbutton" and game.get_count_within_row() == COLUMN:
        # return a list of the current guess
        current_row = game.on_green_check_button_click()

        for each in buttons:  # reset buttons in control panel
            each.draw()

        # get bulls and cows for current guess
        count_bulls_and_cows(checker, current_row, secret_code, game.get_guesses() - 1)

        # set win status to true if the guess is correct
        if current_row == secret_code:
            game.set_won_status_to_true()

    elif selection == "xbutton":  # if cancel button is clicked
        game.on_red_cross_button_click()

        for each in buttons:  # reset the buttons in the control panel
            each.draw()

    elif selection == "quit":  # if quit button is clicked
        game.set_quit_status_to_true()

    # if no button is clicks or the button clicked is not allowed, do nothing
    else:
        return


def count_bulls_and_cows(checker: BullsAndCows, current_row: list, secret_code: list, guess: int):
    """
    Function -- count_bulls_and_cows
        counts bulls and cows for a guess
    Parameters:
        checker (BullsAndCows) -- bulls and cows for all the guesses
        current_row (list) -- the current guess row
        secret_code (list) -- a list of strings representing the secret code
        guess (int) -- The index of the current guess
    Returns None
    """
    bulls, cows = 0, 0  # initialize the counts to 0

    for i in range(COLUMN):
        if current_row[i] == secret_code[i]:
            bulls += 1
        elif current_row[i] in secret_code:
            cows += 1

    # fill colors base on the counts
    checker.fill_counts(bulls, cows, guess)


def show_secret_code(secret_code: list):
    """
    Function -- show_secret_code
        pops out a text window to reveal the secret code
    Parameters:
        secret_code (list) -- a list of strings representing the secret code
    Returns None
    """
    colors = " ".join(secret_code)  # convert list to string
    turtle.textinput("Secret Code Was", colors)


def add_to_leaderboard(score: int, player_name: str):
    """
    Function -- add_to_leaderboard
        adds the player's score and name to the leaderboard
    Parameters:
        score (int) -- the player's score
        player_name (str) -- the player's name
    Returns None
    """
    try:
        with open(LEADERBOARD_FILENAME, "r") as in_file:  # read from file
            lines = in_file.readlines()[2:]
            all_players = []
            for line in lines:
                try:  # store valid previous players in a list
                    cur_score, cur_name = line.strip().split(":")
                    cur_score = int(cur_score.strip())
                    cur_name = cur_name.strip()
                    all_players.append({"score": cur_score, "name": cur_name})
                except ValueError as e:
                    log_error(type(e).__name__)  # log error
                    continue

    except FileNotFoundError as e:
        log_error(type(e).__name__)  # log error
        # pop up error gif
        GUI.display_gif("leaderboard_error.gif")

    # if there's no previous player, just add the player's info
    if not all_players:
        all_players.append({"score": score, "name": player_name})

    # otherwise, insert player's info ordered by the scores
    else:
        added = False  # set flag
        for i in range(len(all_players)):
            if all_players[i]["score"] >= score:  # make sure the highest score on top
                all_players.insert(i, {"score": score, "name": player_name})
                added = True
                break

        if not added:  # if the current score is the lowest
            all_players.append({"score": score, "name": player_name})

    with open(LEADERBOARD_FILENAME, "w") as out_file:  # write to the file
        out_file.write("Leaders:\n\n")
        for i in range(min(5, len(all_players))):  # only keep the top 5
            out_file.write(f"{all_players[i]['score']} : {all_players[i]['name']}\n")


if __name__ == "__main__":
    main()
