from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters.charachter import CharachterTextSplitter
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings 
from langchain_community.vectorstores import chroma
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser



import copy

loader_pdf = PyPDFLoader("CVNSTP.pdf")

pages_pdf = loader_pdf.load()

len(pages_pdf)

# pages_pdf_cut= copy.deepcopy(pages_pdf)
# ' '.join(pages_pdf_cut[0].page_content.split())  

# for i in pages_pdf_cut:
#     i.page_content = ' '.join(i.page_content.split())

# docx file loading

loader_docx = Docx2txtLoader("abc.docx")
pages_docx =  loader_docx.load()
pages_docx 

# for i in range(len(pages_docx)):
#     i.page_content = ' '.join(i.page_content.split())

#Chunking

char_splitter= CharachterTextSplitter(seperator = "", chunk_size = 500, chunk_overlap= 50)#by default the chunk overlap is 200
# char_splitter.split_documents(pages_docx)
pages_char_split = char_splitter.split_documnets(pages_docx)
#markdown Text splitter 
# md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on = [{"#","Course Title"},{"##","Lecture Title"}])
# pags_md_split = md_splitter.split_text(pages_docx[0].page_content )

# EMbeddings

embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
len(pages_char_split)


vectorstore=Chroma.from_documents(documents= pages_char_split ,embedding= embedding, persist_directory= "./into-to-langchain")
vectorstore_from_directory = Chroma(persist_directory= "./into-to-langchain", embedding_function = embedding )

vectorstore_from_directory.get(ids="",include=["embedding"])

added_document = Document(page_content='Alright! So… How are the techniques used in data, business intelligence, or predictive analytics applied in real life? Certainly, with the help of computers. You can basically split the relevant tools into two categories—programming languages and software. Knowing a programming language enables you to devise programs that can execute specific operations. Moreover, you can reuse these programs whenever you need to execute the same action', 
                          metadata={'Course Title': 'Introduction to Data and Data Science', 
                                    'Lecture Title': 'Programming Languages & Software Employed in Data Science - All the Tools You Need'})

vectorstore.add_documents([added_document])

question = "What programming languages do data scientists use?"

#retrieved_docs = vectorstore.similarity_search(query= question,k=3)
# retrieved_docs = vectorstore.max_marginal_relevance_search(query=question,k=3,lambda_mult=0.7,filter= "{"Lecture Title":"prgramming Language........."}")
# for i in retrieved_docs:
#     print(f"PageContent: {i.page_content}\n..........\nLecture Title:{i.metadata['Lecture Title']}\n")

#maximaum marginal relevance search(MMR) algorithm [MR = lambda * similarity(a,b)-(1-lambda)* Max(similarity(a,b))]


retriever = vectorstore.as_retriever(search_type = 'mmr', 
                                     search_kwargs = {'k':3, 
                                                      'lambda_mult':0.7})
retriever

TEMPLATE = '''
Answer the following question:
{question}

To answer the question, use only the following context:
{context}

At the end of the response, specify the name of the lecture this context is taken from in the format:
Resources: *Lecture Title*
where *Lecture Title* should be substituted with the title of all resource lectures.
'''

prompt_template = PromptTemplate.from_template(TEMPLATE)


chat = ChatOpenAI(model= 'gpt-4', 
                  seed=365,
                  max_tokens = 250)

chain = ({'context': retriever, 
         'question': RunnablePassthrough()} | prompt_template | chat | StrOutputParser())
chain.invoke(question)


