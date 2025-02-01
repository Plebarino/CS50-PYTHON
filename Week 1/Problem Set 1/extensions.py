name = input("File name: ").strip().lower()

if name.endswith(".gif"):
    print("image/gif")
elif name.endswith(".jpg") or name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith("pdf"):
    print("application/pdf")
elif name.endswith(".txt"):
    print("text/plain")
elif name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")


# match name:
#     case "jpg":
#         print("image/jpeg")
#     case "jpeg":
#         print("image/jpeg")
#     case "png":
#         print("image/png")
#     case "pdf"
#         print("application/pdf")
#     case "txt"
#         print("text/plain")
#     case ""


#print(new_name)