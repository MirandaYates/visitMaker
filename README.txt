This application is built to run and manage a reservation system for a company
This file serves as a "How To" for the webistes functions
This file should be updated as project updates are implemented

Software needed to run the server includes:
	Python 3
	Django

In order to start the server, enter the visitMaker file and enter the command:
	$python3 manage.py runserver

The server can be accessed at http://127.0.0.1:8000 in your browser

For Customers:
	Contact info can be found on the "Contact" page

	Requesting a reservation:
		1. Navigate to the "Request" page
		2. Fill out various fields
		3. Submit your reservation request for review


For Employees:
	Has all customer privileges.

	View all existing reservations:
		1. Navigate to the "Reservations" page (link in header)
		2. Current day and future reservations that have already been made will be listed here ordered by date then time
		3. Lists of all revervations, past and future can be found throught the button at the top
		4. Each calendar day links to a page with a list of that days reservations
		5. Each list can be sorted and searched 

	Making a new reservation:
		1. Navigate to the "Reservations" page
		2. Click "Add a reservation"
		3. Fill out the various fields
		4. Submit the new reservation
		5. A confirmation email can be sent on the confirmation page if desired
		6. The reservation can also be edited or deleted on the confirmation page

	Making a reservation from a request:
		1. Navigate to the "Reservations" page
		2. Click "Requests"
		3. Click pencil icon
		4. Fill out docent field
		5. Submit the new reservation
		6. A confirmation email can be sent on the confirmation page if desired
		7. The reservation can also be edited or deleted on the confirmation page

	Deleting/Modifying a reservation:
		1. Navigate to the "Reservations" page
		2. To delete:
			- click trash can icon in the rightmost column of target reservation
		3. To edit:
			- click pencil icon in the rightmost column of target reservation
			- change data as needed
			- submit

	Create Report:
		1. Navigate to Reports (link in header)
		2. Fill in start and end date
		3. Submit
		4. Detailed data on each tour can be found in Generated Reports Folder
		5. A report with the same start and end date will overwrite the older report existing


For Admin:
	Has all employee and customer privileges.

	User Creation:
		1. From any page navigate to "Register" (located in uppermosst header)
		2. Input Employee's username and password
		3. Submit

	Manage Users:
		1. From any page navigate to "Manage Users" (located in uppermosst header)
		2. Can sort and search list
		3. Use trash can icon to delete
		
