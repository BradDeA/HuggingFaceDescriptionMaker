from transformers import pipeline

summarizer = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')

text = input('Prompt Text (please remove any line breaks or paragraph separations): ')

print('\n')
  
output = summarizer(text, max_length=160)

print('\n')
print(output[0]['summary_text'])
