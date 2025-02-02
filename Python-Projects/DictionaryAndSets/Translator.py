words={
    "NAME"  : "نام",
    "TELL" : "بتاؤ",
    "LOVE" : "محبت",
    "HEART" : "دل",
    "GO" : "جاؤ"
}
input = input("Enter Word : ").upper()
for word in words:
    if word==input :
        print(words.get(word))
        break
else:
    print("Not Available Rn...")
    
       