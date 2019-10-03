from tkinter import *
from selenium import webdriver
import csv
import sys

# take user inputs so that credentials can be used
user_input = []
user_location = ()


def click():
    username = str(e1.get())
    password = str(e2.get())
    pin = str(e3.get())
    gui_win.destroy()
    global user_input
    user_input = [username, password, pin]


# use tkinter to create gui for input
gui_win = Tk()
Label(gui_win, text="username").grid(row=0)
Label(gui_win, text="password").grid(row=1)
Label(gui_win, text="pin").grid(row=2)
e1 = Entry(gui_win)
e2 = Entry(gui_win)
e3 = Entry(gui_win)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(gui_win, text="SUBMIT", width=6, command=click).grid(row=3, column=0)
gui_win.mainloop()

# data scrape for current inventory csv
def find_ele(element, locator):
    if locator == "id":
        return driver.find_element_by_id(element)
    elif locator == "name":
        return driver.find_element_by_name(element)
    elif locator == "xpath":
        return driver.find_element_by_xpath(element)


driver = webdriver.Firefox()


driver.get("https://cloud.lightspeedapp.com/login.html")
log_input = find_ele("login-input", "id")
pass_input = find_ele("password-input", "id")
log_input.send_keys(user_input[0])
pass_input.send_keys(user_input[1])

"""




# create variables for CSV readers
inventory = open("item_listings_local_matches.csv")
correct_inventory = open("min_stock_worksheet.csv")
temp_sink = open("intermediary", "w", newline="")
# create a nested list for each CSV
inventory_reader = list(csv.reader(inventory))
correct_reader = list(csv.reader(correct_inventory))
sink_writer = csv.writer(temp_sink)
entry_hold = []

# for loop reads and sets variables for item and qty in worksheet
for entry in correct_reader:
    item = entry[0]
    needed = entry[1]

# for loop repeats for the inventory export
    for inv in inventory_reader:
        inst = inv[5]
        have = inv[6]

        # compares lists and prints items that are shorted
        if inst == item and int(have) < int(needed):
            entry_hold.clear()
            entry_hold.append(item)
            entry_hold.append(int(needed)-int(have))
            sink_writer.writerow(entry_hold)


temp_sink.close()
sys.exit()
"""
