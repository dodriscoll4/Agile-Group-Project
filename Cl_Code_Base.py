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
        if len(users_input) > 0 and all(char.isalnum() or char == '_' for char in users_input):
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
    with open("runners.txt") as connection:
        lines = connection.readlines()
    runners_name = []
    runners_id = []

    for line in lines:
        split_line = line.split(",")
        if len(split_line) == 2:  # this skips past any blank lines in txt
            runners_name.append(split_line[0])
            runners_id.append(split_line[1].strip())
    return runners_name, runners_id


def race_results(races_location):
    for i in range(len(races_location)):
        print(f"{i + 1}: {races_location[i]}")
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input - 1]
    runner_id, time_taken = reading_race_results(venue)
    return runner_id, time_taken, venue


def race_venues():
    with open("races.txt") as connection:
        lines = connection.readlines()
    races_location = []
    for line in lines:
        race_name = line.strip().split(',')[0]
        if race_name:
            races_location.append(race_name)
    return races_location


def winner_of_race(runner_id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(runner_id)):
        if quickest_time == time_taken[i]:
            winner = runner_id[i]
    return winner


def podium_position(runner_id, time_taken):
    first_place = None
    second_place = None
    third_place = None

    # Find the first place
    min_time = float('inf')
    for i in range(len(runner_id)):
        if time_taken[i] < min_time:
            min_time = time_taken[i]
            first_place = runner_id[i]

    # Find the second place
    min_time = float('inf')
    for i in range(len(runner_id)):
        if runner_id[i] != first_place and time_taken[i] < min_time:
            min_time = time_taken[i]
            second_place = runner_id[i]

    # Find the third place
    min_time = float('inf')
    for i in range(len(runner_id)):
        if runner_id[i] != first_place and runner_id[i] != second_place and time_taken[i] < min_time:
            min_time = time_taken[i]
            third_place = runner_id[i]

    return first_place, second_place, third_place


def display_races(runner_id, time_taken, venue, fastest_runner, podium_places):
    print(f"Results for {venue}")
    print(f"=" * 37)
    minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
    for i in range(len(runner_id)):
        print(f"{runner_id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    print(f"\n{fastest_runner} won the race.")
    print(f"\n1st Place: {podium_places[0]}"
          f"\n2nd Place: {podium_places[1]}"
          f"\n3rd Place: {podium_places[2]}")


def users_venue(races_location, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            break

    with open(f"{user_location}.txt", "w") as connection:
        races_location.append(user_location)

        time_taken = []
        updated_runners = []

        for i in range(len(runners_id)):
            time_taken_for_runner = read_integer(f"Time for {runners_id[i]} >> ")
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])

            # Append the results to the race file
            print(f"{runners_id[i]},{time_taken_for_runner}", file=connection)

    updating_races_file(races_location)


def updating_races_file(races_location):
    connection = open(f"races.txt", "a")
    new_race = races_location[-1]
    target_time = read_integer(f"Enter the target time for {new_race}: ")

    # Append the new race and its target time to races.txt
    print(f"{new_race}, {target_time}", file=connection)
    connection.close()


def competitors_by_county(names, ids):
    county_codes = {}
    with open('County_codes.txt') as file:
        for line in file:
            if not line.strip():  # Skip empty lines
                continue
            try:
                name, code = line.strip().split(", ")
                county_codes[code] = name
            except ValueError as e:
                print(f"Error splitting line: {line.strip()}. {e}")
                continue

    county_runners = {}
    for i in range(len(names)):
        county_code = ids[i][:2]
        if county_code not in county_runners:
            county_runners[county_code] = []
        county_runners[county_code].append(f"{names[i]} ({ids[i]})")

    sorted_counties = sorted(county_runners.items())
    for county_code, runners in sorted_counties:
        county_name = county_codes.get(county_code, "Unknown County")
        print(f"{county_name} runners")
        print("=" * 20)
        for runner in sorted(runners):
            print(runner)
        print()


