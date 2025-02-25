            # DAY 2 (PYTHON)
# User se input lena
# input() function se user se ek sentence liya ja raha hai.
# .strip() ka matlab hai shuru aur end ke extra spaces hata dena.
user_input = input("Write down your sentence:").strip()

# Sentence mein words to count karna
# split() function sentence ke words ka list bana deta hai.
# len() function us list ke total elements count karta hai.
word_count = len(user_input.split())

# Words ko reverse order mein arrange krna hai
# split() se sentence ko words ke list mein convert kiya.
# [::-1] ka matlab hai list ko reverse order mein karna.
# ' '.join(...) ka matlab hai list ke words ko space
reversed_words = ' '.join(user_input.split()[::-1])

# Count aur reversed words ko print karna
# f"..." ka matlab hai formatted string, jisme {} ke andar variables ko print kar sakte hain.
# Pehle word count print hoga, phir reverse sentence print hoga
print(f"Your sentence has total {word_count} words.")
print("Your message in reverse order:")
print(reversed_words)