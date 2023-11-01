import assemblyai as aai

# Create a Transcriber object
transcriber = aai.Transcriber()

# Transcribe the audio file
transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/Custom-Home-Builder.mp3")

# Print the transcribed text
print(f"TRANSCRIPT:\n{transcript.text}\n")

# Define our task
prompt = """
ROLE:
You are a customer service professional. You are very competent and able to extract meaningful insights from transcripts of customer calls that are submitted to you.
CONTEXT:
This is a call from someone who is inquiring at a home building company
INSTRUCTION:
Answer the following question or respond to the following command: "Provide a short summary of the phone call, and list any outstanding action items after the summary. Finally, provide the caller's contact information. Do not include a preamble."
FORMAT:
SUMMARY:
a one or two sentence summary

ACTION ITEMS:
a bulleted list of action items

CONTACT INFORMATION:
Name: Last name, first name
Phone number: The caller's phone number
""".strip()

# Get the response
r = transcript.lemur.task(prompt)

# Extract the response text and print
print(r.response.strip())

