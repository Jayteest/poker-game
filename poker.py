# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: December 8, 2023


# Description:
# This program creates a "Jacks or Better" Poker game simulator.
# It allows the player to create/open a bank file to store their available coins.
# It then allows the player to  place a bet by either incrementing by 1 coin at a time,
# entering a number of coins, or going all in. The game will deal a hand of 5 cards.
# The player can then select which cards to discard, then the game will deal
# that number of new cards. Finally, it will score the hand and pay out
# any won coins.


# Logic:
# import tkinter, messagebox, simpledialog, random, time
# class Poker
# init:
#   create root window
#   create int variables: funds, bet
#   get name
#   open bank
#   get deck count
#   create card images
#   money frame:
#       label: 'Coins Bet: '
#       label: bet variable
#       label: 'Coins Available: '
#       label: funds variable
#   table frame:
#       labels: img1, img2, img3, img4, img5
#       deal button: call deal method
#   menu frame:
#       bet one button: call update bet method (bet += 1)
#       bet diff button: call choose bet method
#       all in button: call update bet method (funds)
#       exit button: call exit method
# get name:
#   name = simpledialog askstring
#   loop until name entered
# open bank:
#   try: open name.bank, read
#        funds = bank.read()
#        close bank
# fund bank:
#   coinAdd = simpledialog askinteger
#   if input: funds += coinAdd
#   save bank
# save bank:
#   open name.bank, write
#   write funds
#   close bank
# get deck count:
#   top = TopLevel
#   deckCount = StringVar
#   options = range(1, 11)
#   label: deckCount prompt
#   OptionMenu: top, deckCount, *options
#   accept button: call close top method
# close top:
#   deckCount = deckCount.get()
#   create decks
#   top.destroy()
# create decks:
#   deckNum = 0
#   for i in deckCount: append [1] * 52
# create card images:
#   backImg = PhotoImage(back01.gif)
#   initialize suits list and values list
#   for suit in list:
#       for value in list:
#           imgList.append PhotoImage(value + of + suit + .gif)
# update bet:
#   if value not between 0 - 51: display error messagebox
#   elif value > funds: call fund bank
#   else: bet = value
# choose bet:
#   value = simpledialog askinteger
#   updateBet(value)
# deal:
#   if first deal:
#       funds -= bet
#       create keep/discard button for each card
#   for i, card in enumerate(hand):
#       if discard:
#           card = randrange(52)
#           if current deck[card] > 0:
#               currend deck[card] --
#               img = imgList[card]
#   if second deal: score hand
# score hand:
#   create empty lists for hand suits and hand values
#   for card in hand:
#       suit[card // 13] ++
#       value[card % 13] ++
#   if 5 in hand suits and hand values = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]:
#       Royal Flush, payout = bet * 400
#   elif 5 in hand suits and hand values [i] * [i + 1] ... * [i + 4] == 1:
#       Straight Flush, payout = bet * 50
#   elif 4 in hand values:
#       Four of a Kind, payout = bet * 25
#   elif 3 in hand values and 2 in hand values:
#       Full House, payout = bet * 8
#   elif 5 in hand suits:
#       Flush, payout = bet * 5
#   elif hand values [i] * [i + 1] ... * [i + 4] == 1:
#       Striaght, payout = bet * 4
#   elif 3 in hand values:
#       Three of a Kind, payout = bet * 3
#   elif hand values count(2) == 2:
#       Two Pairs, payout = bet * 2
#   elif 2 in hand values and index in [0, 10, 11, 12]:
#       Pair, payout = bet
#   else: None, payout = 0
#   funds += payout
#   save bank
#   clean up
# clean up:
#   try: current deck ++
#   except: "Shuffle"...create decks
#   reset variables
#   hand images set to back01.gif
# exit:
#   save bank
#   root.destroy()


# import tkinter for create GUI
import tkinter as tk
# import messagebox and simpledialog for creating pop-ups
from tkinter import messagebox, simpledialog
# import random for drawing cards and time for creating delay between dealing each card
import random, time

