from tkinter import messagebox
import tkinter as tk


def check_winner():
    global winner
    combos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # Rows
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # Columns
        [0, 4, 8],
        [2, 4, 6],  # Diagonals
    ]

    for combo in combos:
        if (
            buttons[combo[0]]["text"]
            == buttons[combo[1]]["text"]
            == buttons[combo[2]]["text"]
            != ""
        ):
            winner = True
            for index in combo:
                buttons[index].configure(bg="lightgreen")
            messagebox.showinfo(
                "Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!"
            )
            return

    # Check for Draw
    if all(b["text"] != "" for b in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player  # Fixed: assignment '='
        check_winner()
        if not winner:
            toggle_player()


def toggle_player():
    global current_player
    # Fixed: consistent uppercase 'X' and 'O'
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")


root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
winner = False

buttons = [
    tk.Button(
        root,
        text="",
        font=("normal", 25),
        width=6,
        height=2,
        command=lambda i=i: button_click(i),
    )
    for i in range(9)
]

# Grid all 9 buttons
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# UI elements placed outside the loop
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()