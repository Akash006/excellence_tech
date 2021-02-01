Usgae for Que 1:
          usage: question1.py [-h] (--list LIST [LIST ...] | --random RANDOM)

          Sum of list of numbers

          optional arguments:
            -h, --help            show this help message and exit
            --list LIST [LIST ...], -l LIST [LIST ...]
                                  Enter numbers for a list eg: 1 2 3 4
            --random RANDOM, -r RANDOM
                                  Give the list length and numbers will be picked randomly eg: 5
                            
     EX 1: python3 question1.py --list 10 20 30 40 50
     EX 2: python3 question1.py --random 8
     
Usage for Que 2:
    python3 question2.py
    
Usgae for Que 3:
    python question3.py
    
Usgae for Que 4:
    1. Install requirements from requirement.txt file
    2. run the uvicorn server:
        $ uvicorn main:app --reload --host 0.0.0.0
    3. Goto browser enter the machine ip and try and hit the api
        http://127.0.0.1/docs
        
        NOTE: I've used FastAPI so we will get docs inbuild.

Issue:
  1. Getting issue while updating the address using the API. Working on it will resolve soon.
