from assistant import initialize_assistant, ask_question

folder_path = input("Enter Research Papers Folder Path: ")

retriever = initialize_assistant(folder_path)

print("\n========================================")
print(" Research Paper Assistant")
print("Type 'exit' to quit")
print("========================================\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("\nThank you for using Research Paper Assistant!")
        break

    answer, sources = ask_question(retriever, question)

    print("\n Answer:\n")
    print(answer)

    print("\n Sources:")

    for source in sources:
        print("-", source)

    print("\n" + "=" * 50 + "\n")