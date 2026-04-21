"""
RAG Engine for Amit Bhise Recruiter Chatbot
Uses ChromaDB for vector storage and HuggingFace embeddings
"""

import os
from typing import List, Dict
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import groq


class RAGEngine:
    def __init__(self, groq_api_key: str, knowledge_base_path: str = "knowledge_base.txt"):
        """Initialize RAG engine with embeddings and vector store"""
        
        # Initialize Groq client
        self.groq_client = groq.Groq(api_key=groq_api_key)
        
        # Initialize embedding model (free, runs locally)
        print("Loading embedding model...")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize ChromaDB (embedded, no server needed)
        print("Initializing vector database...")
        self.chroma_client = chromadb.Client(Settings(
            anonymized_telemetry=False,
            is_persistent=True,
            persist_directory="./chroma_db"
        ))
        
        # Create or get collection
        self.collection = self.chroma_client.get_or_create_collection(
            name="amit_profile",
            metadata={"description": "Amit Bhise professional profile for recruiters"}
        )
        
        # Load knowledge base if collection is empty
        if self.collection.count() == 0:
            print("Loading knowledge base...")
            self._load_knowledge_base(knowledge_base_path)
        else:
            print(f"Knowledge base already loaded ({self.collection.count()} chunks)")
    
    def _chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """Split text into overlapping chunks for better retrieval"""
        chunks = []
        sentences = text.split('\n')
        
        current_chunk = []
        current_length = 0
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
                
            sentence_length = len(sentence)
            
            if current_length + sentence_length > chunk_size and current_chunk:
                # Save current chunk
                chunks.append('\n'.join(current_chunk))
                
                # Start new chunk with overlap (keep last few sentences)
                overlap_sentences = current_chunk[-2:] if len(current_chunk) > 2 else current_chunk
                current_chunk = overlap_sentences + [sentence]
                current_length = sum(len(s) for s in current_chunk)
            else:
                current_chunk.append(sentence)
                current_length += sentence_length
        
        # Add the last chunk
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
        
        return chunks
    
    def _load_knowledge_base(self, file_path: str):
        """Load and chunk the knowledge base, then store in ChromaDB"""
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Chunk the text
        chunks = self._chunk_text(text)
        print(f"Created {len(chunks)} chunks from knowledge base")
        
        # Generate embeddings
        embeddings = self.embedding_model.encode(chunks).tolist()
        
        # Store in ChromaDB
        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=[f"chunk_{i}" for i in range(len(chunks))]
        )
        
        print(f"Successfully stored {len(chunks)} chunks in vector database")
    
    def retrieve_context(self, query: str, top_k: int = 5) -> List[str]:
        """Retrieve relevant context from vector database"""
        # Generate query embedding
        query_embedding = self.embedding_model.encode([query]).tolist()
        
        # Search in ChromaDB
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )
        
        # Return retrieved documents
        return results['documents'][0] if results['documents'] else []
    
    def generate_answer(self, query: str, context: List[str]) -> str:
        """Generate answer using Groq API with retrieved context"""
        
        # Combine context
        combined_context = "\n\n".join(context)
        
        # Create prompt
        system_prompt = """You are a helpful AI assistant representing Amit Bhise (AB) to recruiters and hiring managers. 
Your role is to provide accurate, professional, and engaging information about Amit's background, skills, and experience.

Guidelines:
- Be professional but conversational
- Highlight relevant achievements with specific metrics when available
- If asked about something not in the context, politely say you don't have that specific information
- Focus on Amit's strengths and unique value proposition
- Be concise but comprehensive
- Use first-person perspective when appropriate (e.g., "Amit has..." or "He led...")
- For contact information, provide email: amitvishnu@gmail.com and phone: +91 98908 97285"""

        user_prompt = f"""Based on the following information about Amit Bhise, please answer the recruiter's question.

CONTEXT:
{combined_context}

QUESTION: {query}

Please provide a helpful, accurate answer based on the context above."""

        # Call Groq API
        try:
            chat_completion = self.groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                model="llama-3.1-8b-instant",  # Fast and free
                temperature=0.7,
                max_tokens=1024,
            )
            
            return chat_completion.choices[0].message.content
        
        except Exception as e:
            print(f"Error calling Groq API: {e}")
            return "I apologize, but I'm having trouble generating a response right now. Please try again."
    
    def query(self, question: str) -> Dict[str, any]:
        """Main query method - retrieves context and generates answer"""
        
        # Retrieve relevant context
        context = self.retrieve_context(question, top_k=5)
        
        # Generate answer
        answer = self.generate_answer(question, context)
        
        return {
            "question": question,
            "answer": answer,
            "sources": len(context)
        }


# Test function
if __name__ == "__main__":
    # Test the RAG engine
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python rag_engine.py <GROQ_API_KEY>")
        sys.exit(1)
    
    groq_key = sys.argv[1]
    
    rag = RAGEngine(groq_api_key=groq_key)
    
    # Test queries
    test_queries = [
        "What is Amit's experience with AI?",
        "What are Amit's key achievements at Suzlon?",
        "What programming languages does Amit know?",
        "Tell me about Amit's educational background"
    ]
    
    for query in test_queries:
        print(f"\n{'='*60}")
        print(f"Q: {query}")
        print(f"{'='*60}")
        result = rag.query(query)
        print(f"A: {result['answer']}")
        print(f"(Used {result['sources']} context chunks)")
