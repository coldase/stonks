import requests
from tkinter import *
import json

def get_data(name, loc):
	name, loc = str(name), str(loc)
	url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"
	querystring = {"symbol":name, "region": loc}

	headers =  {
		'Accept': 'application/json',
	    'x-rapidapi-key': '<YOUR API KEY HERE>',
		'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

	res = requests.get(url, headers=headers, params=querystring)

	return res

class Stockapp:
	def __init__(self):
		self.win_x = 500
		self.win_y = 300
		self.winsize = f'{self.win_x}x{self.win_y}'
		self.root = Tk()
		self.root.title("STONKS")
		self.root.resizable(False,False)
		self.root.geometry(self.winsize)
		self.add_content()

	def run(self):
		self.root.mainloop()

	def add_content(self):
		label_fontsize = 20
		label_width = 200
		label_height = 50
		
		label2_fontsize = 35
		label2_width = 300
		label2_height = 40

		entry_width = 150
		entry_height = 30

		button_width = 80
		button_height = 30

		self.result_label = Label(self.root, text="--", font=("calibri",label_fontsize))
		self.result2_label = Label(self.root, text="--", font=("calibri",label2_fontsize))
		self.name_entry = Entry(self.root)
		search_button = Button(self.root, text="Search", command=self.test)

		self.result_label.place(x=self.win_x / 2 - label_width / 2, y=30, width=label_width, height=label_height)
		self.result2_label.place(x=self.win_x / 2 - label2_width / 2, y=100, width=label2_width, height=label2_height)
		self.name_entry.place(x=self.win_x / 2 - entry_width / 2, y =200, width=entry_width, height=entry_height)
		search_button.place(x=self.win_x / 2 - button_width / 2,y=240,width=button_width, height=button_height)


	def test(self):
		get_term = self.name_entry.get()

		data = get_data(get_term, "US")
		newdata = json.loads(data.text)
		#name = newdata['summaryProfile']['name']
		current_price = newdata['price']['regularMarketPrice']['raw']

		self.result_label.config(text=get_term.upper())
		self.result2_label.config(text=f'${current_price}')

app = Stockapp()

if __name__ == "__main__":
	app.run()