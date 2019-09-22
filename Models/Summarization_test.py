import gensim 
from gensim.summarization.summarizer import summarize 


text = "HPE OneView Advanced licenses include three years of 24x7 Technical Support and Updates (TS&U) for global support of your product.Annual 9x5 support is optionally available for HPE OneView Standard for an additional fee. HPE also offers uplifted support services for additional fees: Proactive Care, Proactive Care Advanced, and Datacenter Care, along with extended terms of 4 and 5 years.HPE Startup Installation and Configuration Services and HPE Installation and Migration Services are additionally available. HPE classes are also offered to make you more effective at work. Further technical consulting is available upon request. For more info, see hpe.com/info/services."


print(summarize(text))