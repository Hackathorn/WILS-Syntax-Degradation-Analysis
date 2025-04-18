# WILS-Syntax-Degradation-Analysis
 Exploring semantic effects of syntax degradation in LLM embeddings

This repro explores a research approach called Syntax Degradation Analysis (SDA), which degrades the syntax of LLM input text to observe its impact on semantic meaning. The change in meaning is measured by the similarity distance between the original text and its degraded version. The SDA approach has the potential to contribute meaningfully to research in Interpretable AI by revealing how language models encode and respond to degraded input.

This work started with the [Kaggle/Google 5-Day Gen-AI Intensive Course (2025Q1)](https://www.google.com/url?q=https%3A%2F%2Frsvp.withgoogle.com%2Fevents%2Fgoogle-generative-ai-intensive_2025q1), 
we explore the implications and extensions of a simple example presented in the Day-Two Explore codelab. 
To launch the capstone version:  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github.com/Hackathorn/WILS-Syntax-Degradation-Analysis/blob/main/Effects-on-Semantic-Similarity-from-Syntax-Degrade-final.ipynb)

That example used the familiar phrase:  
- *The quick brown fox jumps over the lazy dog.* (1.00)

Then, the syntax of that phrase was manually degraded step-by-step:  
- *The quick rbown fox jumps over the lazy dog.* (0.98)  
- *teh fast fox jumps over the slow woofer.* (0.94)  
- *a quick brown fox jmps over lazy dog.* (0.89)  
- *brown fox jumping over do\g* (0.84)  
- *fox > dog* (0.78)  
- *The five boxing wizards jump quickly.* (0.64)  

Ending with complete randomness:  
- *Lorem ipsum dolor sit amet, consectetur adipiscing elit.* (0.47)

A simple cosine similarity metric (values shown above) was used to measure the distance between the original phrase and each degraded version. Cosine similarity compares the angle between vectors: 1.0 means perfectly similar (aligned), while 0.0 means no similarity (orthogonal).

While this example shows a general decline in cosine similarity, the intuitive connection between syntax degradation and semantic similarity is not always obvious. For instance, why isn’t the similarity score for the final random phrase close to 0.0?

The deeper question is: How does the LLM encode meaning into its embedding vectors?
Somehow, the floating-point numbers in these vectors represent the semantics—the meaning—of each phrase. There lies the mystery.

As our capstone exploration, we examine variations on this theme: how semantic similarity is encoded in LLM embeddings. To support this, we created procedures to randomly degrade text in multiple ways, then extended the analysis across three distance metrics and thirty familiar phrases. The final section outlines future research directions and their importance to AI interpretability.

Understanding how LLMs encode knowledge—especially within their embeddings—is essential to understanding how an LLM thinks.