# declare Poker class
class Poker:
    # declare constructor method for Poker class
    def __init__(self):
        # create GUI root window
        self.root = tk.Tk()
        # give root window an appropriate title
        self.root.title(f'Jacks or Better Poker')

        # declare integer variable to store value of available funds
        self.funds = tk.IntVar(value=0)
        # declare integer variableto store value of current bet
        self.bet = tk.IntVar(value=0)

        # call method to get player's name
        self.get_name()
        # call method to open bank file for player
        self.open_bank()
        # call method to get number of decks player would like to play with
        self.get_deck_count()
        # call method to create a list of card images
        self.create_card_img()

        # initialize attribute to track how many times the deal button has been pressed
        self.num_deals = 0

        # frame for displaying money info
        self.money_frame = tk.Frame(self.root)
        # label to display 'Coins Bet: '
        self.bet_label = tk.Label(self.money_frame, text=f'Coins Bet: ')
        # label to display current bet value
        self.bet_out = tk.Label(self.money_frame, textvariable=self.bet)
        # label to display 'Coins Available: '
        self.funds_label = tk.Label(self.money_frame, text=f'Coins Available: ')
        # label to display current available funds
        self.funds_out = tk.Label(self.money_frame, textvariable=self.funds)

        # position each widget within money info frame using grid placement
        self.bet_label.grid(row=0, column=0)
        self.bet_out.grid(row=0, column=1)
        self.funds_label.grid(row=0, column=2)
        self.funds_out.grid(row=0, column=3)
        # position money info frame within root window using grid placement
        self.money_frame.grid(row=1, column=0)

        # frame for displaying table, to contain cards, deal button, and discard options
        self.table_frame = tk.Frame(self.root, bg='green')

        # labels for each of 5 cards displayed on table, each initialized to back image
        self.img_1 = tk.Label(self.table_frame, image=self.back_img, bg='green')
        self.img_2 = tk.Label(self.table_frame, image=self.back_img, bg='green')
        self.img_3 = tk.Label(self.table_frame, image=self.back_img, bg='green')
        self.img_4 = tk.Label(self.table_frame, image=self.back_img, bg='green')
        self.img_5 = tk.Label(self.table_frame, image=self.back_img, bg='green')
        # button to deal cards, initially disabled until bet is placed
        self.deal_btn = tk.Button(self.table_frame, text=f'Deal', 
                                  command=self.deal, state='disabled')

        # position cards and deal button within table frame using grid placement
        self.img_1.grid(row=0, column=0, padx=25)
        self.img_2.grid(row=0, column=1, padx=25)
        self.img_3.grid(row=0, column=2, padx=25)
        self.img_4.grid(row=0, column=3, padx=25)
        self.img_5.grid(row=0, column=4, padx=25)
        self.deal_btn.grid(row=2, column=0, columnspan=5, pady=25)

        # position table frame within root window using grid placement
        self.table_frame.grid(row=0, column=0, pady=25)

        # frame for displaying menu options: bet buttons and exit button
        self.menu_frame = tk.Frame(self.root)

        # button to call method to increment bet by 1 coin
        self.bet_one_btn = tk.Button(self.menu_frame, text=f'Bet One Coin',
                                     command=lambda: self.update_bet(self.bet.get() + 1))
        # button to call method to prompt player for a different bet amount
        self.bet_diff_btn = tk.Button(self.menu_frame, text=f'Bet a Different Amount',
                                      command=self.choose_bet)
        # button to call method to update bet to value of available funds
        self.all_in_btn = tk.Button(self.menu_frame, text=f'All In',
                                    command=lambda: self.update_bet(self.funds.get()))
        # button to call method to end game and exit program
        self.exit_btn = tk.Button(self.menu_frame, text=f'Exit', command=self.exit)

        # position option buttons within menu frame using grid placement
        self.bet_one_btn.grid(row=1, column=0)
        self.bet_diff_btn.grid(row=1, column=1)
        self.all_in_btn.grid(row=1, column=2)
        self.exit_btn.grid(row=1, column=3)
        # position menu frame within root window using grid placement
        self.menu_frame.grid(row=2, column=0)

               
    # method to prompt player for their name
    def get_name(self):
        # display pop-up prompting for string input of player's name, assign to attribute
        self.name = simpledialog.askstring(f'Player Name', f'Enter your name: ')
        # loop to validate name input, check if input is empty or a space
        while self.name is None or self.name == '' or self.name.isspace():
            # if so, display pop-up with error message
            messagebox.showinfo(f'Oops!', f'No name entered.')
            # display pop-up prompting for name to try again
            self.name = simpledialog.askstring(f'Player Name', f'Enter your name: ')


    # method to open player's bank file
    def open_bank(self):
        # try suite for input validation
        try:
            # open bank file in player's name in read mode
            with open(f'{self.name}.bank', 'r') as self.bank:
                # update available funds attribute to value stored in bank file
                self.funds.set(self.bank.read())
                # close bank file
                self.bank.close()
                # display pop-up with player's available funds
                messagebox.showinfo(f'Hello!', f'Welcome back, {self.name}!\n'
                                    f'Your bank balance is {self.funds.get()} coins.')
        # if error opening bank file, then new player
        except:
            # display pop-up informing player they must fund their bank
            messagebox.showinfo(f'Hello!', f'Welcome, {self.name}!\n'
                                    f'Please fund your bank to play.')

            # while loop to iterate as long as no funds in bank
            while self.funds.get() <= 0:
                # call method to fund bank
                self.fund_bank()
                # check if still no funds
                if self.funds.get() <= 0:
                    # if so, display pop-up with error message
                    messagebox.showinfo(f'Oops!', f'Funds must be added to play.')


    # method to fund bank
    def fund_bank(self):
        # display pop-up prompting for number of coins to add, assign to attribute
        coin_add = simpledialog.askinteger(f'Fund Bank', f'Add Coins: ')
        # check if a value was entered
        if coin_add:
            # if so, add value to current funds
            self.funds.set(self.funds.get() + coin_add)
            # call method to save bank file
            self.save_bank()


    # method to save bank file
    def save_bank(self):
        # open bank file in player's name in write mode
        # will create bank file if new player, or overwrite old value if existing player
        with open(f'{self.name}.bank', 'w') as self.bank:
            # write current available funds value to bank file
            self.bank.write(str(self.funds.get()))
            # close bank file
            self.bank.close()


    # method to get number of decks player would like to play with
    def get_deck_count(self):
        # create GUI toplevel window
        self.top = tk.Toplevel()
        # give toplevel window an appropriate title
        self.top.title(f'Decks to Use')
        # declare string variable for deck count, initialize with 1 to use as default
        self.deck_count = tk.StringVar(value=1)
        # initialize options list with 1 - 10
        self.options = list(range(1, 11))

        # label to display deck count prompt
        self.deck_label = tk.Label(self.top, text=f'Select the number of decks '
                                   'to play with: ')
        # option menu to select number of decks
        self.dropdown = tk.OptionMenu(self.top, self.deck_count, *self.options)
        # button to accept option menu selection, calls method to close toplevel window
        self.accept_btn = tk.Button(self.top, text=f'Accept', command=self.close_top)

        # position label, dropdown, and accept button within toplevel window using grid placement
        self.deck_label.grid(row=0, column=0, columnspan=2)
        self.dropdown.grid(row=1, column=0)
        self.accept_btn.grid(row=1, column=1)


    # method to close toplevel window
    def close_top(self):
        # update deck count attribute to integer from option menu
        self.deck_count = int(self.deck_count.get())
        # call method to create specified number of decks
        self.create_decks()
        # close toplevel window
        self.top.destroy()


    # method to create decks
    def create_decks(self):
        # declare list to store decks
        self.decks = []
        # declare attribute to serve as pointer to deck through loop iterations
        self.deck_num = 0
        # for loop to iterate once for each deck needed
        for deck in range(self.deck_count):
            # append 52 element list of 1s to decks list
            self.decks.append([1] * 52)
        # declare attribute to hold deck currently being dealt
        self.current_deck = self.decks[0]
        # declare attribute to hold index of deck currently being dealt
        self.curr_deck_i = 0


    # method to create list of card images
    def create_card_img(self):
        # initialize photo image attribute to image of back of card
        self.back_img = tk.PhotoImage(file=f'back01.gif')
        # initialize list of suit names
        self.suits_list = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        # initialize list of face value names
        self.values_list = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                            'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

        # declare list for storing card images
        self.img_list = []
        # for loop to iterate over suit names
        for suit in self.suits_list:
            # nested for loop to iterate over value names
            for value in self.values_list:
                # append image of suit + value combo to list of card images
                self.img_list.append(tk.PhotoImage(file=f'{value}_of_{suit}.gif'))


    # method to update bet amount
    def update_bet(self, val):
        # check if bet is outside acceptable range of 1-50
        if not 0 < val < 51:
            # if so, display pop-up with error message
            messagebox.showinfo(f'Oops!', f'Bet must be between 1-50 coins.')
        # check if bet is more than available funds
        elif val > self.funds.get():
            # if so, display pop-up with error message
            messagebox.showinfo(f'Oops!', f'Funds must be added for this bet.')
            # call method to add funds to bank
            self.fund_bank()
        # if neither issue above exists...
        else:
            # set bet attribute to requested bet value
            self.bet.set(val)
            # update deal button to normal state
            self.deal_btn['state'] = 'normal'


    # method to select a different bet amount
    def choose_bet(self):
        # display pop-up prompting user for number of coins to bet
        val = simpledialog.askinteger(f'Place Bet', f'Coins to Bet: ')
        # call method to update bet to input value
        self.update_bet(val)


    # method to deal cards
    def deal(self):
        # increment number of deals attribute
        self.num_deals += 1
        # initialize list containing the labels for the card images on the table
        self.hand_img = [self.img_1, self.img_2, self.img_3, self.img_4, self.img_5]
        # check if this is the first deal
        if self.num_deals == 1:
            # if so, initialize hand attribute with list of 5 blank elements
            self.hand = [''] * 5
            # initialize discard attribute with list of 5 'True' bool values
            self.discard = [True] * 5
            # subtract bet from available funds
            self.funds.set(self.funds.get() - self.bet.get())
            # call method to save bank file
            # if not saved here, user can close window after deal to avoid losing coins
            self.save_bank()
            # disable bet one button, bet different amount button, and all in button
            self.bet_one_btn['state'] = 'disabled'
            self.bet_diff_btn['state'] = 'disabled'
            self.all_in_btn['state'] = 'disabled'
            # call method to create keep/discard option buttons
            self.create_opt_buttons()
            
        # enumerate hand list to loop over indices and values
        for i, card in enumerate(self.hand):
            # check if corresponsing discard value is true
            if self.discard[i]:
                # loop to iterate until card is dealt successfully
                while True:
                    # get random value between 0-51
                    card = random.randrange(52)
                    # check if corresponding card value is still in deck
                    if self.current_deck[card] > 0:
                        # if so, remove it from the deck
                        self.current_deck[card] -= 1
                        # update image on table to correspoding card in card image list 
                        self.hand_img[i].config(image=self.img_list[card], bg='green')
                        # update corresponding discard value to false
                        self.discard[i] = False
                        # update corresponding hand value to dealt card value
                        self.hand[i] = card
                        # update root window
                        self.root.update()
                        # pause execution for 0.3 seconds to create left-to-right effect
                        time.sleep(0.3)
                        # break from loop to move to next card in hand
                        break
                    # if card is not still in deck...
                    else:
                        # continue to next iteration to try again
                        continue

        # check if this is the second deal
        if self.num_deals == 2:
            # if so, remove keep/discard option buttons
            self.opt_btn_1.destroy()
            self.opt_btn_2.destroy()
            self.opt_btn_3.destroy()
            self.opt_btn_4.destroy()
            self.opt_btn_5.destroy()

            # call method to score hand
            self.score_hand()


    # method to create keep/discard option buttons
    def create_opt_buttons(self):
        # button for keep/remove option on card 1, calls method to toggle
        self.opt_btn_1 = tk.Button(self.table_frame, text='Keep', 
                                   command=lambda: self.toggle(self.opt_btn_1, 0))
        # position option button 1 within table frame using grid placement
        self.opt_btn_1.grid(row=1, column=0)
        
        # button for keep/remove option on card 2, calls method to toggle
        self.opt_btn_2 = tk.Button(self.table_frame, text='Keep',  
                                   command=lambda: self.toggle(self.opt_btn_2, 1))
        # position option button 2 within table frame using grid placement
        self.opt_btn_2.grid(row=1, column=1)
        
        # button for keep/remove option on card 3, calls method to toggle
        self.opt_btn_3 = tk.Button(self.table_frame, text='Keep',  
                                   command=lambda: self.toggle(self.opt_btn_3, 2))
        # position option button 3 within table frame using grid placement
        self.opt_btn_3.grid(row=1, column=2)
        
        # button for keep/remove option on card 4, calls method to toggle
        self.opt_btn_4 = tk.Button(self.table_frame, text='Keep', 
                                   command=lambda: self.toggle(self.opt_btn_4, 3))
        # position option button 4 within table frame using grid placement
        self.opt_btn_4.grid(row=1, column=3)
        
        # button for keep/remove option on card 5, calls method to toggle
        self.opt_btn_5 = tk.Button(self.table_frame, text='Keep', bg='green', 
                                   command=lambda: self.toggle(self.opt_btn_5, 4))
        # position option button 5 within table frame using grid placement
        self.opt_btn_5.grid(row=1, column=4)


    # method to toggle keep/remove option button                                           
    def toggle(self, btn, i):
        # check if current discard value is true
        if self.discard[i]:
            # if so, update text on button to 'Keep'
            btn.config(text='Keep')
            # update discard value to false
            self.discard[i] = False
            # update card image background color to green
            self.hand_img[i].config(bg='green')
        # if current dicard value is false...
        else:
            # update text on button to 'Discard'
            btn.config(text='Discard')
            # update discard value to true
            self.discard[i] = True
            # update card image background color to red, to indicate cards selected for discard
            self.hand_img[i].config(bg='red')
                    

    # method to score hand
    def score_hand(self):
        # initialize list with 4 elements containing 0s, to be used for hand suits
        self.hand_suits = [0] * 4
        # initialize list with 13 elements containing 0s, to be used for hand face values
        self.hand_values = [0] * 13
        
        # for loop to iterate through cards in hand
        for card in self.hand:
            # get card's suit by dividing by 13, increment corresponding index of suit list
            self.hand_suits[card // 13] += 1
            # get card's face value by calculating remainder when divided by 13,
            # increment corresponding index of face value list
            self.hand_values[card % 13] += 1
            
        # for loop to find lowest face value in hand 
        for val in self.hand_values:
            # check if face value is in hand
            if val != 0:
                # if so, initialize first value variable to face value
                val_1 = self.hand_values.index(val)
                # break from loop
                break
            # if face value is not in hand...
            else:
                # continue to next iteration to check next face value
                continue

        # check if 5 suits match and face values are Ten, Jack, Queen, King, Ace
        if 5 in self.hand_suits and self.hand_values == [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]:
            # if so, set combo attribute to 'Royal Flush'
            self.combo = 'Royal Flush'
            # set payout to bet * 400
            self.payout = self.bet.get() * 400

        # check if 5 suits match and if lowest face value count * count of next 4 face values equal 1                              
        elif 5 in self.hand_suits and self.hand_values[val_1 + 1] * self.hand_values[val_1 + 2]\
             * self.hand_values[val_1 + 3] * self.hand_values[val_1 + 4] == 1:
            # if so, set combo attribute to 'Straight Flush'
            self.combo = 'Straight Flush'
            # set payout to bet * 50
            self.payout = self.bet.get() * 50

        # check if 4 matching face values
        elif 4 in self.hand_values:
            # if so, set combo attribute to 'Four of a Kind'
            self.combo = 'Four of a Kind'
            # set payout to bet * 25
            self.payout = self.bet.get() * 25

        # check if 3 matching face values, and 2 other matching face values
        elif 3 in self.hand_values and 2 in self.hand_values:
            # if so, set combo attribute to 'Full House'
            self.combo = 'Full House'
            # set payout to bet * 8
            self.payout = self.bet.get() * 8

        # check if 5 suits match
        elif 5 in self.hand_suits:
            # if so, set combo attribute to 'Flush'
            self.combo = 'Flush'
            # set payout to bet * 5
            self.payout = self.bet.get() * 5

        # check if lowest face value count * count of next 4 face values equal 1
        elif self.hand_values[val_1 + 1] * self.hand_values[val_1 + 2] * self.hand_values[val_1 + 3] \
             * self.hand_values[val_1 + 4] == 1:
            # if so, set combo attribute to 'Straight'
            self.combo = 'Straight'
            # set payout to bet * 4
            self.payout = self.bet.get() * 4

        # check if 3 matching face values
        elif 3 in self.hand_values:
            # if so, set combo attribute to 'Three of a Kind'
            self.combo = 'Three of a Kind'
            # set payout to bet * 3
            self.payout = self.bet.get() * 3

        # check if 2 different face values have a count of 2
        elif self.hand_values.count(2) == 2:
            # if so, set combo attribute to 'Two Pairs'
            self.combo = 'Two Pairs'
            # set payout to bet * 2
            self.payout = self.bet.get() * 2

        # check if 2 matching face values and if matching values are Ace, Jack, Queen, or King
        elif 2 in self.hand_values and self.hand_values.index(2) in [0, 10, 11, 12]:
            # if so, set combo attribute to 'Pair'
            self.combo = 'Pair'
            # set payout equal to bet
            self.payout = self.bet.get()

        # if no combo above exists...
        else:
            # set combo attribute to 'None'
            self.combo = 'None'
            # set payout to 0
            self.payout = 0

        # add payout to available funds value
        self.funds.set(self.funds.get() + self.payout)
        # call method to save bank
        self.save_bank()
        # display pop-up with combo and payout
        messagebox.showinfo(f'Results', f'Hand: {self.combo}\nPayout: {self.payout}')
        # call method to clean up and prep for next hand
        self.clean_up()


    # method to clean up and prep for next hand
    def clean_up(self):
        # check if current deck has fewer than 31 cards - this indicates less than 60% of deck remains
        if sum(self.current_deck) <= 31:
            # is so, begin try suite for exception handling
            try:
                # increment current deck index
                self.curr_deck_i += 1
                # set current deck to next deck in decks created list
                self.current_deck = self.decks[self.curr_deck_i]
                # display pop-up with message that game is moving to the next deck
                messagebox.showinfo(f'Next Deck', f'Moving to Deck {self.curr_deck_i + 1}')
            # if no next deck, exception will be thrown
            except IndexError:
                # display pop-up with message that decks are being shuffled.
                messagebox.showinfo(f'Shuffle', f'Shuffling Decks')
                # call method to create fresh decks
                self.create_decks()
        # reset bet to 0
        self.bet.set(0)
        # reset number of deals to 0
        self.num_deals = 0
        # reset buttons to initial states
        self.bet_one_btn['state'] = 'normal'
        self.bet_diff_btn['state'] = 'normal'
        self.all_in_btn['state'] = 'normal'
        self.deal_btn['state'] = 'disabled'
        # enumerate hand list to loop over indices and values
        for i, img in enumerate(self.hand_img):
            # update image of card on table to back of card image
            self.hand_img[i].config(image=self.back_img)
            # update root window
            self.root.update()
            # pause execution for 0.1 seconds to create left-to-right effect
            time.sleep(0.1)
        

    # method to end game and exit program
    def exit(self):
        # call method to save bank
        self.save_bank()
        # display pop-up with appropriate message
        messagebox.showinfo(f'Goodbye', f'Thank you for playing!')
        # close root window
        self.root.destroy()


# main function to execute program
if __name__ == '__main__':
    # instantiate Poker class object
    game = Poker()
