#musicplaylist-pgm
from playsound import playsound
import random
print("\n")
print("="*145)
print(" \t\t~PROGRAM  TO  HELP  USER  FIND  A  SUITABLE  PLAYLIST~\n\n\n")
print("="*145)
print("\n\n")
print("Choice 1 Happy music")
print("Choice 2 Soft music")
print("Choice 3 melodious music")
print("\n\n")
print("="*145)

print("Please press enter to continue...")
####list
happy_list=[r"C:\Users\sanjana\Desktop\WTprojs\Pharrell Williams - Happy (Video).mp3.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\All izz well.mp3.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\butter.mp3.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\sooraj ki baahon mein.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\dynamite.mp3.mp3"]
soft_list=[r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Perfect.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Falling.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\My heart will go on.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Main tumhaara.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Hawayein.mp3"]
melodious_list=[r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\A thousand years.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Memories.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Agar tum saath ho.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Fix me up.mp3.mp3",r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\yt1s.com - Raataan Lambiyan  Lyric VideoShershaahSidharth  KiaraTanishk BJubinAsees.mp3 "]
 
#####dictionary 

happy_d={'a':r"C:\Users\sanjana\Desktop\WTprojs\Pharrell Williams - Happy (Video).mp3.mp3", 'b': r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\All izz well.mp3.mp3",'c':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\butter.mp3.mp3",'d':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\sooraj ki baahon mein.mp3",'e':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\dynamite.mp3.mp3"}
soft_d={'A':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Perfect.mp3",'B':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Falling.mp3",'C':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\My heart will go on.mp3",'D':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Main tumhaara.mp3",'E':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Hawayein.mp3"}
melodious_d={'(i)':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\A thousand years.mp3",'(ii)':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Memories.mp3",'(iii)':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Agar tum saath ho.mp3",'(iv)':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\Fix me up.mp3.mp3",'(v)':r"C:\Users\sanja\OneDrive\Desktop\SANJANA\music playlist - cs\yt1s.com - Raataan Lambiyan  Lyric VideoShershaahSidharth  KiaraTanishk BJubinAsees.mp3 "}
ans=" "
ch=input()

choice=input("press 'a' if you want to listen to the entire playlist at once , press 'b' if you want to choose your own song ")
if choice=='a':
    while ans!=2:
        ch=int(input("Please choose from the following [1or 2 or 3] -"))
        if ch==1:
            
            print("\n")
            print("                     ***                        ")
            print("\n")
            print("\t|  yOuR   PlAyLiSt  |")
            print("\n")
            print("The playlist you have chosen is Happy Music.\n\n This playlist gives one immense peasure and satisfaction/n.Happiness is a feeling of pleasure and positivity.When someone feels good,proud,excited,relieved or satisfied about \n something, that person is said to be HAPPY. We have chosen a few songs that we believe will make you happy and \n uplift your mood!")
            print("\n\n")
            print("-"*80)
            print("a.Happy - by Pharrell Williams")
            print("-"*80)
            print("b. All Izz Well - from 3 Idiots")
            print("-"*80)
            print("c. Butter - by BTS")
            print("-"*80)
            print("d. Sooraj ki baahon mein - from Zindagi na milegi dobara")
            print("-"*80)
            print("e. Dynamite - by BTS")
            print("-"*80)
            print("\n")
            shuffle=input("do you want to shuffle the playlist?(yes/no)")
            if shuffle=="yes":
                random.shuffle(happy_list)
            for song in happy_list:
                    playsound(song)
            repeat=input("Do you wish to repeat the playlist?(yes/no)")
            if repeat=="yes":
                for song in happy_list:
                    playsound(song)
            break
        
        elif ch==2:
            print("\t|  yOuR   PlAyLiSt  |")
            print("\n")
            print("Soft music helps a person relax and also helps in stress management.It helps improve one's focus ,calms one's soul\n and helps alleviate any emotional and psychological pain.This genre consists of songs which mainly focuses on\n instruments.We believe that these few songs will calm your mind and help you relax. ")
            print("\n\n")
            print("-"*80)
            print("A. Perfect - Ed Sheeran")
            print("-"*80)
            print("B. Falling - Harry Styles")
            print("-"*80)
            print("C. My Heart will go on - from Titanic")
            print("-"*80)
            print("D. Main tumhaara - from Dil Bechaara")
            print("-"*80)
            print("E. Hawayein ")
            print("-"*80)
            print("\n")
            
            shuffle=input("do you want to shuffle the playlist?(yes/no)")
            if shuffle=="yes":
                random.shuffle(soft_list)
            for song in soft_list:
                    playsound(song)
            repeat=input("Do you wish to repeat the playlist?(yes/no)")
            if repeat=="yes":
                for song in soft_list:
                    playsound(song)
            break
    
        elif ch==3:
            print("\t|  yOuR   PlAyLiSt  |")
            print("\n")
            print("The playlist you have chosen is Melodius music.Anything that makes a pleasant,tuneful sound can be called melodius.\nIt is one of the most calming and soothing type of music. Melodius music helps us relax ,improves sleep,lowers \nstress and anxiety,fostering community and a  sense of togetherness.Melodius music has the power to make us feel happy and \nat peace!Below are a few melodius songs")
            print("\n\n")
            print("-"*80)
            print("(i) Thousand years - Christina Perri")
            print("-"*80)
            print("(ii) Memories - by Maroon 5")
            print("-"*80)
            print("(iii) Agar tum saath ho")
            print("-"*80)
            print("(iv) Fix me up from movie Clouds")
            print("-"*80)
            print("(v) Raatan Lambiyan - from Shershah")
            print("-"*80)
            print("\n")
            
            shuffle=input("do you want to shuffle the playlist?(yes/no)")
             
            if shuffle=="yes":
                random.shuffle(melodious_list)
            for song in melodious_list:
                playsound(song)
            repeat=input("Do you wish to repeat the playlist?(yes/no)")
            if repeat=="yes":
                for song in melodious_list:
                    playsound(song)
            break
        else:
            print("Sorry,try again!")


elif choice=='b':
    while ans!=0:
        ch=int(input("Please choose from the following [1or 2 or 3](type 0 to exit) "))
        print("\n")
        print("                     ***                        ")
        print("\n")
        if ch==1:
            print("\t|  yOuR   PlAyLiSt  |")
            print("\n")
            print("The playlist you have chosen is Happy Music.\n\n This playlist gives one immense peasure and satisfaction/n.Happiness is a feeling of pleasure and positivity.When someone feels good,proud,excited,relieved or satisfied about \n something, that person is said to be HAPPY. We have chosen a few songs that we believe will make you happy and \n uplift your mood!")
            print("\n\n")
            print("-"*80)
            print("a.Happy - by Pharrell Williams")
            print("-"*80)
            print("b. All Izz Well - from 3 Idiots")
            print("-"*80)
            print("c. Butter - by BTS")
            print("-"*80)
            print("d. Sooraj ki baahon mein - from Zindagi na milegi dobara")
            print("-"*80)
            print("e. Dynamite - by BTS")
            print("-"*80)
            print("\n")
            print("type 'none' if you want to move on to another playlist ")
            print("\n")
            
            while ch!=0:
                chsong=input("Which song do u want to play?")
                print("\n")
            
                if chsong=='a':
                    playsound(happy_d['a'])
                elif chsong=='b':
                    playsound(happy_d['b'])
                elif chsong=='c':
                    playsound(happy_d['c'])
                elif chsong=='d':
                    playsound(happy_d['d'])
                elif chsong=='e':
                    playsound(happy_d['e'])
                elif chsong=='none':
                    break
                else:
                    print("oops...invalid")
        
        
        
        elif ch==2:
            print("\t|  yOuR   PlAyLiSt  |")
            print("\n")
            print("Soft music helps a person relax and also helps in stress management.It helps improve one's focus ,calms one's soul\n and helps alleviate any emotional and psychological pain.This genre consists of songs which mainly focuses on\n instruments.We believe that these few songs will calm your mind and help you relax. ")
            print("\n\n")
            print("-"*80)
            print("A. Perfect - Ed Sheeran")
            print("-"*80)
            print("B. Falling - Harry Styles")
            print("-"*80)
            print("C. My Heart will go on - from Titanic")
            print("-"*80)
            print("D. Main tumhaara - from Dil Bechaara")
            print("-"*80)
            print("E. Hawayein ")
            print("-"*80)
            print("\n")
            print("type 'none' if you want to move on to another playlist")
            print("\n")

            while ch!=0:
                chsongsoft=input("Which song do u want to play?")
                print("\n")
                
                if chsongsoft=='A':
                    playsound(soft_d['A'])
                elif chsongsoft=='B':
                    playsound(soft_d['B'])
                elif chsongsoft=='C':
                    playsound(soft_d['C'])
                elif chsongsoft=='D': 
                    playsound(soft_d['D'])
                elif chsongsoft=='E':
                    playsound(soft_d['E'])
                elif chsongsoft=='none':
                    break
                else:
                    print("oops...invalid")
         
    
        elif ch==3:
            print("\t|  yOuR   PlAyLiSt  |")
            print("\n")
            print("The playlist you have chosen is Melodius music.Anything that makes a pleasant,tuneful sound can be called melodius.\nIt is one of the most calming and soothing type of music. Melodius music helps us relax ,improves sleep,lowers \nstress and anxiety,fostering community and a  sense of togetherness.Melodius music has the power to make us feel happy and \nat peace!Below are a few melodius songs")
            print("\n\n")
            print("-"*80)
            print("(i) Thousand years - Christina Perri")
            print("-"*80)
            print("(ii) Memories - by Maroon 5")
            print("-"*80)
            print("(iii) Agar tum saath ho")
            print("-"*80)
            print("(iv) Fix me up from movie Clouds")
            print("-"*80)
            print("(v) Raatan Lambiyan - from Shershah")
            print("-"*80)
            print("\n")
            print("type 'none' if you want to move on to another playlist")
            print("\n")

            while ch!=0:
                chsongmel=input("Which song do u want to play?")
                print("\n")


                if chsongmel=='(i)':
                    playsound(melodious_d['(i)'])
                elif chsongmel=='(ii)':
                    playsound(melodious_d['(ii)'])
                elif chsongmel=='(iii)':
                    playsound(melodious_d['(iii)'])
                elif chsongmel=='(iv)':
                    playsound(melodious_d['(iv)'])
                elif chsongmel=='(v)':
                    playsound(melodious_d['(v)'])
                elif chsongmel=='none':
                    break
                else:
                    print("oops...invalid")
                
            
        elif ch==0:
            break

        else:
            print("Sorry,try again!")
elif choice!='a' and choice!='b' and choice!='c':
    print("Please enter either 'a', 'b' or 'c'!")
 
    
 
 
 
print("We hope you liked listening to our playlist and enjoyed it! Have a great day!")
print("-"*80)
feedback=input("Please enter your feedback...")
print("-"*80)
print("Thank you for your valuable feedback!")
print("-"*80)
print("\t\t|  tHaNk   yOu  |")


