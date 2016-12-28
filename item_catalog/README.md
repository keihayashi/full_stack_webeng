Item Catalog
===

## Description
This application provides a list of items within a variety of categories, as well as provide a user registration and authentication system.

## Usage
1. Install Vagrant and VirtualBox. Use **vagrant up** and **vagrant ssh** command to launch the vagrant VM.
2. Move to /vagrant/catalog folder. Set up database as follows.
```
$ python database_setup.py # set up sql database
```
You can add sample data to the database if you like.  
```
$ python sample_items.py # add sample datas to the database
```
3. Run the **project.py** file. Go to http://localhost:8000 and play around.
```
$ python project.py # run the app on the server
```
