Project Title
Inventory Management System with Stock Tracking (CLI-Based)

1. Project Description
This project is a command-line inventory management system developed using Python and Object-Oriented Programming (OOP). It allows a user to manage products efficiently by performing operations such as adding, viewing, updating, and deleting products. The system also tracks stock changes, recording when items are added or removed.
The project is modular, with separate files for the Product and Inventory classes, making it easier to maintain and expand.
2. Objectives
The main goals of this project are:
1.	To provide a simple, interactive inventory management tool. 
2.	To allow CRUD operations for products (Create, Read, Update, Delete). 
3.	To track stock additions and removals with timestamps. 
4.	To demonstrate modular programming using Python classes. 
5.	To design a system that can be expanded for future enhancements.

3. Tools and Technologies
Component	     Description
Programming Language	       Python 
Modules Used	       datetime for tracking timestamps
IDE/Editor	       VS Code
Platform 	       Windows


4. Project Structure
The project is organized into three main files:
inventory_project/
│── main.py           # Program entry point and menu
│── product.py        # Product class
│── inventory.py      # Inventory class and CRUD methods
4.1 product.py
Defines the Product class:
•	Attributes: id, name, quantity, price, logs. 
•	Methods: 
o	add_stock(amount) – Adds quantity and logs the change. 
o	remove_stock(amount) – Removes quantity and logs the change. 
o	update(name, price) – Updates product name and price. 
o	show() – Displays product information. 
o	show_logs() – Displays the history of stock changes. 
4.2 inventory.py
Defines the Inventory class:
•	Stores all products in a list and maintains a unique product ID. 
•	Methods: 
o	add_product() – Add a new product. 
o	view_products() – List all products. 
o	view_product() – View a product by ID. 
o	view_logs() – View stock logs for a product. 
o	update_product() – Update product name and price. 
o	add_stock() – Increase quantity of a product. 
o	remove_stock() – Decrease quantity of a product. 
o	delete_product() – Remove a product by ID. 
o	delete_out_of_stock() – Remove products with zero quantity. 
4.3 main.py
This file runs the CLI menu and interacts with the Inventory class:
•	Presents a menu with numbered options. 
•	Calls the appropriate Inventory method based on user input. 
•	Loops until the user chooses to exit. 
5. Program Workflow
1.	Run the program using main.py. 
2.	The menu is displayed with all available operations. 
3.	The user selects an option by entering the corresponding number. 
4.	The program performs the operation (add, view, update, delete, manage stock). 
5.	Stock changes are recorded in the product logs with timestamps. 
6.	The menu reappears until the user exits the program. 
Menu Example:
--- INVENTORY MENU ---
1 Add Product
2 View All Products
3 View Product by ID
4 Update Product
5 Add Stock
6 Remove Stock
7 Delete Product
8 Delete Out-of-Stock Products
9 View Logs
0 Exit
6. CRUD Operations
Operation	Method	Description
Create	add_product()	Add a new product
Read	view_products()	List all products
Read	view_product()	View product by ID
Read	view_logs()	View stock history
Update	update_product()	Update product name/price
Update	add_stock()	Increase product quantity
Update	remove_stock()	Decrease product quantity
Delete	delete_product()	Remove product by ID
Delete	delete_out_of_stock()	Remove products with zero stock
7. Advantages
•	Modular Design: Code is separated into different files for easy maintenance. 
•	OOP Principles: Product and Inventory are implemented as classes. 
•	Track Stock Changes: Logs track stock changes with timestamps. 
•	Scalable: Easy to extend with features like database storage or search functionality. 
•	User-Friendly: Simple CLI menu for easy interaction. 
8. Future Enhancements
•	Save inventory data in JSON or a database for persistence. 
•	Implement user authentication for multiple users. 
•	Add search and filter options by name, quantity, or price. 
•	Generate reports or export CSV files of inventory data. 
9. Conclusion
The project provides a working inventory management system with CRUD operations and stock tracking. Using Python and OOP makes it modular, reusable, and maintainable. It demonstrates practical programming concepts such as class design, modularization, and interactive command-line interfaces.

