#random quotes generator..







import random

def get_random_quote():
    quotes=["The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh","Darkness cannot drive out darkness only light can do that Hate cannot drive out hate only love can do that.- Maya Angelou","Success is not just about making money it's about making a difference - Unknown","The only limit to our realization of tomorrow will be our doubts of today. - Franklin D Roosevelt","It always seems impossible until it's done. - Nelson Mandela"]


    return random.choice(quotes)



if __name__=="__main__":
    quote=get_random_quote()
    print("ranodom qutote:",quote)









