from rag.loader import load_pdf
from rag.chunking import split_documents

docs = load_pdf("data/Himanshu_kumar_Python_AI_Resume_ATS.pdf")

chunks = split_documents(docs)

print("Total Chunks:", len(chunks))

#print(chunks)

print(chunks[0].page_content)
print(chunks[0].metadata)