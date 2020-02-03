all:
	python3 request_receiver_class.py
tests: server_repository_test server_log_repository_test executor_test info_sender_test request_receiver_test

server_repository_test:
	python3 -m unittest server_repository_test.py
server_log_repository_test:
	python3 -m unittest server_log_repository_test.py 
executor_test:
	python3 -m unittest executor_test.py 
info_sender_test:
	python3 -m unittest info_sender_test.py 
request_receiver_test:
	python3 -m unittest request_receiver_test.py
