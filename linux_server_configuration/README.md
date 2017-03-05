Linux Server Configuration
===

## Description
Serve the [Item Catalog application](https://github.com/keihayashi/full_stack_webeng/tree/master/item_catalog) on Linux server. Amazon Lightsail is used for Linux server instance.  
Remote login of the root user is not allowed and key-based authentication is forced.

## Information
**IP address**  
52.3.229.101 (URL: http://52.3.229.101/)  
** SSH port **   
2200  
** Software installed **  
Apache, mod_wsgi, PostgreSQL, Flask, SqlAlchemy, sqlite 3  
** Configurations made **   
Change the SSH port to 2200. Configure UFW to only allow incoming connections for SSH, HTTP and FTP  
Create a user account *grader* and gave it SSH key pair and permission to sudo  
Change the local timezone to UTC  
Disable remote login as the root user
