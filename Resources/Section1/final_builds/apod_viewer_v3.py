#APOD Viewer
#Icon CC Attribution 3.0 Unported
import tkinter, requests, webbrowser
from tkcalendar import DateEntry #To use with auto-py-to-exe add hidden imports of bablel.numbers
from PIL import ImageTk, Image
from io import BytesIO
from tkinter import Toplevel, filedialog

#Define window
root = tkinter.Tk()
root.title('APOD Photo Viewer')
root.iconbitmap('rocket.ico')

#Define fonts and colors
nasa_blue = "#043c93"
nasa_light_blue = "#7AA5D3"
nasa_red = "#ff1923"
nasa_white = "#ffffff"
text_font = ('Times New Roman', 14)
root.config(bg=nasa_blue)

#Define functions
def get_request():
    '''Get request data from nasa Astronomy Picture of the Day API'''
    global response

    #Example request
    '''{'copyright': 'Declan Deval', 'date': '2020-07-14', 'explanation': 'Have you ever seen a comet? Tonight -- and likely the next few nights -- should be a good chance. 
    Go outside just at sunset and look to your northwest.  The lower your horizon, the better.  Binoculars may help, but if your sky is cloudless and dark, 
    all you should need is your unaided eyes and patience. As the Sun sets, the sky will darken, and there will be an unusual faint streak pointing diagonally near the 
    horizon. That is Comet NEOWISE. It is a 5-kilometer-wide evaporating dirty iceberg visiting from -- and returning to -- the outer Solar System. As the Earth turns, 
    the comet will soon set, so you might want to take a picture. In the featured image, Comet C/2020 F3 (NEOWISE) was captured two mornings ago rising over Stonehenge 
    in the UK.  Discovered with the NASA satellite NEOWISE toward the end of March, Comet NEOWISE has surprised many by surviving its closest approach to the Sun, 
    brightening dramatically, and developing impressive (blue) ion and (white) dust tails.    
    Notable Images of Comet NEOWISE Submitted to APOD:  || July 13  || July 12  || July 11  || July 10 & earlier ||', 
    'hdurl': 'https://apod.nasa.gov/apod/image/2007/NeowiseStonehenge_Deval_5572.jpg', 'media_type': 'image', 'service_version': 'v1', 
    'title': 'Comet NEOWISE over Stonehenge', 'url': 'https://apod.nasa.gov/apod/image/2007/NeowiseStonehenge_Deval_960.jpg'}'''

    #Set the parameters for the request
    url = 'https://api.nasa.gov/planetary/apod'
    #api_key = 'N0NN5ebP8B13oGp7GFSvj61aeuAlX2urJEKExjhc'
    api_key = 'DEMO_KEY'
    date = calander.get_date()
    #date = date_entry.get()

    #USE YOUR OWN API KEY!
    querystring = {'api_key':api_key, 'date':date}

    #Call the request and turn it into a python format
    response = requests.request("GET", url, params=querystring)
    response = response.json()

    set_info()


def set_info():
    """Update output lables based on API call"""   
    #Update the picture text and date
    picture_date.config(text=response['date'], font=text_font, bg=nasa_white)
    picture_explanation.config(text=response['explanation'], font=text_font, bg=nasa_white)

    #We need to use these 3 images in other functions so make them global
    #Also Tkinter's garbage collector removes photos inside functions if not global
    global img
    global full_img
    global thumb

    #Grab the photo that is stored in the previous request.  Stream=True sets for automatic download
    url = response['url']
    img_response = requests.get(url, stream=True)

    if response['media_type'] == 'image':
        #Get the content of the response and use BytesIO to open it as an image.
        #Keep a reference to this as this is what you can use to save (Image not PhotoImage)
        #Create the full screen image for the second window
        img_data = img_response.content
        img = Image.open(BytesIO(img_data))
        full_img = ImageTk.PhotoImage(img)

        #Create the thumbnail for the main screen
        thumb_data = img_response.content
        thumb = Image.open(BytesIO(img_data))
        thumb.thumbnail((200,200))
        thumb = ImageTk.PhotoImage(thumb)

        #Set the thumnail image
        picture_label.config(image=thumb)
    else:
        #WE have a link to a video...open the video (try july 1st, 2020)
        picture_label.config(image='')
        picture_label.config(text=url)
        webbrowser.open(url)


def full_photo():
    """Open the full size photo in a new window"""
    #global full_img

    top = Toplevel()
    img_label = tkinter.Label(top, image=full_img)
    img_label.pack()


def save_photo():
    """Save the desired photo"""
    #global img
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Image", filetypes=(("JPEG","*.jpg"),("All Files","*.*")))
    img.save(save_name + ".jpg")


#Define GUI Layout
#Create frames
input_frame = tkinter.Frame(root, bg=nasa_blue)
output_frame = tkinter.Frame(root, bg=nasa_white)
input_frame.pack()
output_frame.pack(padx=50, pady=(0,25))

#Layout for input frame
calander = DateEntry(input_frame, width=10,  font=text_font, background=nasa_blue, foreground=nasa_white)
#date_entry = tkinter.Entry(input_frame, width=10)
submit_button = tkinter.Button(input_frame, text="Submit", font=text_font, bg=nasa_light_blue, command=get_request)
full_button = tkinter.Button(input_frame, text='Full Photo', font=text_font, bg=nasa_light_blue, command=full_photo)
save_button = tkinter.Button(input_frame, text="Save Photo", font=text_font, bg=nasa_light_blue, command=save_photo)
quit_button = tkinter.Button(input_frame, text="Exit", font=text_font, bg=nasa_red,command=root.destroy)

calander.grid(row=0, column=0, padx=5, pady=10)
#date_entry.grid(row=0, column=0)
submit_button.grid(row=0, column=1, padx=5, pady=10, ipadx=35)
full_button.grid(row=0, column=2, padx=5, pady=10, ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=20)
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=50)

#Layout for output frame
picture_date = tkinter.Label(output_frame)
picture_explanation = tkinter.Label(output_frame, wraplength=600)
picture_label = tkinter.Label(output_frame)

picture_explanation.grid(row=0, column=0, rowspan=2, padx=10, pady=10) 
picture_label.grid(row=0, column=1, padx=10, pady=10)
picture_date.grid(row=1, column=1, padx=10)

#Call get_request() so you always start with a photo and explination
get_request()

root.mainloop()

