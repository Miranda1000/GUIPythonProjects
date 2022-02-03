# Import tkinter
import tkinter as tk

# Import time
import time

# The array that will store an array of numbers corresponding to the user's button press
# Global variable which in a later version should be removed as not good programming practice
user_input = []


# Main program function
def main():
    # Set up the Tkinter window
    window = tk.Tk()
    window.geometry("400x400")
    window.title("Timer")
    window.resizable(False, False)

    # Create the buttons and text fields
    information = tk.Label(text="Enter the time in seconds and press enter", padx=10, pady=20, font=('Arial', 12))
    b0 = tk.Button(window, text="0", command=lambda: add_number(0, user_input), activeforeground="red",
                   activebackground="pink", padx=20, pady=10,
                   font=('Arial', 12))
    b1 = tk.Button(window, text="1", command=lambda: add_number(1, user_input), activeforeground="blue",
                   activebackground="pink", padx=20, pady=10,
                   font=('Arial', 12))
    b2 = tk.Button(window, text="2", command=lambda: add_number(2, user_input), activeforeground="green",
                   activebackground="pink", padx=20, pady=10,
                   font=('Arial', 12))
    b3 = tk.Button(window, text="3", command=lambda: add_number(3, user_input), activeforeground="yellow",
                   activebackground="pink", padx=20,
                   pady=10, font=('Arial', 12))
    b4 = tk.Button(window, text="4", command=lambda: add_number(4, user_input), activeforeground="red",
                   activebackground="pink", padx=20, pady=10,
                   font=('Arial', 12))
    b5 = tk.Button(window, text="5", command=lambda: add_number(5, user_input), activeforeground="blue",
                   activebackground="pink", padx=20, pady=10,
                   font=('Arial', 12))
    b6 = tk.Button(window, text="6", command=lambda: add_number(6, user_input), activeforeground="green",
                   activebackground="pink", padx=20, pady=10,
                   font=('Arial', 12))
    b7 = tk.Button(window, text="7", command=lambda: add_number(7, user_input), activeforeground="yellow",
                   activebackground="pink", padx=20,
                   pady=10, font=('Arial', 12))
    b8 = tk.Button(window, text="8", command=lambda: add_number(8, user_input), activeforeground="red",
                   activebackground="pink", padx=20,
                   pady=10, font=('Arial', 12))
    b9 = tk.Button(window, text="9", command=lambda: add_number(9, user_input), activeforeground="blue",
                   activebackground="pink", padx=20,
                   pady=10, font=('Arial', 12))
    b_enter = tk.Button(window, text="Enter", command=lambda: timer(user_input, window), activeforeground="blue",
                        activebackground="pink", padx=10,
                        pady=10, font=('Arial', 12))

    # Place and position the buttons and text fields using grid layout
    information.grid(row=1, column=0, rowspan=2, columnspan=2)
    b1.grid(row=3, column=0, sticky='E')
    b2.grid(row=3, column=1)
    b3.grid(row=3, column=2, sticky='E')
    b4.grid(row=4, column=0, sticky='E')
    b5.grid(row=4, column=1)
    b6.grid(row=4, column=2, sticky='E')
    b7.grid(row=5, column=0, sticky='E')
    b8.grid(row=5, column=1)
    b9.grid(row=5, column=2, sticky='E')
    b0.grid(row=6, column=1)
    b_enter.grid(row=7, column=1, rowspan=2, sticky='S')

    # Call the main loop to run the Tkinter program
    # Creates a loop to ensure the Tkinter window remains open until the user presses 'X'
    window.mainloop()


# Add number method
# Parameter number_to_add passes the number to be added to the input_array
# Parameter input_array is the user_input array passed to this function
def add_number(number_to_add, input_array):
    input_array.append(number_to_add)


# Method to create the timer
# Parameter input_array to be converted to a number
# Parameter window_container to display the labels
def timer(input_array, window_container):
    number = ""
    output = tk.IntVar()

    # Loop through the input_array and store the array contents in one string variable number is later converted to
    # an integer
    for item in input_array:
        number = str(number) + str(item)

    # Repeat the number times
    for second in range(0, int(number) + 1):
        # Wait one second
        # So the timer works at counting speed and not program speed (which is faster)
        time.sleep(1)
        # Time remaining = big number - seconds passed
        # Display the time remaining on the Tkinter window
        output.set(int(number) - int(second))
        timer_text_seconds = tk.Label(window_container, textvariable=output, padx=10, pady=20,
                                      font=('Arial', 24, 'bold'))
        timer_text_seconds.grid(row=9, column=0, columnspan=2, sticky='W')
        # Update the container (otherwise the changes will not be visible as Tkinter doesn't update automatically
        # in a for loop
        window_container.update()
        # Remove the instance of timer_text_seconds
        timer_text_seconds.destroy()

    window_container.update()
    # Output time's up
    timer_text = tk.Label(text="Time's up", padx=10, pady=20, font=('Arial', 24, 'bold'))
    timer_text.grid(row=9, column=1, columnspan=2)
    window_container.update()
    # Wait 5 seconds and remove time's up
    timer_text.after(5000, timer_text.destroy())
    window_container.update()
    # Clear the user_input array before another countdown takes place
    user_input.clear()


# Call the main procedure
main()
