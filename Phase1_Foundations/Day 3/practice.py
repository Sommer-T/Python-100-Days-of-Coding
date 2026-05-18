quote = "  Every bug is a breadcrumb. Follow it.  "
day = 3
topic = "strings and formatting"

clean_quote = quote.strip()

print("String Practice Lab")
print("-" * 30)
print(f"Original quote: '{quote}'")
print(f"Clean quote: '{clean_quote}'")
print(f"Quote length after strip: {len(clean_quote)}")
print(f"Uppercase topic: {topic.upper()}")
print(f"Title case topic: {topic.title()}")
print(f"First character of quote: {clean_quote[0]}")
print(f"First 10 characters: {clean_quote[:10]}")
print(f"Last 10 characters: {clean_quote[-10:]}")
print(f"Today is Day {day}: {topic.title()}.")

challenge_sentence = f"On Day {day}, I practiced {topic} and made the lesson personal."
print(challenge_sentence)
