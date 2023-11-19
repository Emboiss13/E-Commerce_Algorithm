import numpy as np
import math


#This function gets the angle between 2 vectors

def calc_angle(x, y):
    theta = 0
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    if cos_theta > 1:
        cos_theta = 1
    else:
        theta = math.degrees(math.acos(cos_theta))
    return theta


#Reading the first line
def Read_Line():
    file = open("history.txt", "r")
    history_file_content = file.readline().strip().split("\n")
    return(history_file_content)


#Gathering data from 1st line
first_line = []
def First_Line_Data():
    Content_List = Read_Line()
    first_line = Content_List[0]
    return(first_line.split())

"""------------------------------------------------------------------------------------"""

#Individual first line data variables
first_line_list = First_Line_Data()
Number_of_Customers = first_line_list[0]
Number_of_Items = first_line_list[1]
Number_of_Transactions = first_line_list[2]

Int_Number_of_Customers = int(Number_of_Customers)
Int_Number_of_Items = int(Number_of_Items)
Int_Number_of_Transactions = int(Number_of_Transactions)

"""------------------------------------------------------------------------------------"""

#Reading the whole file
def Read_History_File():
    file = open("history.txt", "r")
    history_file_content = file.read().strip().split("\n")
    return(history_file_content)

#Removing the first line from data
#Creating a list with all the values on the file
CustomerID_ItemID_List = Read_History_File()[1:]


"""------------------------------------------------------------------------------------"""

#Initializing dictionary variable
#Creating empty vector dictionary
dictionary = {}

def Individial_Values_List_Data():
    for i in range(Int_Number_of_Transactions):
        
        #Getting data on individual transactions
        Get_Values_on_CustomerID_ItemID_List = CustomerID_ItemID_List[i]
        Split_Values_List = Get_Values_on_CustomerID_ItemID_List.strip().split(" ")
        
        #Creating the dictionary with the individual transaction data
        #Create a dictionary where the itemID is the key and the User is the value on the dictionary
        Customer_ID = int(Split_Values_List[0]) 
        Item_ID = int(Split_Values_List[1]) 

        #Create list where the itemID is the key and the Customers who bought that item creates the vector
        if Item_ID in dictionary: # checks if item is already a key in dictinary (at first it wont be)
            dictionary[Item_ID][Customer_ID-1] = 1 # sets the value of the customer id index in the item_id list to 1
        else:
            dictionary[Item_ID] = np.zeros(Int_Number_of_Items, dtype=int)
            dictionary[Item_ID][Customer_ID-1] = 1

    return dictionary
      

#Making the dictionary subscriptable 
dictionary_stored_values = Individial_Values_List_Data()
#print(dictionary_stored_values)

angle_list = []
#Getting x and y values for maths formula
def List_of_angles():
    for i in range(1,Int_Number_of_Items + 1):
        x = dictionary_stored_values.get(i)
        for j in range(1,Int_Number_of_Items + 1):
            y = dictionary_stored_values.get(j)
            if i == j:
                continue
            #Testing
            #print(x," and",y)
            degree = calc_angle(x, y)
            angle_list.append([i,j,degree])
            
    return angle_list


Angle_List = List_of_angles()
#print(Angle_List)


#Retrieving the shopping cart from queries.txt
#Reading the whole file
def Read_Queries_File_Function():
    file = open("queries.txt", "r")
    queries_file_content = file.read().strip().split("\n")
    return(queries_file_content)

#Creating a list with all the values on the file
Read_Queries_File= Read_Queries_File_Function()
#print(Read_Queries_File)



"""------------------------------------------------------------------------------------"""
"""------------------------------------------------------------------------------------"""

#CREATING THE OUTPUT - Functions

#Positive entrie function
def positive_entries_Func(): 
    Total = 0
    for vector in dictionary_stored_values.values():
        Total += sum(vector)
    return Total

Positive_entries = positive_entries_Func()
#print(Positive_entries)


#Average angle function
def Average_Angle_Function():
    count = 0
    angle_count = 0
    angle_average = 0

    for i in Angle_List:
        count += i[2]
        angle_count += 1 
    angle_average =  count/angle_count
    return angle_average

Average_Angle = Average_Angle_Function()
#print("%.2f" % Average_Angle)



"""------------------------------------------------------------------------------------"""
"""------------------------------------------------------------------------------------"""



#OUTPUT

print("Positive entries: " , Positive_entries)
print("Average angle: " , "%.2f" % Average_Angle)

for i in Read_Queries_File:
    Shopping_Cart = i.split(" ")
    print("Shopping Cart: " , i)
    item_match_dictionary = {}
    
    for Items_Shopping_Cart in Shopping_Cart:
        item_on_Cart = int(Items_Shopping_Cart)
        angle_count = 90
        item_match = 0
        

        for Data_on_Angle_List in Angle_List:
            if item_on_Cart == Data_on_Angle_List[0]:
                item_compared_to = Data_on_Angle_List[1]
                angle = Data_on_Angle_List[2]

                if angle < angle_count and str(item_compared_to) not in Shopping_Cart:
                    angle_count = angle
                    item_match = item_compared_to

        if angle_count != 90:
            print("Item: ", item_on_Cart, "; match: " ,item_match, "; angle: " , "%.2f" % angle_count)
             
            if item_match not in item_match_dictionary: 
                item_match_dictionary[item_match] = angle_count

        else: 
            print("Item: ", item_on_Cart, " no match")
    item_match_dictionary = dict(sorted(item_match_dictionary.items(), key=lambda n: n[1]))           
    print("Recomend: " , " ".join(map(str, item_match_dictionary.keys())))

