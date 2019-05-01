# imports all functions from tkinter
from tkinter import *

#this function is created to remove common characters 
def remove_match_char(list1, list2):  
  
    for i in range(len(list1)) :  
        for j in range(len(list2)) :  
    		#if common character is found in the two names 
    		#then remove that character
            if list1[i] == list2[j] :  
                c = list1[i]  
   
                list1.remove(c)  
                list2.remove(c)  
    
                list3 = list1 + ["*"] + list2  
   				# returns the altered list with true flag
                return [list3, True]  
  	# if no common character is found 
  	#returns the unaltered list with no flag
    list3 = list1 + ["*"] + list2  
    return [list3, False]  


# backend  
def tell_status() : 
	
	# take a 1st player name from Player1_field entry box 
	p1 = Player1_field.get() 

	# converted all letters into lower case 
	p1 = p1.lower() 

	# replace any space with empty string 
	p1.replace(" ", "") 

	# make a list of letters or characters 
	p1_list = list(p1) 

	# take a 2nd player name from Player2_field entry box 
	p2 = Player2_field.get() 
	p2 = p2.lower() 
	p2.replace(" ", "") 
	p2_list = list(p2) 

	# taking a flag as True initially 
	proceed = True
	
	# keep calling remove_match_char function 
	# untill common characters is found or 
	# keep looping untill proceed flag is True 
	while proceed : 

		# function calling and store return value 
		ret_list = remove_match_char(p1_list, p2_list) 

		# take out concatenated list from return list 
		con_list = ret_list[0] 

		# take out flag value from return list 
		proceed = ret_list[1] 

		# find the index of "*" / border mark 
		star_index = con_list.index("*") 

		# list slicing perform 
		
		# all characters before * store in p1_list 
		p1_list = con_list[ : star_index] 

		# all characters after * store in p2_list 
		p2_list = con_list[star_index + 1 : ] 


	# count total remaining characters 
	count = len(p1_list) + len(p2_list) 

	# list of FLAMES acronym 
	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"] 

	# keep looping untill only one item 
	# is not remaining in the result list 
	while len(result) > 1 : 

		# store that index value from 
		# where we have to perform slicing. 
		split_index = (count % len(result) - 1) 

		# this steps is done for performing 
		# anticlock-wise circular fashion counting. 
		if split_index >= 0 : 

			# list slicing 
			right = result[split_index + 1 : ] 
			left = result[ : split_index] 

			# list concatenation 
			result = right + left 

		else : 
			result = result[ : len(result) - 1] 

	# insert method inserting the 
		# value in the text entry box. 
	Status_field.insert(10, result[0]) 


# Function for clearing the 
# contents of all text entry boxes 
def clear_all() : 
	Player1_field.delete(0, END) 
	Player2_field.delete(0, END) 
	Status_field.delete(0, END) 
	
	# set focus on the Player1_field entry box 
	Player1_field.focus_set() 


# Front end 
if __name__=="__main__":
	root= Tk()

	root.geometry("350x125")
	root.title("Flames")


	label1=Label(root,text="Player1:")
	label2=Label(root,text="Player2:")
	label3=Label(root,text="Status:")

	label1.grid(row=1,column=0,sticky="E")
	label2.grid(row=2,column=0,sticky="E")
	label3.grid(row=4,column=0,sticky="E")

	Player1_field=Entry(root)
	Player2_field=Entry(root)
	Status_field=Entry(root)

	Player1_field.grid(row = 1, column = 1, ipadx ="50")   
	Player2_field.grid(row = 2, column = 1, ipadx ="50")   
	Status_field.grid(row = 4, column = 1, ipadx ="50")   

	button1 = Button(root, text = "Submit",command=tell_status)
	button2 = Button(root, text = "Clear",command=clear_all) 

	button1.grid(row = 3, column = 1)  
	button2.grid(row = 5, column = 1) 


root.mainloop()

