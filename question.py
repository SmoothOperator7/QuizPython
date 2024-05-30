# Programme Python pour créer une interface graphique simple
from tkinter import *
from tkinter import messagebox as mb
import json

# classe pour définir les composants de l'interface graphique
class Quiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        # nombre de questions
        self.data_size = len(question)
        self.correct = 0

#Affiche le résultat elle compte le nombre de bonnes et mauvaises réponses puis les affiche à la fin dans une boîte de message
    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Bonnes réponses : {self.correct}"
        wrong = f"Mauvaises réponses : {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score : {score}%"
        # Affiche une boîte de message pour afficher le résultat
        mb.showinfo("Résultat", f"{result}\n{correct}\n{wrong}")

# vérifie la réponse après avoir cliqué sur Suivant.
    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

#vérifie la réponse de la question actuelle en appelant check_ans et le numéro de la question.
    def next_btn(self):
        # Vérifie si la réponse est correcte
        if self.check_ans(self.q_no):
            self.correct += 1
            #Si correct feedback en vert
            self.display_feedback("Correct", "green")
        else:
            #Si fausse feedback en rouge
            self.display_feedback("Faux", "red")
        # Déplacer vers la prochaine question après un court délai
        gui.after(2000, self.next_question)

    # Méthode pour afficher un feedback coloré
    def display_feedback(self, message, color):
        feedback = Label(gui, text=message, width=8, font=("ariel", 16, "bold"), fg=color)
        feedback.place(x=600, y=360)
        # Retirer le feedback après un court délai
        gui.after(2000, feedback.destroy)

    # Méthode pour passer à la question suivante
    def next_question(self):
        # Passe à la question suivante en incrémentant le compteur q_no
        self.q_no += 1
        # vérifie si la taille de q_no est égale à la taille des données
        if self.q_no == self.data_size:
            self.display_result()
            #détruit l'interface graphique
            gui.destroy()
        else:
            # affiche la question suivante
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(gui, text="Suivant", command=self.next_btn, width=10, bg="blue", fg="white", font=("ariel", 20, "bold"))
        next_button.place(x=950, y=310)
        quit_button = Button(gui, text="Quitter", command=gui.destroy, width=10, bg="black", fg="white", font=("ariel", 20, "bold"))
        quit_button.place(x=950, y=410)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        q_no = Label(gui, text=question[self.q_no], width=75,font=('ariel', 20, 'bold'), anchor='w')
        q_no.place(x=300, y=100)

    def display_title(self):
        title = Label(gui, text="Quiz World SKG", width=75, bg="blue", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 280
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=(150), y=y_pos)
            y_pos += 50
        return q_list

# Créer une fenêtre GUI
gui = Tk()
# définir la taille de la fenêtre GUI
gui.geometry("1280x720")
# définir le titre de la fenêtre
gui.title("Quiz STEPHANNE")
# obtenir les données depuis le fichier json
with open('data.json') as f:
    data = json.load(f)
# définir la question, les options, et la réponse
question = (data['question'])
options = (data['options'])
answer = (data['answer'])
# créer un objet de la classe Quiz.
quiz = Quiz()
# Démarrer l'interface graphique
gui.mainloop()

# FIN DU PROGRAMME
