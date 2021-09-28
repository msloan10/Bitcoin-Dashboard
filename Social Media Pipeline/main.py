from Social_Media_Pipeline import Social_Media_Text_Pipeline


Twitter_pipeline = Social_Media_Text_Pipeline(social_platform='Twitter', topics = ["Bitcoin"])
pop = Twitter_pipeline.Extract(dataFlow = "batch", result_type = 'popular', count = 82)

#SOME TIMES TWEEPY DOES NOT RETURN THE EXPECTED NUM OF ROWS FOR POP TWEETS 
rowsLeft = 82 - len(pop)
complete_data = []
if (rowsLeft >= 41):
    complete_data = Twitter_pipeline.Extract(dataFlow = "batch", result_type = 'recent', count = rowsLeft) + pop
else: 
    for i in range(41):
        complete_data[i] = pop[i]

    complete_data += Twitter_pipeline.Extract(dataFlow = "batch", result_type = 'recent', count = 41)


Twitter_pipeline.Load(data = 4)

