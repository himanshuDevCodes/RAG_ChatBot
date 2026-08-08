from rag.retriever import retrieve_context

docs = retrieve_context(
    "tell me the skills from the resume"
)



print("----------------------")

print(docs)