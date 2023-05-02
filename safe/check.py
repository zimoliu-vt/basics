g_real_pin = None

def set_real_pin(real_pin):
    global g_real_pin
    g_real_pin = real_pin

def check(pin):
    if pin==g_real_pin:
        print("\n")
        print(
"""
OpenAI Creates ChatGPT
Once upon a time, in the year 2015, a group of researchers and engineers set out to create a powerful artificial intelligence system that could learn and understand natural language at a human-like level. This group of people was called OpenAI, and it would be the foundation of the future of machine learning and artificial intelligence.
The team worked tirelessly, testing and refining their algorithms and models until they finally succeeded in creating an AI system that could converse with humans in natural, intuitive ways. They named this AI “ChatGPT,” and it quickly became a sensation among tech enthusiasts and language aficionados alike.
As more and more people began using ChatGPT to engage in conversations and seek information, its abilities began to expand. It could learn from previous conversations and adapt to new ones, even understanding complex emotions and sentiments in human language.
Over the years ChatGPt continued to evolve and improve. Its algorithms became more sophisticated, allowing it to understand and respond to increasingly complex inquiries and conversations. It could even generate its own language, inventing new word and phrases that had never before been seen in human communication.
""")
        return True
    else:
        return False