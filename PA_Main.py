import personal_assistant_api as p_asist

# importing speech recognition package from google api 
import speech_recognition as sr 

# to control browser operations 
from selenium import webdriver 

# google text to speech 
from gtts import gTTS 

# to calculate strings into formula 
import wolframalpha 

# to play saved mp3 file 
import playsound 

# to save/open files 
import os 

# write your wolframalpha app_id here 
app_id = "EX748L-22V7E33HW6"

def process_text(input): 
	try:

		if "calculate" in input.lower(): 
			
			client = wolframalpha.Client(app_id) 

			indx = input.lower().split().index('calculate') 
			query = input.split()[indx + 1:] 
			res = client.query(' '.join(query)) 
			answer = next(res.results).text 
			p_asist.assistant_speaks("The answer is " + answer) 
			return

		elif 'search' in input or 'play' in input: 
			# a basic web crawler using selenium 
			search_web(input) 
			return

		elif "who are you" in input or "define yourself" in input: 
			speak = '''Hello, I am Person. Your personal Assistant. 
			I am here to make your life easier. You can command me to perform 
			various tasks such as calculating sums or opening applications etcetra'''
			p_asist.assistant_speaks(speak) 
			return

		elif 'open' in input: 
			
			# another function to open 
			# different application availaible 
			open_application(input.lower()) 
			return

		else: 

			p_asist.assistant_speaks("I can search the web for you, Do you want to continue?") 
			ans = p_asist.get_audio() 
			if 'yes' in str(ans) or 'yeah' in str(ans): 
				search_web(input) 
			else: 
				return 

	except : 

		p_asist.assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
		ans = p_asist.get_audio() 
		if 'yes' in str(ans) or 'yeah' in str(ans): 
			search_web(input) 

def search_web(input): 

	driver = webdriver.Firefox() 
	driver.implicitly_wait(1) 
	driver.maximize_window() 

	if 'wikipedia' in input.lower(): 

		p_asist.assistant_speaks("Opening Wikipedia") 
		indx = input.lower().split().index('wikipedia') 
		query = input.split()[indx + 1:] 
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
		return

	else: 

		if 'google' in input or 'search' in input : 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 

		else: 

			driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 

		return


# function used to open application 
# present inside the system. 
def open_application(input): 

	if "chrome" in input: 
		p_asist.assistant_speaks("Google Chrome") 
		os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
		return
	else: 

		p_asist.assistant_speaks("Application not available") 
		return

# Driver Code 
if __name__ == "__main__": 
	p_asist.assistant_speaks("What's your name, Human?") 
	name ='Human'
	name = p_asist.get_audio() 
	p_asist.assistant_speaks("Hello, " + name + '.') 
	
	while(1): 

		p_asist.assistant_speaks("What can i do for you?") 
		text = p_asist.get_audio().lower() 

		if text == 0: 
			continue

		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
			p_asist.assistant_speaks("Ok bye, "+ name+'.') 
			break

		# calling process text to process the query 
		process_text(text)