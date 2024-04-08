import random
from flask import Flask, request, jsonify


app = Flask(__name__)
def load_vocab(file_path='/home/trangpi/Project/JointIDSF/wordle_words.txt'):
    with open(file_path, "r") as f:
        data = f.read().strip().split('\n')
        return data

vocab = load_vocab()

def match_word(token, target):
    """
    len(token) == len(target)
    Args:
        token:
        target:

    Returns:

    """
    char_match = []
    for i, key in enumerate(token):
        item = {"slot": i, "guess": key, "result": "absent"}
        if token[i] == target[i]:
            item['result'] = 'correct'
        elif token[i] in target:
            item['result'] = 'present'
        char_match.append(item)

    return char_match


def check_rule(token, len_word=5):
    if len(token) != len_word:
        return 1
    elif not token.isalpha():
        return 2
    else:
        return 3


@app.route('/random', methods=['GET'])
def predict():
    guess = request.args.get('guess')
    seed_int = request.args.get('seed')
    random.seed(int(seed_int))
    target = random.choice(vocab)
    print("target:", target)

    rule_result = check_rule(guess, len_word=5)
    if rule_result == 1:
        return jsonify({'error': 'Guess must be the same length as the word'})
    elif rule_result == 2:
        return jsonify({'error': '.Guess must only contain letters'})
    else:
        match = match_word(token=guess, target=target)
        return jsonify(match)







if __name__ == "__main__":
    app.run(debug=True)
    # random.seed(1234)
    # target = random.choice(vocab)
    # print(target)

