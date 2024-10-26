# LLM-Chat-GUI
Hosting an LLM API on Colab (Use ngrok to create a tunnel to have a public url) and Creating a GUI to chat with the LLM Model


I created a GUI to chat with the LLM Model.
The user types a question and clicks the "Send" button. After a period(it might be a little bit long) , the QTextEdit box (chat) displays the chat history, showing both the user's question and the API's response. The user cannot type or remove anything from the chat box. Once the answer is displayed, the question isappears from the entry box, allowing the user to type another question. Clicking the "Clear Chat" button removes everything from the chat box. The length of the response for each question can be adjusted by changing the max_tokens parameter in the code.
