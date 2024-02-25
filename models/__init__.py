from models.engine.file_storage import FileStorage

# Create an instance of file storage
"""
Create an instance of FileStorage to handle file-based storage of objects.
"""
storage = FileStorage()

# Reload objects from file
"""
Load previously stored objects from file into the storage instance.
"""
storage.reload()
