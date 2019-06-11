"""

Q2. Code Challenge (Connecting Hearts)


Downlaod Link: http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/Resource.zip

What influences love at first sight? (Or, at least, love in the first four minutes?) This dataset was compiled by Columbia Business School Professors Ray Fisman and Sheena Iyengar for their paper Gender Differences in Mate Selection: Evidence from a Speed Dating Experiment.

Data was gathered from participants in experimental speed dating events from 2002-2004. During the events, the attendees would have a four minute "first date" with every other participant of the opposite sex. At the end of their four minutes, participants were asked if they would like to see their date again.

They were also asked to rate their date on six attributes: Attractiveness, Sincerity, Intelligence, Fun, Ambition, and Shared Interests.

The dataset also includes questionnaire data gathered from participants at different points in the process.

These fields include: demographics, dating habits, self-perception across key attributes, beliefs on what others find valuable in a mate, and lifestyle information.

See the Key document attached for details of every column and for the survey details.


What does a person look for in a partner? (both male and female)


For example: being funny is more important for women than man in selecting a partner! Being sincere on the other hand is more important to men than women.

    What does a person think that their partner would look for in them? Do you think what a man thinks a woman wants from them matches to what women really wants in them or vice versa. TIP: If it doesn’t then it will be one sided :)

    Plot Graphs for:
            How often do they go out (not necessarily on dates)?
            In which activities are they interested?
    
    If the partner is from the same race are they more keen to go for a date?
    What are the least desirable attributes in a male partner? Does this differ for female partners?
    How important do people think attractiveness is in potential mate selection vs. its real impact?
    """
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Dating_Data.csv")



#What does a person look for in a partner? (both male and female)
gp=dataset.groupby('gender')
import operator
dict1=dict()
dict1['pf_o_att']=(gp['pf_o_att'].sum()[1])
dict1['pf_o_sin']=(gp['pf_o_sin'].sum()[1])
dict1['pf_o_int']=(gp['pf_o_int'].sum()[1])
dict1['pf_o_fun']=(gp['pf_o_fun'].sum()[1])
dict1['pf_o_amb']=(gp['pf_o_amb'].sum()[1])
dict1['pf_o_sha']=(gp['pf_o_sha'].sum()[1])

plt.bar(dict1.keys(),dict1.values())
plt.xlabel("Attributes")
plt.ylabel("Preference")
plt.xticks(dict1.keys(),rotation=90)
plt.show()
min(dict1.iteritems(), key=operator.itemgetter(1))[0]#for mens

dict2=dict()

dict2['pf_o_att']=(gp['pf_o_att'].sum()[0])
dict2['pf_o_sin']=(gp['pf_o_sin'].sum()[0])
dict2['pf_o_int']=(gp['pf_o_int'].sum()[0])
dict2['pf_o_fun']=(gp['pf_o_fun'].sum()[0])
dict2['pf_o_amb']=(gp['pf_o_amb'].sum()[0])
dict2['pf_o_sha']=(gp['pf_o_sha'].sum()[0])

plt.bar(dict2.keys(),dict2.values())
plt.xlabel("Attributes")
plt.ylabel("Preference")
plt.xticks(dict2.keys(),rotation=90)
plt.show()
max(dict2.iteritems(), key=operator.itemgetter(1))[0]#for womens

#*****************************************************************

#What does a person think that their partner would look for in them? Do you think what a man thinks a woman wants from them matches to what women really wants in them or vice versa. TIP: If it doesn’t then it will be one sided :)

dict1=dict()
dict1['attr2_1']=(gp['attr2_1'].sum()[1])
dict1['sinc2_1']=(gp['sinc2_1'].sum()[1])
dict1['intel2_1']=(gp['intel2_1'].sum()[1])
dict1['fun2_1']=(gp['fun2_1'].sum()[1])
dict1['amb2_1']=(gp['amb2_1'].sum()[1])
dict1['shar2_1']=(gp['shar2_1'].sum()[1])

plt.bar(dict1.keys(),dict1.values())
plt.xlabel("Attributes")
plt.ylabel("Preference")
plt.xticks(dict1.keys(),rotation=90)
plt.show()
max(dict1.iteritems(), key=operator.itemgetter(1))[0]#for mens


