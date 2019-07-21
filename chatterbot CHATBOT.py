
# coding: utf-8

# In[1]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from chatterbot.trainers import ChatterBotCorpusTrainer
bot = ChatBot("Edith")
bot = ChatBot(
    "My ChatterBot",
   logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ]
)


trainer = ChatterBotCorpusTrainer(bot)



#importing all the neccesary packages




# In[2]:


for files in os.listdir('C:/Users/LENOVO IDEAPAD/Downloads/chatterbot-corpus-1.2.0/chatterbot-corpus-1.2.0/chatterbot_corpus/data/english/'):
    data = ('C:/Users/LENOVO IDEAPAD/Downloads/chatterbot-corpus-1.2.0/chatterbot-corpus-1.2.0/chatterbot_corpus/data/english/' +  files)
    trainer.train(data)
    
    
    
  #training the chatbot with data  
    
    
    
    
    
    


# In[ ]:


while(1):
    t=input('YOU:')
    response = bot.get_response(t)
    if (t =='stop'):
        print('Edith: Bye , See you later .')
        break
    print('Edith:',response)
    
    
    #using a while loop to start the conversation

