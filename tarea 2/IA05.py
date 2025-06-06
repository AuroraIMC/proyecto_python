from transformers import pipeline 
from textblob import TextBlob
#pregunta y respuesta
nlp_qa = pipeline("question-answering")
#ingresa el texto a usar
contexto = input("Ingrese texto pequeño: ")
pregunta = "¿Cuál es la idea principal?"

respuesta_1 = nlp_qa(question=pregunta,context=contexto)
#genera resumen
nlp_generation = pipeline("text-generation")

texto_gen = nlp_generation(contexto,max_length=60, do_sample=True)
#da un sentimiento
sentimiento  = TextBlob(contexto).sentiment
#resumen abstractivo 
nlp_resumen = pipeline("summarization")
resumen = nlp_resumen(contexto, max_length=60,do_sample=True)

print(pregunta,respuesta_1)
print("Una historia basada en el texto: ",texto_gen[0]["generated_text"])
print("Un sentimiento del texto es",sentimiento)
print("Un resumen es",resumen[0]["summary_text"])
