import os

# each website you crawl is a separate project(folder)
# Creating a New Project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory: "+directory)
        os.makedirs(directory)

#Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue=project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#create a new file
def write_file(path, data):
    f=open(path, 'w')
    f.write(data)
    f.close()
# create_project_dir('Wikipedia')

create_data_files('Wikipedia', 'http://www.python.org')

# add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data+'\n')

