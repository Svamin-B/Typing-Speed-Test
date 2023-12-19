from tkinter import *
from tkinter import messagebox

user_words = []
window = Tk()
window.title("Typing Speed Test")
window.config(bg="#add8e6")
window.geometry("885x600")
window.after_id = None

sample_text = "I should have lived happy enough in that country, if my littleness had not exposed me to several " \
              "ridiculous and troublesome accidents; some of which I shall venture to relate. Glumdalclitch often " \
              "carried me into the gardens of the court in my smaller box, and would sometimes take me out of it, " \
              "and hold me in her hand, or set me down to walk. I remember, before the dwarf left the queen, " \
              "he followed us one day into those gardens, and my nurse having set me down, he and I being close " \
              "together, near some dwarf apple trees, I must needs show my wit, by a silly allusion between him and " \
              "the trees, which happens to hold in their language as it does in ours. Whereupon, the malicious rogue, " \
              "watching his opportunity, when I was walking under one of them, shook it directly over my head, " \
              "by which a dozen apples, each of them near as large as a Bristol barrel, came tumbling about my ears; " \
              "one of them hit me on the back as I chanced to stoop, and knocked me down flat on my face; but I " \
              "received no other hurt, and the dwarf was pardoned at my desire, because I had given the provocation."


words_in_sample = sample_text.split(" ")


def count_down(count):
    if count > 0:
        window.after_id = window.after(1000, count_down, count-1)
    else:
        window.after_id = None
    if count < 10:
        count = f"0{count}"
    if count == "00":
        wpm = len(user_words)
        messagebox.showinfo(title="Result", message=f"Your WPM (words per minute) is: {wpm}")
    timer_label.config(text=f"Time Left: {count}")


def start_timer():
    if window.after_id is not None:
        window.after_cancel(window.after_id)
    count_down(60)


started = False


def user_typed(event):
    global sample_text, text, started
    if entered_text.get().strip() in words_in_sample:
        words_in_sample.pop(0)
        new_sample_text = ' '.join(words_in_sample)
        text.delete("1.0", "end")
        text.insert("1.0", new_sample_text)
        entered_text.delete(0, "end")
        user_words.append(entered_text.get().strip())
        entered_text.focus()
    if not started:
        start_timer()
        started = True


title = Label(text="Press space to start...", font=8, padx=10)
title.grid(column=1, columnspan=2, row=0)
timer_label = Label(text=f"Time Left: 60")
timer_label.grid(row=1, column=0)

text = Text(window, height=30, width=50, padx=20, pady=20)

text.grid(column=0, row=2)
text.insert(END, sample_text)

entered_text = Entry(window, width=73)
entered_text.focus()
window.bind("<space>", user_typed)
scroll = Scrollbar(window)
entered_text.grid(row=2, column=1)


window.mainloop()
