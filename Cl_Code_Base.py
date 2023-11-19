def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if mini <= users_input <= maximum:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry - numbers only please")


def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input


def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry - numbers only please")


def runners_data():
    with open("runners.txt") as input:
        lines = input.readlines()
    runners_name = []
    runners_id = []

    for line in lines:
        split_line = line.split(",")
        if len(split_line) == 2:  # this skips past blank lines in txt
            runners_name.append(split_line[0])
            runners_id.append(split_line[1].strip())
    return runners_name, runners_id


def race_results(races_location):
    for i in range(len(races_location)):
        print(f"{i + 1}: {races_location[i]}")
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input - 1]
    id, time_taken = reading_race_results(venue)
    return id, time_taken, venue


def race_venues():
    with open("races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        race_name = line.strip().split(',')[0]
        if race_name:
            races_location.append(race_name)
    return races_location


def winner_of_race(id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(id)):
        if quickest_time == time_taken[i]:
            winner = id[i]
    return winner


def podium_position(id, time_taken):
    first_place = None
    second_place = None
    third_place = None

    # Find the first place
    min_time = float('inf')
    for i in range(len(id)):
        if time_taken[i] < min_time:
            min_time = time_taken[i]
            first_place = id[i]

    # Find the second place
    min_time = float('inf')
    for i in range(len(id)):
        if id[i] != first_place and time_taken[i] < min_time:
            min_time = time_taken[i]
            second_place = id[i]

    # Find the third place
    min_time = float('inf')
    for i in range(len(id)):
        if id[i] != first_place and id[i] != second_place and time_taken[i] < min_time:
            min_time = time_taken[i]
            third_place = id[i]

    return first_place, second_place, third_place


def display_races(id, time_taken, venue, fastest_runner, podium_places):
    print(f"Results for {venue}")
    print(f"="*37)
    minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
    for i in range(len(id)):
        print(f"{id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    print(f"\n{fastest_runner} won the race.")
    print(f"\n1st Place: {podium_places[0]}"
          f"\n2nd Place: {podium_places[1]}"
          f"\n3rd Place: {podium_places[2]}")


def users_venue(races_location, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            break
    connection = open(f"{user_location}.txt", "a")
    races_location.append(user_location)
    time_taken = []
    updated_runners = []
    for i in range(len(runners_id)):
        time_taken_for_runner = read_integer(f"Time for {runners_id[i]} >> ")
        if time_taken_for_runner == 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner},", file=connection)
    connection.close()


def updating_races_file(races_location):
    connection = open(f"races.txt", "w")
    for i in range(len(races_location)):
        print(races_location[i], file=connection)
    connection.close()


def competitors_by_county(name, id):
    print("Cork runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({id[i]})")
    print("Kerry runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({id[i]})")


def reading_race_results(location):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        if line.strip():
            split_line = line.strip("\n").split(",")
            id.append(split_line[0])
            time_taken.append(int(split_line[1].strip("\n")))
    return id, time_taken


def reading_race_results_of_relevant_runner(location, runner_id):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        if len(split_line) == 2:  # this skips past blank lines in txt
            id.append(split_line[0])
            time_taken.append(int(split_line[1].strip("\n")))
    for i in range(len(id)):
        if runner_id == id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None


def displaying_winners_of_each_race(races_location):
    print("Venue             Looser")
    print("="*24)
    for i in range(len(races_location)):
        id, time_taken = reading_race_results(races_location[i])
        fastest_runner = winner_of_race(id, time_taken)
        print(f"{races_location[i]:<18s}{fastest_runner}")


def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input -1]
    return runner, id


def convert_time_to_minutes_and_seconds(time_taken):
    MINUTE = 60
    if isinstance(time_taken, int):
        # If time_taken is a single integer, convert it to a list
        time_taken = [time_taken]
    minutes = [time // MINUTE for time in time_taken]
    seconds = [time % MINUTE for time in time_taken]
    return minutes, seconds


def sorting_where_runner_came_in_race(location, time):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        if len(split_line) == 2:  # this skips past blank lines in txt
            t = int(split_line[1].strip("\n"))
            time_taken.append(t)

    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)


def displaying_race_times_one_competitor(races_location, runner, id):
    print(f"{runner} ({id})")
    print(f"-"*35)
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i], id)
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


def finding_name_of_winner(fastest_runner, id, runners_name):
    runner = ""
    for i in range(len(id)):
        if fastest_runner == id[i]:
            runner = runners_name[i]
    return runner


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    winners = []
    runners = []
    for i, location in enumerate(races_location):
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")


def displaying_runners_who_have_not_gotten_podium():
    """This still needs to be implemented"""


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race " \
           "\n2. Add results for a race " \
           "\n3. Show all competitors by county " \
           "\n4. Show the winner of each race " \
           "\n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race " \
           "\n7. Show all competitors who never got a podium place " \
           "\n8. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 8)

    while input_menu != 8:
        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            podium_places = podium_position(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner, podium_places)
        elif input_menu == 2:
            users_venue(races_location, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            displaying_winners_of_each_race(races_location)
        elif input_menu == 5:
            runner, id = relevant_runner_info(runners_name, runners_id)
            displaying_race_times_one_competitor(races_location, runner, id)
        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        elif input_menu == 7:
            displaying_runners_who_have_not_gotten_podium()
        print()
        input_menu = read_integer_between_numbers(MENU, 1, 8)
    updating_races_file(races_location)


if __name__ == '__main__':
    main()
