transcript = " I would like to thank President Joe Biden for convening this Summit. It is a welcome signal of US leadership and commitment to a multilateral climate solution, underlined by the US rejoining the Paris Agreement. Although Singapore is a small island state, we will contribute our share to the climate agenda. Singapore was among the first 20 countries to submit our long-term strategy to the UNFCCC. This year we launched the Singapore Green Plan 2030, our roadmap towards sustainable development and net zero emissions. Our strategy goes beyond meeting emission caps or implementing our carbon tax. To overcome our small size and lack of resources, and achieve our emission reduction goals, Singapore must also innovate and use technology extensively. For instance, we have very limited renewable energy options. Nevertheless, we plan to quadruple solar energy production by 2025. We are opening one of the world’s largest floating solar energy systems, which will offset 33,000 tonnes of carbon dioxide (CO2) annually. Another major concern for our compact and dense city is rising urban temperatures. To moderate this, we are using computer modelling for more climate-responsive urban design, experimenting with special cooling paint on buildings, and planting one million more trees. As a financial hub, Singapore can help the global push for sustainability through green finance, fintech and capability building. We have launched a US$2 billion Green Investments Programme. This will support the development of carbon trading and services, sustainability consultancies and environmental risk management. One promising area is emissions verification, including using new technology to measure the carbon footprints and monitor abatement commitments of businesses. Singapore is happy to share our experience in all these areas. We have incorporated climate and sustainability in the Singapore-US Third Country Training Programme. And as country coordinator for ASEAN-US energy cooperation, we will work closely with the US to support our region’s clean energy transition. We look forward to working with the US and all countries to build a sustainable future. Thank you."

# 1. count total number of words in the transcript using string methods like split() and built-in methods like len()

# split the transcript into words
words = transcript.split()

# count the number of words
total_words = len(words)

print("Total number of words:", total_words)


# 2. find the most common word in the transcript; use a dict

# initialize an empty dictionary to store word counts
word_count = {}

# loop through each word in the list
for word in words:
    # convert the word to lower case to make the count case insensitive
    word = word.lower()
    # if the word is already in the dictionary, increment its count
    if word in word_count:
        word_count[word] += 1
    # if the word is not in the dictionary, add it with a count of 1
    else:
        word_count[word] = 1

# find the word with the highest count
most_common_word = max(word_count, key=word_count.get)
most_common_count = word_count[most_common_word]

print("Most common word:", most_common_word)
print("Count of most common word:", most_common_count)