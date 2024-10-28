def pos_neg_tally(review, pos_words, neg_words): #define function that tallies positive and negative words for Task 2
    pos_count = 0 #initialize the positive word tally
    neg_count = 0 #initialize the negative word tally

    for current_pos_word in pos_words: #iterate the positive words
        pos_count += 1 if review.lower().find(current_pos_word) != -1 else 0 #increment the tally if the positive word can be found in the review
        
    for current_neg_word in neg_words: #iterate the negative words list
        neg_count += 1 if review.lower().find(current_neg_word) != -1 else 0 #increment the tally if the negative word can be found in the review
    
    return [pos_count, neg_count] #return list of tallies

 #Task 1:   
reviews = [ 
    "This product is really good. I'm impressed with its quality.", 
    "The performance of this product is excellent. Highly recommended!", 
    "I had a bad experience with this product. It didn't meet my expectations.", 
    "Poor quality product. Wouldn't recommend it to anyone.", 
    "The product was average. Nothing extraordinary about it." 
    ] # list of reviews to process
important_keywords = ["good", "excellent", "bad", "poor", "average"] #list of important keywords

for review in reviews: #iterate through the reviews
    for current_keyword in important_keywords: #iterate the keyword list
        if review.lower().find(current_keyword) != -1: #check that the current keyword from the list can be found in the list
            index = review.lower().find(current_keyword) #index of beginning of keyword in the review
            end_index = index + len(current_keyword) #find and store the index for the end of the keyword in the review
            highighted_review = review[:index] + current_keyword.upper() + review[end_index:] #store the highlighted review by slicing and using upper() to hightlight keyword
        else: #current word is not a keyword
            continue #continue iterating the through the review
        
    print(highighted_review) #print the highlighted review
    print("\n") #print empty line to make next task easier to diffentiate

#Task 2:
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] #list of positive words
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"] #list of negative words 

for review in reviews: #iterate throught the reviews
    tallies = pos_neg_tally(review, positive_words, negative_words) #store the tallies from the tallying function
    print(f"Positive Words: {tallies[0]}\tNegative Words: {tallies[1]}") #print the tallies of the positive and negative words
    print("\n") #print empty line to make next task easier to diffentiate

#Task 3:
summaries = [] #list to hold the summaries

for review in reviews: #iterate through the reviews
    if review[29].isspace() or review[30].isspace() and review[29].isalpha(): #verify that the summary slice will be at/after the end of a word
        summary = review[:30] + "..." #slice the summary from the review and add the '...' to the end
        summaries.append(summary) #add summary to list
    else: #summary does not end at end of word or space
        i = 28 #set character index for finding end of word to the 29th index
        while True: #iterate through the review by character
            if review[i].isalpha() or review[i] == "'": #test if current character is in a word
                i -= 1 #decrement the index for next iteration
            else: #end of word found
                summary = review[:i + 1] + "..." #slice the summary from the review add the '...' to the end of the summary
                summaries.append(summary) #add the summary to the list
                break #stop the loop

for summary in summaries: #print summaries by iterating the list of summaries
    print(summary)

                        
                   

