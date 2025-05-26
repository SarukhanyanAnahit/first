from random import randint, shuffle

QUESTIONS_COUNT = 5

def get_questions(fname):
  f = open(fname)
  return f.readlines()

def get_random_indexes(QUESTIONS_COUNT, qcount):
  indexes = []
  while len(indexes) < QUESTIONS_COUNT:
    ind = randint(0, qcount)
    if ind not in indexes:
      indexes.append(ind)
  return indexes

def get_game_questions(gq_list):
  final_questions = []
  for question in gq_list:
    tmp = {}
    q, a = question.split("?")
    tmp["question"] = q + "?"
    variants = a.split(",")
    tmp["correct"] = variants[0]
    shuffle(variants)
    tmp["variants"] = variants
    final_questions.append(tmp)
  return final_questions

def play(final_questions):
    count = 0
    print("\nStart the game!\n")
    for qobj in final_questions:
        print(qobj["question"])
        for v in qobj["variants"]:
            print(v)
        ans = input("Your answer: ")
        if ans == qobj["correct"]:
            count += 1
            print("Correct! You got %d/%d\n" % (count, len(final_questions)))
        else:
            print("Incorrect. The correct answer was", qobj["correct"])
            print("You got %d/%d\n" % (count, len(final_questions)))
    return count

def read_scoreboard(fname):
    scores = {}
    f = open(fname)
    lines = f.readlines()
    f.close()
    for line in lines:
        if " : " in line:
            parts = line.strip().split(" : ")
            if len(parts) == 2:
                uname = parts[0]
                xp = int(parts[1])
                scores[uname] = xp
    return scores

def write_top_score_board(fname, uname, xp):
    f = open(fname, "a")
    f.write(uname + " : " + str(xp) + "\n")
    f.close()
    print("Successfully saved.")

def add_question(fname):
    question = input("Enter your question (without '?'): ") + "?"
    correct = input("Enter the correct answer: ")
    v1 = input("Enter variant 1: ")
    v2 = input("Enter variant 2: ")
    f = open(fname, "a")
    f.write(question + correct + "," + v1 + "," + v2 + "\n")
    f.close()
    print("Question added.")

# Main Menu
choice = input("Do you want to play or add question? (play/add): ").lower()

if choice == "add":
    add_question("questions.txt")

elif choice == "play":
    username = input("Enter your username: ")

    f = open("top.txt")
    top_content = f.read().strip()
    f.close()

    if top_content != "":
        scores = read_scoreboard("top.txt")
    else:
        scores = {}

    if username in scores:
        print("You already have a score: %d" % scores[username])
        update = input("Do you want to try to beat it? (yes/no): ")
        if update.lower() != "yes":
            print("Okay, your previous score is kept.")
        else:
            questions = get_questions("questions.txt")
            indexes = get_random_indexes(QUESTIONS_COUNT, len(questions) - 1)
            game_questions_list = [questions[i].strip() for i in indexes]
            final_questions = get_game_questions(game_questions_list)
            xp = play(final_questions)
            print("End of the game! Your final score is: %d/%d" % (xp, len(final_questions)))
            if xp > scores[username]:
                scores[username] = xp
                print("New high score!")
            else:
                keep = input("Your previous score was better. Keep it? (yes/no): ")
                if keep.lower() != "yes":
                    scores[username] = xp
                    print("Score updated with new result.")
            write_top_score_board("top.txt", username, scores[username])
    else:
        questions = get_questions("questions.txt")
        indexes = get_random_indexes(QUESTIONS_COUNT, len(questions) - 1)
        game_questions_list = [questions[i].strip() for i in indexes]
        final_questions = get_game_questions(game_questions_list)
        xp = play(final_questions)
        print("End of the game! Your final score is: %d/%d" % (xp, len(final_questions)))
        scores[username] = xp
        write_top_score_board("top.txt", username, scores[username])

else:
    print("Invalid choice.")
