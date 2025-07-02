from random import randint, shuffle

QUESTIONS_COUNT = 5

class QuestionManager:
    def __init__(self, filename):
        self.__filename = filename

    def get_questions(self):
        with open(self.__filename) as f:
            return [line.strip() for line in f if line.strip()]

    def add_question(self):
        question = input("Please enter your question: ")
        correct = input("Please enter the correct answer: ")
        var1 = input("Please enter the incorrect variant: ")
        var2 = input("Please enter another variant: ")
        var3 = input("Please enter again another variant: ")
        if question[-1] != "?":
            question += "?"
        line = f"{question}{correct},{var1},{var2},{var3}"
        with open(self.__filename, "a") as f:
            f.write(line + "\n")
        print("Question added successfully.")

    def get_random_questions(self):
        all_questions = self.get_questions()
        indexes = set()
        while len(indexes) < QUESTIONS_COUNT:
            indexes.add(randint(0, len(all_questions) - 1))
        return [all_questions[i] for i in indexes]

    def parse_questions(self, raw_questions):
        parsed = []
        for q in raw_questions:
            try:
                question, answers = q.split("?")
                variants = answers.split(",")
                correct = variants[0]
                shuffle(variants)
                parsed.append({
                    "question": question + "?",
                    "variants": variants,
                    "correct": correct
                })
            except ValueError:
                print(f"Invalid question format skipped: {q}")
        return parsed


class ScoreBoard:
    def __init__(self, filename):
        self.__filename = filename
        self.__players = self.__load_scores()

    def __load_scores(self):
        scores = {}
        try:
            with open(self.__filename) as f:
                for line in f:
                    user, xp = line.strip().split(" : ")
                    scores[user] = int(xp)
        except FileNotFoundError:
            pass
        return scores

    def save_scores(self):
        sorted_players = sorted(self.__players.items(), key=lambda x: x[1], reverse=True)
        with open(self.__filename, "w") as f:
            for user, score in sorted_players:
                f.write(f"{user} : {score}\n")
        print("Scores saved successfully.")

    def update_score(self, username, score):
        self.__players[username] = score
        self.save_scores()

    def user_exists(self, username):
        return username in self.__players

    def get_all_scores(self):
        return self.__players.copy()


class Game:
    def __init__(self, question_file, top_file):
        self.__qm = QuestionManager(question_file)
        self.__sb = ScoreBoard(top_file)

    def __play(self):
        username = input("Enter your username: ")
        while self.__sb.user_exists(username):
            print("Your username already exists.")
            ans = input("Would you like to override your score (y/n)? ")
            if ans.lower() == "n":
                username = input("Enter your username: ")
            else:
                break

        raw_questions = self.__qm.get_random_questions()
        final_questions = self.__qm.parse_questions(raw_questions)

        score = 0
        print("\nStart the game!\n")
        for q in final_questions:
            print(q["question"])
            for option in q["variants"]:
                print(option)
            ans = input("Your answer: ")
            if ans == q["correct"]:
                score += 1
                print(f"Correct. You got {score}/{QUESTIONS_COUNT}")
            else:
                print(f"Incorrect. Correct answer: {q['correct']}")
                print(f"You got {score}/{QUESTIONS_COUNT}")
            print()

        print("Game over! Final score: ", f"{score}/{QUESTIONS_COUNT}")
        self.__sb.update_score(username, score)

    def run(self):
        mode = input("Would you like to play or add question (p/a): ")
        if mode.lower() == "p":
            self.__play()
        elif mode.lower() == "a":
            self.__qm.add_question()
        else:
            print("Invalid option. Please run the game again.")


if __name__ == "__main__":
    game = Game("../../oop/questions.txt", "top.txt")
    game.run()
