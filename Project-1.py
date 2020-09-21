#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Application to find your Horoscope!!
print('''
      Pick your Zodiac Sign
      1)Capricorn, from 22/Dec to 19/Jan
      2)Aquarius, from 20/Jan to 18/Feb
      3)Pisces, from 19/Feb to 20/Mar
      4)Aries, from 21/Mar to 19/Apr
      5)Taurus, from 20/Apr to 20/May
      6)Gemini, from 21/May to 20/Jun
      7)Cancer, from 21/Jun to 22/July
      8)Leo, from 23/July to 22/Aug
      9)Virgo, from 23/Aug to 22/Sept
      10)Libra, from 23/Sept to 22/Oct
      11)Scorpio, from 23/Oct to 21/Nov
      12)Sagittarius, from 22/Nov to 21/Dec
      ''')
n=True
while n==True:
    s=int(input("enter your Zodiac sign number:"))
    if s==1:
        print("Your Zodiac Sign is Capricorn")
        print('''\nYou love the people around you unconditionally and such emotions will be more visible now than ever.
              Today, you will want to keep yourself surrounded with your loved ones, make them happy and have a good time. 
              Your honesty and sincerity will give depth to your existing relationships.''')
    elif s==2:
        print("Your Zodiac Sign is Aquarius")
        print('''\nGod helps those who help themselves. 
              You have experienced this plenty of times as your efforts have been paid off.  
              While your colleagues at work may pass negative comments at your work, your boss will not have any complains with you.
              ''')
    elif s==3:
        print("Your Zodiac Sign is Pisces")
        print('''\nYou will be able to come up trumps against the competition today. 
              You should be wary of hidden enemies, for they might be involved in slandering you. 
              It is best to reach out to others and make friends before they take it upon themselves to hinder your progress.
              ''')
    elif s==4:
        print("Your Zodiac Sign is Aries")
        print('''\nAll eyes may be on you today — for your looks, skills, Make hay while the sun shines, 
              and charge your batteries with all that attention.
              ''')
    elif s==5:
        print("Your Zodiac Sign is Taurus")
        print('''\nSpontaneity yet sincerity will be the ruling emotions of the day. 
              Keep your eyes and ears open, as trouble might be headed your way. 
              Make it a point to read the print well before you sign any legal contract today. 
              Prevention is better than cure.
              ''')
    elif s==6:
        print("Your Zodiac Sign is Gemini")
        print('''\nToday, your enthusiasm for sports and outdoor activities is palpable. 
              According to you, variety is the spice of life. You will keep on jumping from one venture to another.
              ''')
    elif s==7:
        print("Your Zodiac Sign is Cancer")
        print('''\nIt is likely that you will reach an important milestone in life today. 
              Keep in mind that your success may be a cause of envy for a few people, some of whom may want to harm you. 
              You are left with two choices: 
              either try to help them out of their troubles and miseries, or prepare for a battle.
              ''')
    elif s==8:
        print("Your Zodiac Sign is Leo")
        print('''\nToday, the only thing shining bright are your chances of spending some quality time with your near and dear ones.
              Going along these lines, how long has it been since you last did the same. 
              So, make the most of this lucky day. 
              Chances are that you shall make new friends, who might turn out to be very supportive in the future.
              ''')
    elif s==9:
        print("Your Zodiac Sign is Virgo")
        print('''\nYour management skills are immaculate. 
              Move with imagination, innovation and motivation to further your enterprise. 
              Feel free to express and exercise your sense of judgement.
              ''')
    elif s==10:
        print("Your Zodiac Sign is Libra")
        print('''\nThe whole point of being a Libran is that you always have the tendency to be two separate things put together on a pair of scales that somehow balance. 
              You'll bring to the scales the stability of being your own master and servant. 
              It's a fine balance to maintain. But only you are capable of doing that, thanks to your extremely high-power status today.
              ''')
    elif s==11:
        print("Your Zodiac Sign is Scorpio")
        print('''\nYou might have the chance to speak with new people in interesting fields, perhaps from foreign lands. 
              Your conversational abilities are at an all-time high, so you'll not only enjoy talking with everyone, but they'll enjoy talking with you. 
              Intriguing ideas and useful information could have your mind buzzing all night.
              ''')
    elif s==12:
        print("Your Zodiac Sign is Sagittarius")
        print('''\nFriends are highly valuable to you, and you shall spend much time with them cherishing their company and reliving amazing times spent together.
              ''')
    n=True if input("Would you like to try again?(Y/N)")=="Y" else False


# In[ ]:





# In[ ]:




