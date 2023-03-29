import requests
POKEMON_SEARCH_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    ability_list = search_for_pokemon('piKacHu  ')
    print(*ability_list, sep='\n')
    ability_list = search_for_pokemon(601)
    print(*ability_list, sep='\n')
    
# Accept a parameter that specifies the name of the Pokémon or PokéDex number.
def search_for_pokemon(search_term):
    """ Gets a list of pokemon abilities.

    Args:
        search_term (str): Pokemon name or pokedex number.

    Returns:
        list: List of Pokemon abilities.
    """
    # Converts the parameter to a string, removes any leading and trailing whitespace characters, and converts it to all lowercase letters.
    clean_string = str(search_term).strip().lower()
    # Send GET request to the poke api.
    print(f'Getting information for {clean_string}....', end='')
    resp_msg = requests.get(POKEMON_SEARCH_URL + clean_string)
    # Check whether the GET request was successful.
    if resp_msg.ok:
        print('success.')
        pokemon_dict = resp_msg.json()
        ability_list = [a['ability']['name'] for a in pokemon_dict['abilities']]
        return resp_msg.json
    else:
        print('failure.')
        print(f'Response code: {resp_msg.status_code} {resp_msg.reason}')

if __name__ == '__main__':
    main()