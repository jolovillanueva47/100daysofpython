try:
    file=open("test.txt")
    dict={"key":"value"}
    print(dict["key"])
except FileNotFoundError:
    file=open("test.txt","w")
    file.write("Something")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist")
else:
    content=file.read()
    print(content)
finally:
    # file.close()
    # print("File was closed.")
    raise KeyError("This is an error I made up")

