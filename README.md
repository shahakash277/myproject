# myproject
Step 1:-
    install postgres:- sudo apt-get install postgresql
    create db : sudo -u postgres psql postgres
                createdb demodb;
    set postgres password :- sudo -u postgres psql postgres
                             \password postgres
                             give password :- postgres
    
 step 2:-
     install python3 :- sudo apt-get install python3
     install pip3 :- sudo apt-get install python3
     install virtual env :- pip3 install virtualenv
     install djang0 :-sudo pip3 install Django
     install db dependancy :-sudo apt-get install python3-psycopg2
     
step 3:-
  open terminal :
    write command :
        mkdir Demo
        cd Demo
        git clone https://github.com/shahakash277/myproject.git
        cd myproject
        python3 manage.py runserver