#men thinks what womens look in them is:

dict2=dict()
dict2['attr2_1']=(gp['attr2_1'].sum()[0])
dict2['sinc2_1']=(gp['sinc2_1'].sum()[0])
dict2['intel2_1']=(gp['intel2_1'].sum()[0])
dict2['fun2_1']=(gp['fun2_1'].sum()[0])
dict2['amb2_1']=(gp['amb2_1'].sum()[0])
dict2['shar2_1']=(gp['shar2_1'].sum()[0])

plt.bar(dict2.keys(),dict2.values())
plt.xlabel("Attributes")
plt.ylabel("Preference")
plt.xticks(dict2.keys(),rotation=90)
plt.show()
max(dict2.iteritems(), key=operator.itemgetter(1))[0]#for mens

#*********************************************************************

#How often do they go out (not necessarily on dates)?
            
labels=['Several times a week',
	'Twice a week',
	'Once a week',
	'Twice a month',
	'Once a month',
	'Several times a year',
	'Almost never'
]
plt.title("How often do they go out (not necessarily on dates)?")

go_out=dataset['go_out'].value_counts()
plt.bar(labels,go_out.values)
plt.xlabel("How ofter you go")
plt.ylabel("No.of peoples")
plt.xticks(labels,rotation=90)
plt.show()

#****************************************************

#In which activities are they interested?

dict1=dict()
dict1['sports']=dataset['sports'].mean()
dict1['tvsports']=dataset['tvsports'].mean()
dict1['exercise']=dataset['exercise'].mean()
dict1['dining']=dataset['dining'].mean()
dict1['museums']=dataset['museums'].mean()
dict1['art']=dataset['art'].mean()
dict1['hiking']=dataset['hiking'].mean()
dict1['gaming']=dataset['gaming'].mean()
dict1['clubbing']=dataset['clubbing'].mean()
dict1['reading']=dataset['reading'].mean()
dict1['tv']=dataset['tv'].mean()
dict1['theater']=dataset['theater'].mean()
dict1['movies']=dataset['movies'].mean()
dict1['concerts']=dataset['concerts'].mean()
dict1['music']=dataset['music'].mean()
dict1['shopping']=dataset['shopping'].mean()
dict1['yoga']=dataset['yoga'].mean()


plt.title("In which activities are they interested?")

plt.bar(dict1.keys(),dict1.values())
plt.xlabel("How ofter you go")
plt.ylabel("avg rating")
plt.xticks(dict1.keys(),rotation=90)
plt.show()

# If the partner is from the same race are they more keen to go for a date?
gp1=dataset.groupby('race')
gp1['date'].apply(lambda x :x.mode()[0])

#What are the least desirable attributes in a male partner? Does this differ for female partners?
dict2=dict()

dict2['pf_o_att']=(gp['pf_o_att'].sum()[0])
dict2['pf_o_sin']=(gp['pf_o_sin'].sum()[0])
dict2['pf_o_int']=(gp['pf_o_int'].sum()[0])
dict2['pf_o_fun']=(gp['pf_o_fun'].sum()[0])
dict2['pf_o_amb']=(gp['pf_o_amb'].sum()[0])
dict2['pf_o_sha']=(gp['pf_o_sha'].sum()[0])

min(dict2.iteritems(), key=operator.itemgetter(1))[0]#ambitious

#What are the least desirable attributes in a female partner? Does this differ for male partners?
dict1=dict()
dict1['pf_o_sin']=(gp['pf_o_sin'].sum()[1])
dict1['pf_o_int']=(gp['pf_o_int'].sum()[1])
dict1['pf_o_fun']=(gp['pf_o_fun'].sum()[1])
dict1['pf_o_amb']=(gp['pf_o_amb'].sum()[1])
dict1['pf_o_sha']=(gp['pf_o_sha'].sum()[1])
min(dict1.iteritems(), key=operator.itemgetter(1))[0]#ambitious
    

#How important do people think attractiveness is in potential mate selection vs. its real impact?
