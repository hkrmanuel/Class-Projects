

def eval_loop():
    while True:
        user_input= input("Enter Pyhton Expression or 'done' to exit:")
        
        
        if user_input == "done":
            print('Bye')
            break
        else:
            result = eval(user_input)
        print(result)
        
eval_loop()