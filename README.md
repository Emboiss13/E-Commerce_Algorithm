# 🛒 Recommendation System
This repository contains a Python script for a basic recommendation system. The system analyzes historical shopping data to calculate angles between items, and it provides recommendations based on the angles between items in a given shopping cart.
_____

## Functionality

### `calc_angle(x, y)`

- This function calculates the angle (in degrees) between two vectors `x` and `y`.

### `Read_Line()`

- Reads the first line from the "history.txt" file and returns the content as a list.

### `First_Line_Data()`

- Processes the first line data from the "history.txt" file, extracting the number of customers, items, and transactions.

### `Read_History_File()`

- Reads the entire "history.txt" file and returns its content as a list.

### `Individial_Values_List_Data()`

- Processes individual transaction data, creating a dictionary where itemIDs are keys, and the corresponding customers who bought those items create vectors.

### `List_of_angles()`

- Calculates the angles between all pairs of items based on the vectors created for each item.

### `Read_Queries_File_Function()`

- Reads the "queries.txt" file and returns its content as a list.

### `positive_entries_Func()`

- Calculates the total number of positive entries in the dataset.

### `Average_Angle_Function()`

- Calculates the average angle between items.

### Output

- Prints the total number of positive entries, average angle between items, and provides item recommendations for each shopping cart specified in the "queries.txt" file.

## How to Use

1. Ensure you have the "history.txt" and "queries.txt" files in the same directory as the script.

2. Run the script.

3. View the output, which includes the total number of positive entries, average angle between items, and item recommendations for each shopping cart.

***📝Note:*** Make sure the input data files follow the expected format for accurate results.
