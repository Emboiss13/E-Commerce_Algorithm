import numpy as np 
Customer_ID = 8
ID = 3

dictionary = {}
dictionary[ID][Customer_ID-1] = 1
print(dictionary)


def Get_Values_on_CustomerID_ItemID_List_function():
    for i in range(int(Number_of_Transactions)):
            
            #Getting data on individual transactions
            Get_Values_on_CustomerID_ItemID_List = CustomerID_ItemID_List[i]
            Split_Values_List = Get_Values_on_CustomerID_ItemID_List.strip().split(" ")
            return Split_Values_List
            
#Creating the dictionary with the individual transaction data
#Create a dictionary where the itemID is the key and the User is the value on the dictionary
x = Get_Values_on_CustomerID_ItemID_List_function()
Customer_ID = int(x[0]) 
Item_ID  = int(x[1])             

#Initializing dictionary variable
#Creating empty vector dictionary
dictionary = {}

def Individial_Values_List_Data():
    for i in range(int(Number_of_Transactions)):
        #Create list where the itemID is the key and the Customers who bought that item create a vector
        if Item_ID in dictionary: # checks if item is already a key in dictinary (at first it wont be)
            dictionary[Item_ID][Customer_ID-1] = 1 # sets the value of the customer id index in the item_id list to 1
        else:
            dictionary[Item_ID] = np.zeros(int(Number_of_Items))
            dictionary[Item_ID][Customer_ID-1] = 1
    return dictionary
        

#Testing Individual_Values_List_Data
dictionary_test = Individial_Values_List_Data()
print(dictionary_test)
print(dictionary_test.get(Customer_ID))