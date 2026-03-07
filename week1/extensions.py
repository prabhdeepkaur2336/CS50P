file_name =input("File name: ").lower().strip()

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith((".jpg",".jpeg")):
    print("image/jpg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("document/pdf")
elif file_name.endswith(".txt"):
    print("document/text")
elif file_name.endswith(".zip"):
    print("folder/zip")
else:
    print("application/octet-stream")