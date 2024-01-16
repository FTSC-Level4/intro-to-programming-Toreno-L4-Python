cats = {"kind" : "Cat", "owner" : "Shaun", "definition" : "A four legged feline that is known for its love of fish and sleep."}
dogs = {"kind" : "Dog", "owner" : "Patrick", "definition" : "A four legged canine that is known by the majority as 'Man's best friend' because of it's loyalty and companionship."}
birds = {"kind" : "Bird", "owner" : "Annie", "definition" : "A feathery animal that soars through the skies with its unique and vibrant colors of its feathers depending on the speices."}
fishes = {"kind" : "fish", "owner" : "Jessie", "definition" : "An aquatic animal that lives and swims underwater with its fins."}

pets =  [cats, dogs, birds, fishes]

for pet in pets:
    kind = pet["kind"]
    owner = pet["owner"]
    definition = pet["definition"]
    print(f"{owner} owns a pet {kind}.\n{definition}\n")