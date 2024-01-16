sentences = {
    "Mississippi River" : "It is the longest river in North America.",
    "Amazon River" : "It is the second longest river in the world.",
    "Yangtze River" : "It is the longest river in Asia."
}

rivers = {
    "Mississippi River" : "United States",
    "Amazon River" : "Brazil",
    "Yangtze River" : "China"
}

for key, value in rivers.items():
    sentence = sentences[key]
    print(f"Country of origin: {value}\n{key}: {sentence}\n")