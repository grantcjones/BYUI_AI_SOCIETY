#--------------------------------------------------------------------------------------------------------------
#?    Dependancies + Globals
#--------------------------------------------------------------------------------------------------------------

import json                             # For context demonstration. This isn't important for AI.
import ollama
MODEL = "llama3.2:3B"                   # The model we'll be using.

from simplify import clear, wait       # Not important either. This just clears the terminal.

#--------------------------------------------------------------------------------------------------------------
#?    Just the text. You won't see anything happen until all text has been generated.
#--------------------------------------------------------------------------------------------------------------

#* You don't need to load the model like this. It just feel a little more seamless.
print("Loading model...")
output = ollama.generate(MODEL, 'Output just the word "done"')
input("Done. (Press any button to continue)")
clear()

current_context = []

while True:
    user_input = input("> ")
    output = ollama.generate(MODEL, user_input, context=current_context)
    current_context = output.context
    print(output.response)
    print()

#--------------------------------------------------------------------------------------------------------------
#     End of
#--------------------------------------------------------------------------------------------------------------
