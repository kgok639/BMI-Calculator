import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=200)


def Calculate():
    weight = int(weightEntry.get())
    height = int(heightEntry.get()) / 100
    bmi = weight / (height * height)
    bmiLabel = tkinter.Label(text=f"Your BMI is {bmi}")
    bmiLabel.pack()
    print(f"Your bmi is {bmi}")
    if bmi <= 18.4:
        print("You are underweight")
        underweightLabel.pack()
    elif bmi <= 24.9:
        print("You are normal")
        normalLabel.pack()
    elif bmi <= 39.9:
        print("You are overweight")
        overweightLabel.pack()
    else:
        print("You are obese")
        obeseLabel.pack()

weightEntry = tkinter.Entry()
heightEntry = tkinter.Entry()

weightLabel = tkinter.Label(text= "Enter your weight (kg)")
heightLabel = tkinter.Label(text= "Enter your height (cm)")

underweightLabel = tkinter.Label(text="You are underweight")
normalLabel = tkinter.Label(text="You are normal")
overweightLabel = tkinter.Label(text="You are overweight")
obeseLabel = tkinter.Label(text="You are obese")

calculateButton = tkinter.Button(text= "Calculate", command=Calculate)


weightLabel.pack()
weightEntry.pack()
heightLabel.pack()
heightEntry.pack()
calculateButton.pack()

window.mainloop()

