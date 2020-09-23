# INCOMPLETE
def uncover_spy(n, trust):
    # SPY
    # Doesn't trust anyone
    # Is trusted by everyone
    # Works alone

    # HASH MAP
    # For each person, store the people they trust.

    # CHECK IF SPY
    # Find people that occur in every key's list of values
    # Then check all those people individually to see if they trust anyone
    # if they do return that person's identified else return -1

    hash_map = {}

    # Populate the hash map with all the people
    for i in range(n + 1):
        if i == 0:
            continue
        if i not in hash_map:
            hash_map[i] = [i]

    # Populate the hash map with each person N trusts
    for i in trust:
        person = i[0]
        trustee = i[1]
        hash_map[person].append(trustee)

    # if len of hash_map[some_index] = 0, then they trust no one.
    # check if that person occurs in every key's value

    possible_spies = []

    for key in hash_map:
        if len(hash_map[key]) == 1:
            possible_spies.append(key)

    print(hash_map)
    print(possible_spies)

    if len(possible_spies) > 0:
        for key in possible_spies:
            print(key)
            if any(key in val for val in hash_map.values()) == True:
                return key

    # for i in possible_spies:
    #     for x in hash_map[i]:
    #         if x != i:
    #             return

    return -1