from queue import Empty
from tkinter import *
from last import response, speak
import speech_recognition as s
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
from googletrans import Translator
from playsound import playsound

BG_GRAY = "#ABB2B9"
BG_COLOR = "#EAECEE"
TEXT_COLOR = "#17202A"
bot_name = 'Abhijnyah'
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("AICTE Welcomes you")
        self.window.iconbitmap('E:\Python_Chatbot\AICTE_logo-removebg-preview.ico')
        self.window.resizable(width=True, height=True)
        self.window.configure(width=670, height=550, bg='black')
        
        # head label
        global head_label
        head_label = Label(bg='dodger blue', text="Abhijnyah here!! let's chat", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1, relheight = 0.15)
       
        #Image 
        self.frame = Frame(self.window, width=6, height=4)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.06, rely=0.07)
        self.img = (Image.open("logo_bot.png"))
        self.resized_image= self.img.resize((60,60))
        self.new_image= ImageTk.PhotoImage(self.resized_image)
        self.Photo_label = Label(self.frame, image = self.new_image)
        #self.Photo_label.place(relx=0.82, rely=0.18, relheight=6, relwidth=0.15)
        self.Photo_label.pack(anchor = 'center')

        # tiny divider
        line = Label(self.window, width=450, bg='black')
        line.place(relwidth=1, rely=0.142, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=10, height=2, bg='deep sky blue',
                                font=FONT, padx=16, pady=10, wrap = WORD)
        self.text_widget.place(relheight=0.67459, relwidth=1, rely=0.15)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        self.text_widget.tag_config('qu', background="white", foreground="black")

        # scroll bar
        scrollbar = Scrollbar()
        scrollbar.place(relheight=1, relx=0.98)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg='dodger blue', height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
         # tiny divider
        line = Label(self.window, width=450, bg='black')
        line.place(relwidth=1, rely=0.825, relheight=0.012)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="white", fg='black', font=FONT, border="2")
        self.msg_entry.place(relwidth=0.74, relheight=0.03, rely=0.02, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
    
        # send button
        self.send = (Image.open("send.png"))
        self.resized_Send= self.send.resize((30,30))
        self.new_send= ImageTk.PhotoImage(self.resized_Send)
        send_button = Button(bottom_label, image = self.new_send , width=0,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.02, relheight=0.03, relwidth=0.10)

        #Hindi Audio
        self.send = (Image.open("send.png"))
        self.resized_Send= self.send.resize((30,30))
        self.new_send= ImageTk.PhotoImage(self.resized_Send)
        send_button = Button(bottom_label, image = self.new_send , width=0,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.02, relheight=0.03, relwidth=0.10)

        # speak button
        self.speak = (Image.open("Speak.png"))
        self.resized_Speak= self.speak.resize((50,50))
        self.new_speak= ImageTk.PhotoImage(self.resized_Speak)

        speak_button = Button(head_label, image = self.new_speak , width=10,
                             command=lambda: self._on_click(None))
        speak_button.place(relx=0.87, rely=0.05, relheight=0.70, relwidth=0.08)

        #IPAudio_button = Button(bottom_label, text="Audio IP", fg='black', font=FONT_BOLD, width=20, bg='#83838B',
                   #          command=lambda: self.takeQuery(None))
        self.img2 = (Image.open("mic2.png"))
        self.resized_image2= self.img2.resize((20,20))
        self.new_image2= ImageTk.PhotoImage(self.resized_image2)

        IPAudio_button = Button(bottom_label, image= self.new_image2, width=20,
                             command=lambda: self.takeQuery(None))
        IPAudio_button.place(relx=0.87, rely=0.02, relheight=0.03, relwidth=0.1)
        
        select_lang = tk.StringVar()
        lang = ttk.Combobox(self.window, textvariable = select_lang)
        lang['values'] = ["English", "Hindi"]
        lang['state'] = 'readonly'


        lang.place(relx=0.86, rely=0.115, relheight=0.02, relwidth=0.1)



        def lang_change(event):
            print(lang.get())
            a = lang.get()
            if(a == "Hindi"):
                print("Hindi")
                IPAudio_button = Button(bottom_label, image= self.new_image2, width=20,
                             command=lambda: self.tQuery(None))
                IPAudio_button.place(relx=0.87, rely=0.02, relheight=0.03, relwidth=0.1)

                speak_button = Button(head_label, image = self.new_speak , width=10,
                             command=lambda: self._click(None))
                speak_button.place(relx=0.87, rely=0.05, relheight=0.70, relwidth=0.08)

                send_button = Button(bottom_label, image = self.new_send , width=0,
                             command=lambda: self._Hon_enter_pressed(None))
                send_button.place(relx=0.77, rely=0.02, relheight=0.03, relwidth=0.10)

                self.msg_entry = Entry(bottom_label, bg="white", fg='black', font=FONT, border="2")
                self.msg_entry.place(relwidth=0.74, relheight=0.03, rely=0.02, relx=0.011)
                self.msg_entry.focus()
                self.msg_entry.bind("<Return>", self._on_enter_pressed)            
            else:
                print("English")
                IPAudio_button = Button(bottom_label, image= self.new_image2, width=20,
                             command=lambda: self.takeQuery(None))
                IPAudio_button.place(relx=0.87, rely=0.02, relheight=0.03, relwidth=0.1)

                speak_button = Button(head_label, image = self.new_speak , width=10,
                             command=lambda: self._on_click(None))
                speak_button.place(relx=0.87, rely=0.18, relheight=0.68, relwidth=0.08)

                send_button = Button(bottom_label, image = self.new_send , width=0,
                             command=lambda: self._on_enter_pressed(None))
                send_button.place(relx=0.77, rely=0.02, relheight=0.03, relwidth=0.10)

                self.msg_entry = Entry(bottom_label, bg="white", fg='black', font=FONT, border="2")
                self.msg_entry.place(relwidth=0.74, relheight=0.03, rely=0.02, relx=0.011)
                self.msg_entry.focus()
                self.msg_entry.bind("<Return>", self._on_enter_pressed)

        lang.bind('<<ComboboxSelected>>', lang_change)

    def _auto_rec(self):
        # Update the listbox
        def update(data):
            # Clear the listbox
            my_list.delete(0, END)

            # Add Questions to listbox
            for item in data:
                my_list.insert(END, item)

        # Update entry box with listbox clicked
        def fillout(e):
            # Delete whatever is in the entry box
            self.msg_entry.delete(0, END)

            # Add clicked list item to entry box
            self.msg_entry.insert(0, my_list.get(ANCHOR))

        # Create function to check entry vs listbox
        def check(e):
            # grab what was typed
            typed = self.msg_entry.get()

            if typed == '':
                data = Questions
            else:
                data = []
                for item in Questions:
                    if typed.lower() in item.lower():
                        data.append(item)

            # update our listbox with selected items
            update(data)				

        #self.msg_entry.pack()

        # Create a listbox
        #List Box
        my_list = Listbox(self.window, width=50)
        my_list.place(relwidth=0.74, relheight=0.06, rely=0.94, relx=0.011)

        # Create a list of pizza Questions
        Questions =['Can you tell me What is the goal/moto/reason/aim for Scheme for Promoting Interests, Creativity and Ethics among Students scheme?', 'Can you tell me What is the reason behind formation of SPICES scheme in AICTE?', 'Can you tell me What is the goal/moto/reason/aim for SPICES scheme?', 'Can you tell me What is the aim of SPICES scheme?', 'Can you tell me What is AICTE expecting from the institution under SPICES scheme?\n\n', 'Can you tell me Under Spices scheme what AICTE is expecting from the institution?', 'Can you tell me For what other things AICTE look forward to institutions under SPICES scheme?', 'Can you tell me Under Spices scheme Are Students Chapters and Students Societies also eligible to apply?', 'Can you tell me Are Students Chapters and Students Societies also eligible to apply in SPICES scheme?', 'Can you tell me It is allowed / possible to use the grant to other coordinator/faculty/facilitator which is been given/ qualified to institute for spices scheme in aicte?\n', 'Can you tell me Can the grant be utilised by the institute on the expenditures pertaining to Faculty Coordinator/ Co-coordinator or any other faculty member under SPICES scheme?', 'Can you tell me How many proposals can be submitted by the institute under SPICES scheme?\n\n', 'Can you tell me In how many proposal institute can seek support for finance under SPICES scheme?', 'Can you let me know/ tell us Institute can submit proposal for how many club under SPICES scheme?', 'Can you tell me Will my institute be eligible to apply, if project is granted once under SPICES scheme?/"Once the SPICES project is granted, institution is still eligible under SPICES scheme?\n', 'Can you tell me Once the SPICES project is granted, institution is still eligible under SPICES scheme?/Will my institute be eligible to apply, if project is granted once under SPICES scheme?', 'Can you tell me Any of the stream can apply for SPICES Scheme?"/"Can non-technical/ non-engineering clubs apply under this SPICES scheme?\n', 'Can you tell meCan non-technical/ non-engineering clubs apply under this SPICES scheme?"/Any of the stream can apply for SPICES Scheme?', 'Can you tell me Can I get the remittance/money order in favor of the Coordinator’s/facilitator account name under SPICES scheme?', 'Can you tell me Can I get the payment/money in favor of the Coordinator’s / facilitator account name under SPICES scheme?', 'Can you tell me Under spices scheme in aicte can we get money, fee, cheque in favor of coordinator/facilitator account name?', 'Can you tell me What time AICTE takes to process proposal given by institutes for SPICES? And where to contact for further information under SPICES scheme?\n\n', 'Can you tell me How much time institute need to wait for SPICES proposal processing by AICTE under SPICES scheme?', 'Can you tell me How much time is taken by AICTE for processing the proposal under SPICES scheme?', 'Can you tell meCan institute utilise the interest accrued on grant under SPICES scheme?\n\n', 'Can you tell me Does any Institute can utilise interest of grant for other purpose which is given for SPICES club ?', 'Can you tell me Under SPICES scheme does interest accured on grant can institute apply for other purpose?', 'Can you tell me If The club intends to organize events jointly with other institutes/ organization. Is that encouraged under SPICES scheme?', 'Can you tell meIs any collaborations allowed with other organization/institute/agency/body, etc under SPICES scheme?', 'Can you tell me What things institues should achieve to get support from AICTE for scheme for Promoting Interests, Creativity and Ethics among Students Course/SPICES scheme?', 'Can you tell me What are the strong points which enhance possibility of SPICES support from AICTE under SPICES scheme?', 'Can you tell me How institute can get support for SPICES course from AICTE under SPICES scheme?', 'Can you tell me What are the strong points which enhance possibility of support from AICTE? under SPICES scheme', 'Can you tell me Where to submit application for Registration as a NEEM Facilitator under NEEM scheme?', 'Can you tell me What is the process to register as NEEM Facilitator/Applicant/coordinator/candidate under NEEM scheme?', 'Can you tell me Let me know Is there any registration fee for applying under NEEM scheme?', 'Can you tell me What is the regsiteration fee for NEEM Scheme?', 'Can you tell me What amount need to pay to apply under Neem Scheme?', '\nCan you tell me Under NEEM scheme is procedural / processing fees is refundable or not under NEEM scheme?', 'Can you tell us that Is Processing fee under scheme is refundable or not for NEEM ?', 'Can you tell me What is the eligibility criteria of a NEEM Facilitator under NEEM scheme? \n', 'Can you tell me How Faciliatator/Applicant/Participant can be eligible for NEEM scheme?', 'Can you tell me Does NEEM Scheme and the exemptions under NEEM Scheme fall under the PF and ESI Act.?', 'Can you tell me What is the Maximum capacity to train students in registered companies or registered industries for the purpose of providing training under NEEM?', 'Can you tell me Under NEEM scheme what is the maximum capacity to train students in registered students or companies for providing training?', 'Let me know Is there any certification after completion of training under NEEM Scheme?', 'Can you tell that after completion of training is certificate provided under NEEM scheme?', 'let me know is any stipend is provided/given to students under NEEM scheme/National Employability Enhancement Mission?', 'Can you tell Is any Stipend available for students under NEEM scheme?', 'Can you tell us is grant provided/given to NEEM facilitator under NEEM Scheme/National Employability Enhancement Mission?', 'Let me know Is any grant available for approved NEEM Facilitator under NEEM scheme?', '\nCan you tell me It is possible that if a already enrolled student drops in between than new student can be added under NEEM scheme/National Employability Enhancement Mission?', 'Can you tell me What If a student enrolled for a course drops in between, can a new student be added under NEEM Scheme?', 'Can you tell me Is it compulsory/required giving Aadhar number is mandatory under NEEM Scheme/National Employability Enhancement Mission?', 'Let me know Is taking Attendance of the student is compulsory under NEEM Scheme/National Employability Enhancement Mission?', '\nCan you tell me Who is the one that will provide training under NEEM Scheme/National Employability Enhancement Mission?', 'Can you tell me Who will be provide the training under NEEM scheme?', 'Can you tell me What is the time period or Duration of training under NEEM ?/National Employability Enhancement Mission', 'Can you tell me What is the list of designated trades and industries for the purpose of training under NEEM Scheme /National Employability Enhancement Mission?', '\nCan you tell me Under what age group of trainees can enrolled under NEEM Scheme/National Employability Enhancement Mission?', 'Can you tell me What should be the age group of trainees to be enrolled under NEEM Scheme?', 'Can you tell me What group of people can register as participants under ATAL Scheme/AICTE Training & Learning Academy for participants?', 'Can you tell me Who can register as a participant under ATAL/AICTE Training & Learning Academy for participants?', 'Can you tell meHow to apply for workshops under ATAL scheme/AICTE Training & Learning Academy for participants? \n', 'Can you tell meWhat is the procedure to apply for workshops under ATAL Scheme/AICTE Training & Learning Academy for participants?', 'Can you tell me What to do if verification email not recieved by the new user during registeration on ATAL PORTAL', 'Can you tell me Whom should I contact, if verification email not received by the new user during registration on ATAL portal?', 'It is possible to change phone no. and email used during registeration under ATAL Scheme/AICTE Training & Learning Academy for participants?', 'Can I change my Email and Phone No. used during registration under ATAL Scheme/AICTE Training & Learning Academy for participants?', 'Can you tell me How many FDPs/CPDPs a participant can attend under ATAL scheme/AICTE Training & Learning Academy for participants?', 'Can you tell meHow to retrieve the forgot password under ATAL scheme/AICTE Training & Learning Academy for participants?', 'What method/procedure can be follow to retrieve forgot password uner ATAL Scheme?', 'Can you tell meHow to check the status of workshops for which I have applied under ATAL scheme/AICTE Training & Learning Academy for participants?\n\n', "Can you tell me How can I find out the status of the workshops I've applied for through the ATAL scheme?", "Can you tell meHow do I find out the status of the workshops I've applied for through the ATAL scheme/AICTE Training & Learning Academy for participants?", 'Can you tell me Can I apply for multiple workshops with the same dates under ATAL scheme?\n\n', 'Can you tell me Can I apply for more than one workshop with the same dates under the ATAL scheme?', 'Can you tell meCan I apply for numerous workshops with the same dates under the ATAL scheme/AICTE Training & Learning Academy for participants?', "Can you tell me How do I modify the ATAL scheme's General Details field?", 'Can you tell me For which standard & discipline, the Courses shall be delivered through SWAYAM scheme?', 'can you tell me What is AICTE-NEQIP Scheme? can you tell me about the AICTE-NEQIP Scheme? \ncan you Please provide the details of AICTE-NEQIP Scheme?', 'can you tell me What is the eligibility of Institutes to participate and avail the Financial Grant–in-AID under the AICTE-NEQIP Scheme? \n', 'can you tell me What are the Objectives of AICTE – NEQIP Scheme/AICTE-NORTH EAST QUALITY IMPROVEMENT PROGRAMME?\n', 
        'can you tell me Which are the eligibility norms/requirement of the Institutions to avail grant-in-aid under the AICTE – NEQIP Scheme /AICTE-NORTH EAST QUALITY IMPROVEMENT PROGRAMME?', 'can you tell me How the IDPs can be sent AICTE – NEQIP Scheme? \n', 'can you tell me Are the Institutes already receiving TEQIP Grant eligible to apply under the AICTE – NEQIP Scheme? \n', 'can you tell me What is the method of assessment of the Proposals AICTE – NEQIP Scheme?\n', 'can you tell me What is the time duration of the Project AICTE – NEQIP Scheme?\n', 'can you tell me What is the limit of funds under the AICTE – NEQIP Scheme? \n', 'can you tell me What are the documents required to be submitted by the Institute at the time of issue of Offer Letter for grant of Financial Aid under the AICTE – NEQIP Scheme?', 'can you tell me Which are the documents required to be submitted for each disbursement after the release of 25% of advance towards the first installment AICTE – NEQIP Scheme/AICTE-NORTH EAST QUALITY IMPROVEMENT PROGRAMME?', 'tell me What is the process of Grant of 2nd Installment under the AICTE – NEQIP Scheme/AICTE-NORTH EAST QUALITY IMPROVEMENT PROGRAMME?', 'can you tell me Which department at AICTE deals with the NEQIP matters AICTE – NEQIP Scheme? \n', 'can you tell me Who is the Director in-charge of NEQIP and what is e-mail ID AICTE – NEQIP Scheme? \nCan you tell me that who is the Director in-charge of NEQIP? Can you provide what is e-mail ID of AICTE-NEQIP?', 'can you tell me Is it essential for the Institution for to have the Board of Governors (BoG) AICTE – NEQIP Scheme? ', 'can you tell me In my Institute the faculties / staff are assigned additional duty of works relating to NEQIP over & above their normal duty. ', 'you tell me Whether the training programme attended by the faculty of any of the beneficiary institutions under AICTE-NEQIP Scheme as Career Advancement Scheme (CAS) can be taken as per of the AICTE – NEQIP Scheme?', 'Can you tell me Can any portion of the sanctioned amount be diverted for any purpose other than that for which it has been sanctioned or the funds under different heads of expenses can be clubbed AICTE – NEQIP Scheme?', 'Can you tell me What is the Area of land on which AICTE HQ building has been constructed. provide the details abour area of land on which AICTE HQ building has been constructed.', 'Can you tell me What is the permissible/achieved FAR of the HQ building? ', 'Can you tell me What is total built-up area of HQ building? \n', 'Can you tell me When was the completion certificate issued under EMC for AICTE? who will issued the completion certificate under EMC under AICTE?', 'Can you tell me Permission/Approval of which agencies have been taken for construction of building under EMC? ', 'Can you tell me What are the main features of AICTE HQ building?', 'Can you tell me How the Guest House booking is done? \n', '\nCan you tell me what is total premises of Built-up area?', 'What is the Difference between PMKVY & PMKVY-TI? ', 'Can you tell me Where to submit application of PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me What is the Eligibility of any Institution under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?\n', 'Can you tell me Upto what Age group of students to be enrolled under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES.', 'Can you tell me What are the Level of course which may be offered under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can any Industry be associated in training programme under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES? ', 'Can you tell me What are Category – I, II & III under PMKVY-TI? ', 'Can you tell me What details for Faculty and Machines are to be given in online application under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES? ', 'Can you tell me When course may be started under PMKVY-TI.? ', 'Can you tell me Is Any Stipend is available for students/hostel under PMKVY-TI? ', 'Can you tell me What is the Timing of running programme under PMKVY-TI? ', 'Can you tell me Whether security has to be taken from the student under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES? ', 'Can you tell me about Training of Trainers (TOT) under PMKVY-TI? let me know Training of trainer under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me what If a student enrolled for a course and he drops in between can a new student by added under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me Who will do the assessment and certification under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me Who will pay assessment fee under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me How to submit claim for 1st Installment of Grant under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me When will the 2nd Installment be released under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me Is giving Aadhar number is mandatory under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me Which curriculum to be followed for training under PMKVY-TI?', 'Can you tell me Is it mandatory to submit Mandate Form under PMKVY-TI?', 'Can you tell me what to do when Facing issues while creating Batches on Portal under PMKVY-TIPRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me Is taking Attendance of the student is compulsory under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me What is the maximum batch size to start the course under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES? ', 'Can you tell me What type of Expenditure/things can be booked for the Course under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me What is the maximum Time line for Course under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me What is the eligibility criteria of the student under PMKVY-TI/PRADHAN MANTRI KAUSHAL VIKAS YOJANA TECHNICAL INSTITUTES?', 'Can you tell me Who can apply for the Grants under AQIS Scheme?', 'Can you tell me When the proposals can be submitted under AQIS? ', 'Can you tell me Can a proposal be submitted in the form of Hard Copy under AQIS?', 'Can you tell me How are the proposals considered and processed for being eligible to receive grants under AQIS? ', 'Can you tell me How do institution would come to know about the award of grant for the Proposal under AQIS? ', 'Can you tell me In how many stages/installments, grants are released to the grantee Institution under AQIS? ', 'Can you tell me Can a project proposal be revised midway after receipt of the grants under AQIS?', 'Can you tell me Is it necessary to procure equipments proposed by the Institutes in its initial proposal and approved by the Evaluation Committee under AQIS?', 'Can you tell me What will be the status of assets created from out of AICTE grants under AQIS? ', 'Can you tell me Can Institutes incurre expenditure on overhead (Admin. Charges, including audit fee) from out of the grants released by AICTE under AQIS?', 'Can you tell me When should the project completion report with all mandatory documents, be submitted under AQIS? ', 'Can you tell me Which are the mandatory/required documents required to be submitted for release of final installment for the Faculty Development Program (FDP) under AQIS?', 'Can you tell me What are the mandatory documents required to be submitted for release of subsequent recurring grants for the scheme like RPS & MODROBS where non-recurring grants are released under AQIS?', 'Can you tell me When the project completion report is required to be submitted under AQIS? at what time Project completions report reqired to be submitted under AQIS?', 'Can you tell me What is the method/system/procedure/technique of refunding unspent balance under AQIS?', 'Can you tell me What is the SWAYAM Scheme in the Aicte portal ? ', 'Can any person in the world register/Enroll/Apply a Course on SWAYAM? ', 'Can you tell me How learner can choose the course under Swayam scheme?', 'Can you tell me Which organization and institues deliver MOOCs on SWAYAM scheme?', 'What is the Format/Pedagogy of MOOCs production under Swayam scheme? ', 'is the Courses on the Swayam are free of cost?', 'What does the learner recieved after the end of the Swayam course? ', 'Has the Government issued any policy regarding transfer of credits earned by a student through MOOCs on SWAYAM?', 'Is the SWAYAM a ‘New Plan’ proposal not included in the current Plan period under Swayam? ', 'What is the genesis/reason/motto of launching the SWAYAM?Whvernment embarked upon an ICT Programme in the Past under Swayam?', 'Tell me that does Has MHRD had any experience in developing/building similar material under Swayam?', 'Is SWAYAM programme is a the part of the Digital India Programme under Swayam?', 'Can you just tell me Has the Ministry/government issued any Guidelines/Information on the preparation of MOOCs under Swayam?', 'Let me know Does the Ministry provide funding for development/progress of MOOCs to the Institutions under Swayam?', 'What are sailent features on transfer of Credits earned through SWAYAM by a student to the Institute where the student is studying under Swayam.']        
        # Add the Questions to our list
        update(Questions)

        # Create a binding on the listbox onclick
        my_list.bind("<<ListboxSelect>>", fillout)

        # Create a binding on the entry box
        self.msg_entry.bind("<Key>", check)
        self.window.mainloop()

    def _click(self,event):
        translator = Translator()
        global b,c
        b = translator.translate(a,src='en',dest=str('hi'))
        c = b.text
        from gtts import gTTS
        import os

        tts = gTTS(text = c, lang='hi')
        tts.save("audio.mp3")
        playsound("audio.mp3")




    def _on_click(self, event):
        speak(a)

    def tQuery(self, event):
        sr = s.Recognizer()
        sr.pause_threshold = 0.7
        print("your bot is listening try to speak")
        with s.Microphone() as m:
            try:
                audio = sr.listen(m)
                query = sr.recognize_google(audio, language='hi-in')
                self.msg_entry.delete(0, END)
                self.msg_entry.insert(0, query)
                translator = Translator()
                query = translator.translate(query,src='hi',dest=str('en')).text
                self._from_bot()
                print(query)
            except Exception as e:
                print(e)
                print("not recognized")

    def takeQuery(self, event):
        sr = s.Recognizer()
        sr.pause_threshold = 0.7
        print("your bot is listening try to speak")
        with s.Microphone() as m:
            try:
                audio = sr.listen(m)
                query = sr.recognize_google(audio, language='eng-in')
                self.msg_entry.delete(0, END)
                self.msg_entry.insert(0, query)
                self.ask_from_bot()
            except Exception as e:
                print(e)
                print("not recognized")

    def ask_from_bot(self):
        self.query = self.text_widget.get()
        self._auto_rec()
        a = response(self.query)
      
        msg1 = f"You: {self.query}\n\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1, 'qu')
        self.text_widget.configure(state=DISABLED)
       
        self.msg_entry.insert(END, "bot : " + str(a))
        msg2 = f"{bot_name}: {a}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)
        self.msg_entry.delete(0, END)
        #self.msg_entry.yview(END)

    def _Hinsert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        #t1 = msg1.grid(row=0,column=0)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1, 'qu')
        self.text_widget.configure(state=DISABLED)
        
        global a
        a = response(msg)
        translator = Translator()
        b = translator.translate(a, src = 'en', dest = 'hi')
        c = b.text 
        print(c)
        msg2 = f"{bot_name}: {c}\n\n"
        #t2 = msg1.grid(row=0,column=5)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

    def _Hon_enter_pressed(self, event):
            msg = self.msg_entry.get()
            self._Hinsert_message(msg, "You")
            if(msg != ""):
                self._auto_rec()
        
   
    def update(self, data):
        # Clear the listbox
        self.msg_entry.delete(0, END)

        # Add Questions to listbox
        for item in data:
            self.msg_entry.insert(END, item)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        if(msg != ""):
            self._auto_rec()
        
   

    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n"
        #t1 = msg1.grid(row=0,column=0)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1, 'qu')
        self.text_widget.configure(state=DISABLED)
        
        global a
        a = response(msg)
        
        msg2 = f"{bot_name}: {a}\n\n"
        #t2 = msg1.grid(row=0,column=5)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()

