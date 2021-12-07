from python 
user root
env dataset=/dataset/
env db_user=""
env db_pass=""
env db_address=""
env db = ""
workdir /apps/bin
run pip install pandas && pip install numpy 
run pip install  sklearn 
#run pip install  matplotlib 
#run pip install  seaborn as sb 
run pip install statsmodels
run pip install flask 
run pip install mysql-connector-python
add process.py process.py
add api.py api.py
cmd  python api.py
