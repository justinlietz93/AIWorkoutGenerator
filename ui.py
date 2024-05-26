from tkinter import *
from workoutai import chatgpt
from functools import partial
import datetime as dt
import os

LABEL_FONT = ("Helvetica", 10, "normal")

# Sets current date in MM-DD-YYYY format
current_datetime = dt.datetime.now()
today = f"{current_datetime.month}-{current_datetime.day}-{current_datetime.year}"


# UI Class
class AppInterface:
    def __init__(self):
        # Variables / Parameters
        self.training_style = None
        self.body_focus = None
        self.rep_range = None

        # Window Setup
        self.window = Tk()
        self.window.title("AI Workout Builder")
        self.window.config(padx=20, pady=20, bg="black")
        self.window.minsize(height=800, width=800)

        # Frames #

        # Rep Range
        # Rep Range Frame
        self.rep_range_frame = Frame(self.window, bg="black")
        self.rep_range_frame.grid(row=15, column=0)

        # Rep range text canvas
        self.rep_range_canvas = Canvas(self.rep_range_frame, width=100, height=30, bg="black", highlightthickness=0)
        self.rep_range_canvas.grid(row=0, column=0)

        # Rep Range label
        self.one_three_text = self.rep_range_canvas.create_text(50, 10,
                                                                text="Rep Range",
                                                                fill="white",
                                                                font=LABEL_FONT)
        # 1 - 3 Reps Button
        self.one_three_btn = Button(self.rep_range_frame, text="1 - 3", bg="gray", width=15,
                                    command=partial(self.change_reps, reps='1 to 3'), font=LABEL_FONT)
        self.one_three_btn.grid(row=1, column=0, pady=2)

        # 3 - 5 Reps Button
        self.three_five_btn = Button(self.rep_range_frame, text="3 - 5", bg="gray", width=15,
                                     command=partial(self.change_reps, reps='3 to 5'), font=LABEL_FONT)
        self.three_five_btn.grid(row=2, column=0, pady=2)

        # 6 - 8 Reps Button
        self.six_eight_btn = Button(self.rep_range_frame, text="6 - 8", bg="gray", width=15,
                                    command=partial(self.change_reps, reps='6 to 8'), font=LABEL_FONT)
        self.six_eight_btn.grid(row=3, column=0, pady=2)

        # 8 - 12 Reps Button
        self.eight_twelve_btn = Button(self.rep_range_frame, text="8 - 12", bg="gray", width=15,
                                       command=partial(self.change_reps, reps='8 to 12'), font=LABEL_FONT)
        self.eight_twelve_btn.grid(row=4, column=0, pady=2)

        # 12 - 15 Reps Button
        self.twelve_fifteen_btn = Button(self.rep_range_frame, text="12 - 15", bg="gray", width=15,
                                         command=partial(self.change_reps, reps='12 to 15'), font=LABEL_FONT)
        self.twelve_fifteen_btn.grid(row=5, column=0, pady=2)

        # Output Text
        # Output Text Frame
        self.workout_text_frame = Frame(self.window, bg="black")
        self.workout_text_frame.grid(row=1, column=2, rowspan=30, columnspan=4, padx=20, pady=20)

        # Output Text Widget to display workout program
        self.workout_text = Text(self.workout_text_frame, height=40, width=80, bg="gray", font=LABEL_FONT)
        self.workout_text.grid(row=0, column=0)

        # Scrollbar widget for Output Text widget
        self.scrollbar = Scrollbar(self.workout_text_frame, command=self.workout_text.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.workout_text.config(yscrollcommand=self.scrollbar.set)

        # Canvas Setup #

        # Training Style text canvas
        self.options_canvas = Canvas(width=100, height=20, bg="black", highlightthickness=0)
        self.options_canvas.grid(row=0, column=0)

        # Training length text canvas
        self.length_text_canvas = Canvas(width=100, height=20, bg="black", highlightthickness=0)
        self.length_text_canvas.grid(row=4, column=0)

        # Bodypart focus text canvas
        self.body_focus_canvas = Canvas(width=100, height=20, bg="black", highlightthickness=0)
        self.body_focus_canvas.grid(row=8, column=0)

        # Text #

        # Training Style label
        self.options = self.options_canvas.create_text(50, 10,
                                                       text="Program Focus",
                                                       fill="white",
                                                       font=LABEL_FONT, )

        # Training length label
        self.length_text = self.length_text_canvas.create_text(50, 10,
                                                               text="Program Length",
                                                               fill="white",
                                                               font=LABEL_FONT, )

        # Bodypart focus label
        self.body_focus_text = self.body_focus_canvas.create_text(50, 10,
                                                                  text="Body Focus",
                                                                  fill="white",
                                                                  font=LABEL_FONT)

        # Buttons #

        # Hypertrophy button
        self.hypertrophybtn = Button(text="Hypertrophy", bg="gray", width=15,
                                     command=partial(self.change_style, style='hypertrophy'), font=LABEL_FONT)
        self.hypertrophybtn.grid(row=1, column=0)

        # Powerlifting button
        self.powerliftingbtn = Button(text="Powerlifting", bg="gray", width=15,
                                      command=partial(self.change_style, style='powerlifting'), font=LABEL_FONT)
        self.powerliftingbtn.grid(row=2, column=0, pady=2)

        # Stability button
        self.stabilitybtn = Button(text="Stability", bg="gray", width=15,
                                   command=partial(self.change_style, style='stability'), font=LABEL_FONT)
        self.stabilitybtn.grid(row=3, column=0)

        # Program Length
        self.fourweeksbtn = Button(text="4 Weeks", bg="gray", width=15, font=LABEL_FONT)
        self.fourweeksbtn.grid(row=5, column=0)

        self.eightweeksbtn = Button(text="8 Weeks", bg="gray", width=15, font=LABEL_FONT)
        self.eightweeksbtn.grid(row=6, column=0)

        self.twelveweeksbtn = Button(text="12 Weeks", bg="gray", width=15, font=LABEL_FONT)
        self.twelveweeksbtn.grid(row=7, column=0)

        # Upper Focus
        self.upperbtn = Button(text="Upper", bg="gray", width=15,
                               command=partial(self.change_focus, focus='upper'), font=LABEL_FONT)
        self.upperbtn.grid(row=9, column=0)

        # Lower Focus
        self.lowerbtn = Button(text="Lower", bg="gray", width=15,
                               command=partial(self.change_focus, focus='lower'), font=LABEL_FONT)
        self.lowerbtn.grid(row=10, column=0)

        # Push Focus
        self.pushbtn = Button(text="Push", bg="gray", width=15,
                              command=partial(self.change_focus, focus='push'), font=LABEL_FONT)
        self.pushbtn.grid(row=11, column=0)

        # Pull Focus
        self.pullbtn = Button(text="Pull", bg="gray", width=15,
                              command=partial(self.change_focus, focus='pull'), font=LABEL_FONT)
        self.pullbtn.grid(row=12, column=0)

        # Full Body Focus
        self.fullbodybtn = Button(text="Full Body", bg="gray", width=15,
                                  command=partial(self.change_focus, focus='full body'), font=LABEL_FONT)
        self.fullbodybtn.grid(row=13, column=0)

        # Arms Focus
        self.armsbtn = Button(text="Arms", bg="gray", width=15,
                                  command=partial(self.change_focus, focus='arms'), font=LABEL_FONT)
        self.armsbtn.grid(row=14, column=0)

        # Write Program Button
        self.write_program = Button(text="Write Program", bg="gray", width=15, command=self.call_workoutprogram,
                                    font=LABEL_FONT)
        self.write_program.grid(row=32, column=2)

        # Clear Button
        self.clear_program = Button(text="Clear", bg="gray", width=15, command=self.clear_button,
                                    font=LABEL_FONT)
        self.clear_program.grid(row=32, column=4)

        # Save Button
        self.save_program = Button(text="Save Program", bg="gray", width=15, command=self.save_program,
                                   font=LABEL_FONT)
        self.save_program.grid(row=32, column=3)

        self.window.mainloop()

    # Save Program function: Avoids overwriting file by adding count number to end
    def save_program(self):
        counter = 1
        filepath = f"{self.training_style}_{self.body_focus}_{today}.txt"

        while os.path.exists(filepath):
            filepath = f"{self.training_style}_{self.body_focus}_{today}_{counter}.txt"
            counter += 1

        with open(filepath, "w") as file:
            workout_program = self.workout_text.get("1.0", "end-1c")
            file.write(workout_program)

    # Changes text on output screen
    def change_workout_text(self, new_text):
        self.workout_text.delete("1.0", "end")
        self.workout_text.insert("1.0", new_text)

    # Deletes text on output screen
    def clear_button(self):
        self.workout_text.delete("1.0", "end")
        self.training_style = None
        self.rep_range = None
        self.body_focus = None

    # Calls ChatGPT OpenAI API to display text on screen
    def call_workoutprogram(self):
        result = chatgpt(self.training_style, self.body_focus, self.rep_range)
        self.change_workout_text(f"Workout Program \n{result}")

    # Changes prompt for ChatGPT Training Style
    def change_style(self, style):
        self.training_style = style
        print(self.training_style)

    # Changes prompt for ChatGPT Bodypart Focus
    def change_focus(self, focus):
        self.body_focus = focus
        print(self.body_focus)

    # Changes prompt for ChatGPT Rep Range
    def change_reps(self, reps):
        self.rep_range = reps
        print(self.rep_range)
