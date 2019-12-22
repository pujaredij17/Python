from tkinter import * 
from tkinter import messagebox 
import requests, json 

def weather():
    api_key = "886705b4c1182eb1c69f28eb8c520e20"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_field.get() 
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key 
    print(complete_url)
    response = requests.get(complete_url) 
    x = response.json() 
    print(x)
    
    if x["cod"] != "404" : 
  
        # store the value of "main" key in variable y 
        y = x["main"] 
  
        # store the value corresponding to the "temp" key of y 
        current_temperature = y["temp"] 
  
        # store the value corresponding to the "pressure" key of y 
        current_pressure = y["pressure"] 
  
        # store the value corresponding to the "humidity" key of y 
        current_humidiy = y["humidity"] 
  
        # store the value of "weather" key in variable z 
        z = x["weather"] 
  
        # store the value corresponding to the "description" key 
        # at the 0th index of z  
        weather_description = z[0]["description"] 
  
        # insert method inserting the  
        # value in the text entry box.  
        temp_field.insert(15, str(current_temperature) + " Kelvin") 
        atm_field.insert(10, str(current_pressure) + " hPa") 
        humid_field.insert(15, str(current_humidiy) + " %") 
        desc_field.insert(10, str(weather_description) ) 
    else : 
  
        # message dialog box appear which 
        # shows given Error meassgae 
        messagebox.showerror("Error", "City Not Found \n"
                             "Please enter valid city name") 
  
        # clear the content of city_field entry box 
        city_field.delete(0, END) 
        
def clear():
    city_field.delete(0, END)   
    temp_field.delete(0, END) 
    atm_field.delete(0, END) 
    humid_field.delete(0, END) 
    desc_field.delete(0, END) 

    # set focus on the city_field entry box  
    city_field.focus_set()  
  
    # Driver code 
if __name__ == "__main__" : 
  
    # Create a GUI window 
    root = Tk() 
  
    # set the name of tkinter GUI window 
    root.title("Gui Application") 
  
    # Set the configuration of GUI window  
    root.geometry("425x175") 
  
    # Create a Weather Gui Application label  
    headlabel = Label(root, text = "Weather Gui Application") 
      
    # Create a City name : label 
    label1 = Label(root, text = "City name : ") 
      
    # Create a City name : label 
    label2 = Label(root, text = "Temperature :") 
  
    # Create a atm pressure : label 
    label3 = Label(root, text = "atm pressure :") 
  
    # Create a humidity : label 
    label4 = Label(root, text = "humidity :") 
  
    # Create a description :label 
    label5 = Label(root, text = "description  :") 
      
  
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure .   
    headlabel.grid(row = 0, column = 1)  
    label1.grid(row = 1, column = 0, sticky ="E")  
    label2.grid(row = 3, column = 0, sticky ="E")  
    label3.grid(row = 4, column = 0, sticky ="E")  
    label4.grid(row = 5, column = 0, sticky ="E")  
    label5.grid(row = 6, column = 0, sticky ="E") 
  
  
    # Create a text entry box  
    # for filling or typing the information.  
    city_field = Entry(root)  
    temp_field = Entry(root)  
    atm_field = Entry(root)  
    humid_field = Entry(root)  
    desc_field = Entry(root) 
  
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure .  
    # ipadx keyword argument set width of entry space .  
    city_field.grid(row = 1, column = 1, ipadx ="100")  
    temp_field.grid(row = 3, column = 1, ipadx ="100")  
    atm_field.grid(row = 4, column = 1, ipadx ="100")  
    humid_field.grid(row = 5, column = 1, ipadx ="100")  
    desc_field.grid(row = 6, column = 1, ipadx ="100") 
  
    # Create a Submit Button and attached  
    # to tell_weather function  
    button1 = Button(root, text = "Submit",command = weather) 
  
    # Create a Clear Button and attached  
    # to clear_all function  
    button2 = Button(root, text = "Clear", command = clear) 
  
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure .  
    button1.grid(row = 2, column = 1) 
    button2.grid(row = 7, column = 1) 
      
    # Start the GUI  
    root.mainloop() 


