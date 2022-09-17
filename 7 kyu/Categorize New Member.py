def open_or_senior(data):
    return ['Senior' if person[0] >= 55 and person[1] > 7 else 'Open' for person in data]

#[0] integer for the persons age
#[1] integer for the persons handicap
#If a person is over 55 and has a handicap greater than 7 they are a senior otherwise Open