#######################
# MY HELPER FUNCTIONS #
#######################
'''
Reads a text file, and appends the words into a list
'''
def file_to_list(filename):

	my_file = open(filename, "r")
	content_list = my_file.readlines()
	i=0 
	while i < len(content_list):
		content_list[i] = content_list[i][:len(content_list[i])-1]
		i+=1
	return content_list

''' 
Finds the top nth negative or positive terms,
and returns them as a list
'''
def top_terms(text, filedata, n=20):

  arr = file_to_list(filedata)
  tk_text = nltk.word_tokenize(text)
  top = []
  dic_freq = {}
  for i in arr:
    dic_freq[i] = 0
  
  # removing special chars from text
  for term in tk_text:
    term = remove_special_chars(term.lower())
  
  # building the dictionary frequency
  for word in tk_text:
    if word in dic_freq:
      dic_freq[word] +=1

  # sorting dictionary
  dic_freq = dict(sorted(dic_freq.items(), key=lambda item: item[1], reverse=True))
  
  # appending the top values
  for k,v in dic_freq.items():
    if len(top) == n:
      break
    else:
      top.append(k)
  return top
