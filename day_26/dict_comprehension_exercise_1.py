sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list=sentence.split()
print(sentence_list)
result={item:len(item) for item in sentence_list}
print(result)