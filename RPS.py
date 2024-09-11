import random

def player(prev_play, opponent_history=[]):
    # Keep track of the opponent's history
    opponent_history.append(prev_play)

    if len(opponent_history) == 0 or prev_play == '':
        # First move, choose randomly
        return random.choice(['R', 'P', 'S'])

    # Analyze the opponent's last moves
    last_play = opponent_history[-1]
    
    # Simple counter-strategy: beat the opponent's last move
    if last_play == 'R':
        return 'P'  # Paper beats Rock
    elif last_play == 'P':
        return 'S'  # Scissors beat Paper
    elif last_play == 'S':
        return 'R'  # Rock beats Scissors

    # Default to random choice if something goes wrong
    return random.choice(['R', 'P', 'S'])