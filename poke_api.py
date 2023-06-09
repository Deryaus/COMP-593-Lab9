import requests
POKEMON_SEARCH_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    ability_list = search_for_pokemon('piKacHu  ')
    print(*ability_list, sep='\n')
    ability_list = search_for_pokemon(601)
    print(*ability_list, sep='\n')
    
# Accept a parameter that specifies the name of the Pokémon or PokéDex number.
def search_for_pokemon(search_term):
    """ Gets info about a specified Pokemon from the PokeAPI.

    Args:
        search_term (str): Pokemon name or pokedex number.

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Convert the parameter to a string.
    # Remove any leading and trailing whitespace characters
    # Convert to all lowercase letters.
    clean_string = str(search_term).strip().lower()
    # Send GET request to the poke api.
    print(f'Getting information for {clean_string}....', end='')
    resp_msg = requests.get(POKEMON_SEARCH_URL + clean_string)
    # Check whether the GET request was successful.
    if resp_msg.ok:
        print('success.')
        pokemon_dict = resp_msg.json()
        return pokemon_dict
    else:
        print('failure.')
        print(f'Response code: {resp_msg.status_code} {resp_msg.reason}')

if __name__ == '__main__':
    main()