from Social_Media_Pipeline import Social_Media_Text_Pipeline

#executed every 12 hours via Windows Task Manager

NUM_ROWS = 82

Twitter_pipeline = Social_Media_Text_Pipeline(social_platform='Twitter', topics = ["Bitcoin"])
pop = Twitter_pipeline.Extract(dataFlow = "batch", result_type = 'popular', count = NUM_ROWS)


rowsLeft = 82 - len(pop)
complete_data = []
if (rowsLeft >= 41):
    complete_data = Twitter_pipeline.Extract(dataFlow = "batch", result_type = 'recent', count = rowsLeft) + pop
else: 
    for i in range(41):
        complete_data[i] = pop[i]

    complete_data += Twitter_pipeline.Extract(dataFlow = "batch", result_type = 'recent', count = 41)


for row in complete_data: 
    Twitter_pipeline.Analyze(key = '', endpoint = '', row = row)


Twitter_pipeline.Load(data = complete_data)