def reading_race_results(location):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    runner_id = []
    time_taken = []
    for line in lines:
        if line.strip():
            split_line = line.strip("\n").split(",")
            runner_id.append(split_line[0])
            time_taken.append(int(split_line[1].strip("\n")))
    return runner_id, time_taken


def reading_race_results_of_relevant_runner(location):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    runner_id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        if len(split_line) == 2:  # this skips past any blank lines in txt
            runner_id.append(split_line[0])
            time_taken.append(int(split_line[1].strip("\n")))
    for i in range(len(runner_id)):
        if runner_id == runner_id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None


def displaying_winners_of_each_race(races_location):
    print("Race                  1st Place    2nd Place    3rd Place")
    print("=" * 57)
    for race in races_location:
        ids, time_taken = reading_race_results(race)
        podium = podium_position(ids, time_taken)
        print(f"{race:<22s}{podium[0]:<13}{podium[1]:<13}{podium[2]}")


def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    runner_id = runners_id[user_input - 1]
    return runner, runner_id


def convert_time_to_minutes_and_seconds(time_taken):
    minute = 60
    if isinstance(time_taken, int):
        # If time_taken is a single integer, convert it to a list
        time_taken = [time_taken]
    minutes = [time // minute for time in time_taken]
    seconds = [time % minute for time in time_taken]
    return minutes, seconds


def sorting_where_runner_came_in_race(location, time):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        if len(split_line) == 2:  # this skips past any blank lines in txt
            t = int(split_line[1].strip("\n"))
            time_taken.append(t)

    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)


def displaying_race_times_one_competitor(races_location, runner, runner_id):
    print(f"{runner} ({runner_id})")
    print(f"-" * 35)
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i])
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


def finding_name_of_winner(fastest_runner, runner_id, runners_name):
    runner = ""
    for i in range(len(runner_id)):
        if fastest_runner == runner_id[i]:
            runner = runners_name[i]
    return runner


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    winners = []
    runners = []
    for i, location in enumerate(races_location):
        runner_id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(runner_id, time_taken)
        name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")


def displaying_runners_who_have_not_gotten_podium(races_location, runners_name, runners_id):
    podium_runners = set()

    # Fetching podium runners
    for location in races_location:
        ids, _ = reading_race_results(location)
        podium = podium_position(ids, _)
        podium_runners.update(podium)

    # Finding non-podium runners
    non_podium_runners = [(runners_id[i], runners_name[i]) for i in range(len(runners_id)) if
                          runners_id[i] not in podium_runners]

    # Displaying non-podium runners
    print("Competitors who have not achieved a podium position in any race:")
    print("=" * 65)
    if non_podium_runners:
        for competitor_id, competitor_name in non_podium_runners:
            print(f"{competitor_name} ({competitor_id})")
    else:
        print("All competitors have achieved at least one podium position.")


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    menu = "1. Show the results for a race " \
           "\n2. Add results for a race " \
           "\n3. Show all competitors by county " \
           "\n4. Show the winner of each race " \
           "\n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race " \
           "\n7. Show all competitors who never got a podium place " \
           "\n8. Quit \n>>> "
    input_menu = read_integer_between_numbers(menu, 1, 8)

    while input_menu != 8:
        if input_menu == 1:
            runner_id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(runner_id, time_taken)
            podium_places = podium_position(runner_id, time_taken)
            display_races(runner_id, time_taken, venue, fastest_runner, podium_places)
        elif input_menu == 2:
            users_venue(races_location, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            displaying_winners_of_each_race(races_location)
        elif input_menu == 5:
            runner, runner_id = relevant_runner_info(runners_name, runners_id)
            displaying_race_times_one_competitor(races_location, runner, runner_id)
        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        elif input_menu == 7:
            displaying_runners_who_have_not_gotten_podium(races_location, runners_name, runners_id)
        print()
        input_menu = read_integer_between_numbers(menu, 1, 8)


if __name__ == '__main__':
    main()
