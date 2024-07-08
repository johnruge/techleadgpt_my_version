# chatgpt-retrieval
Simple script to use ChatGPT on your own files.

## Installation
Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```

Place your own data into `data/data.txt`.

## Example usage
Test reading `data/data.txt` file.
```
> python chatgpt.py "what is my dog's name"
Your dog's name is Sunny.(sepending on the information in your data.txt file)
```

Test reading `data/cat.pdf` file.(ypu can add PDF files)
```
> python chatgpt.py "what is my cat's name"
Your cat's name is Muffy. (depending on the data in your file)
```

Make sure you download all the requirements by running {pip install -r requirements.txt}
if that doesn't work, try replacing pip with pip3


