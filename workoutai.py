import openai


openai.api_key = "API KEY GOES HERE"  # Replace with your API key


def chatgpt(style, focus, reps):
    # while True:
    # question = input("Ask me a question: \n(Type 'exit' to end)\n")
    # if question.lower() == "exit":
    #     break
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      # model="gpt-4",
      messages=[
        {
          "role": "user",
          "content": "Please write a single workout."
                     f"The body part focus of the workout should be {focus}."
                     f"The training style of the workout should be 100% {style} focused."
                     f"The rep range for this {style} {focus} program will be: ({reps}) or whatever is suited for the"
                     f"training style and body part focus."
                     "For the rep ranges, keep the heavy compound movements slightly lower "
                     "reps than the other movements."
                     "For the amount of exercises, keep it around 5 with a maximum of 7-8"
                     "For the total amount of sets, aim for 15 to 25 sets total, but >= 10 sets for a specific muscle"
                     " group."
                     "For the rest times, keep the rest between 1 to 4 minutes or until heart rate has recovered."
                     "Only write a structured program and nothing else."
                     "Make sure to keep compound movements near the beginning of the workout."
                     "Try to keep isolation movements near the end of the workout."
                     "The program should be structured like this"
                     f"Focus: {style}{focus}"
                     "Exercise: "
                     "Sets: "
                     "Reps: "
                     "Rest: "
                     "If the training style is stability, then choose exercises that put the trainee in unstable"
                     "positions that force them to engage their core more than normal."
                     "If the focus is hypertrophy keep an even mix of machines and free weight exercises."
                     "If the focus is powerlifting keep the exercises based around "
                     "squat, bench, deadlift, and accessories"
                     "Do not write out any advice, semantics, rhetoric or considerations."
                     "Do not add any extra notes or comments."
        }
      ],
      temperature=0.5,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['message']['content']

