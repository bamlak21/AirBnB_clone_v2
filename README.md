# HBNB - The Console

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

### Repository Contents by Project Task

| Tasks | Files | Description |
| ----- | ----- | ----------- |
| 0: Authors/README File | AUTHORS |
| 1: Pep8 | N/A | All code is pep8 compliant |
| 2: Unit Testing | /tests | All class-defining modules are unittested |
| 3. Make BaseModel | /models/base_model.py | Defines a parent class to be inherited by all model classes |
| 4. Update BaseModel w/ kwargs | /models/base_model.py | Add functionality to recreate an instance of a class from a dictionary representation |
| 5. Create FileStorage class | /models/engine/file_storage.py /models/_init_.py /models/base_model.py | Defines a class to manage persistent file storage system |
| 6. Console 0.0.1 | console.py | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | console.py |	Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | console.py /models/engine/file_storage.py /models/user.py | Dynamically implements a user class |
| 9. More Classes | /models/user.py /models/place.py /models/city.py /models/amenity.py /models/state.py /models/review.py | Dynamically implements more classes |
| 10. Console 1.0 | console.py /models/engine/file_storage.py | Update the console and file storage system to work dynamically with all classes update file storage |

### General Use
