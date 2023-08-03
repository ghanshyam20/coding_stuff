def word_count(paragraph):
    words=paragraph.split()
    return len(words)




if __name__=="__main__":
    paragraph=input("enter the paragraph:")
    count=word_count(paragraph)
    print(f"the total number of words in paragraph are {count}")

#simple mini project on paragraph counting ..