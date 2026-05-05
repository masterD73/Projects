# Reviewer: Alex.
from statistics import mean
from csv import reader, writer as wrt

AGE = 1
VACCINATED = 6
HOSP_LENGTH = 4


def user_input(original):
    """
    Filters the requested columns by the user to a new csv file.
    :param original: The original file to get  the data from.
    :return: None.
    """
    rows = []
    print('Enter filters (Gender, Min age, Max age, Vaccinated):')
    requested = [row.strip().lower() for row in input().split(",")]
    with open(original, 'r') as org:
        csv_file = reader(org)
        header = next(csv_file)
        with open(f'filtered.csv', 'w', newline='') as file:
            write = wrt(file)
            for row in csv_file:
                rows.append(row)
            write.writerow(header)
            for row in rows:
                if row[0].lower() == requested[0] and \
                        int(requested[1]) <= int(row[1]) <= int(requested[2]) and \
                        row[6].lower() == requested[3]:
                    write.writerow(row)


def csv_read(file_name):
    """
    Read the particular csv and print min/max age of vaccinated/not vaccinated
    and the mean hospitalization of all patients.
    :param file_name: csv name or path.
    :return: Tuple of printed values.
    """
    with open(file_name, 'r') as file:
        csv_file = reader(file)
        next(csv_file)
        rows = []
        for row in csv_file:
            rows.append(row)

    max_age_vac = max(int(row[AGE]) for row in rows if row[VACCINATED] == 'Y')
    max_age_no_vac = max(int(row[AGE]) for row in rows if row[VACCINATED] == 'N')
    min_age_vac = min(int(row[AGE]) for row in rows if row[VACCINATED] == 'Y')
    min_age_no_vac = min(int(row[AGE]) for row in rows if row[VACCINATED] == 'N')
    mean_hosp_len = mean([int(row[HOSP_LENGTH]) for row in rows])

    print('Max age of vaccinated people:', max_age_vac)
    print('Max age of not vaccinated people:', max_age_no_vac)
    print('Min age of vaccinated people:', min_age_vac)
    print('Min age of not vaccinated people:', min_age_no_vac)
    print('Mean hospitalization length:', mean_hosp_len)
    return min_age_vac, min_age_no_vac, max_age_vac, max_age_no_vac, mean_hosp_len


def main():
    file_path = 'corona.csv'
    csv_read(file_path)
    user_input(file_path)


if __name__ == '__main__':
    main()
