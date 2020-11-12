import wikipedia
import pageviewapi

wikipedia.set_lang("es")

query = wikipedia.summary("Silla")
route = wikipedia.page("Silla").url

print("{}\n\nBusca mas info en: {}".format(query,route))