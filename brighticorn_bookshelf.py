books = ["To Kill a Mockingbird", "their eyes were watching God"]


print("Brighticorns books")

print("here's what you can do- add, view, check or exit")




while True:
	
	print("here's what you can do- add, view, check or exit")

	command = input("What would you like to do? ")	 #input has to be here or else it wont ask for command again
	command = command.lower()
	
	if command== "exit":
		print("Goodbye!")
		break

	elif command == "add":
		print("add book")
		book_addition = input("what book would you like to add? ")
		books.append(book_addition)
		
		print(f"added {book_addition}")

	elif command == "view":
		print("view books")
		for book in books:
			print(book)

	elif command == "check":
		print("view books")
		book_looking_for = input("what book would you like to see if you have? ")
		
		if book_looking_for in books:
			print(book_looking_for)
		else:
			print("that book isnt in the library")

	else:
		print("either type add, view, check or exit")
		
