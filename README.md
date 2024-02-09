# Step One: Develop a Command Interpreter for Managing Your AirBnB Objects

This initial step lays the foundation for constructing your first full-fledged web application: the AirBnB clone. It holds significant importance as the functionalities developed here will be utilized throughout subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development.

Each task is interlinked and contributes towards:

- Establishing a parent class (BaseModel) responsible for initializing, serializing, and deserializing future instances.
- Creating a streamlined process of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.
- Defining all necessary classes for AirBnB (such as User, State, City, Place, etc.) that inherit from the BaseModel.
- Implementing the initial abstracted storage engine for the project: File storage.
- Developing comprehensive unit tests to validate all classes and the storage engine.

### What is a Command Interpreter?

Think of it as akin to the Shell, but tailored to a specific use-case. In our context, it enables us to manage the objects within our project by allowing us to:

- Create new objects (e.g., a new User or a new Place).
- Retrieve objects from various sources such as files or databases.
- Perform operations on objects (e.g., count, compute statistics, etc.).
- Update attributes of objects.
- Delete objects.

**Resources:** 
<https://docs.python.org/3.8/library/cmd.html>
<https://www.pythonsheets.com/notes/python-tests.html>

By Alao Samuel <malaosamuel2020@gmail.com>
