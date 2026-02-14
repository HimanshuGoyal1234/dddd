def find_answer(input_file, user_input):
    with open(input_file, 'r',encoding="utf-8") as file:
        lines = file.readlines()
    qa_dict = {}
    for line in lines:
        if ':' in line:
            question, answer = line.split(':', 1)
            qa_dict[question.strip()] = answer.strip()
    best_match = ""
    for question in qa_dict:
        if question.startswith(user_input) and len(question) > len(best_match):
            best_match = question
    if best_match:
        print(f"Question: {best_match}")
        print(f"Answer: {qa_dict[best_match]}")
input_file = 'G:\\MYJARVIS\\information_of_you\\data.txt'
for i in range(199):
    user_input = input()
    find_answer(input_file, user_input)
