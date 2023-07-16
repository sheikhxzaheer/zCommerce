# zCommerce v1.2.6
<br>
<img
    src="https://images.unsplash.com/photo-1688580401123-5430148e0d7a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80">

<h1>Ecommerce Website</h1>
<br>
<p>Welcome to the documentation of the Ecommerce Website. This project is built using Django, Python, JavaScript, HTML,
    CSS, Bootstrap, jQuery, Django REST Framework, and PostgreSQL.</p>
<br>

<h2>Table of Contents</h2>
<ol>
    <li><a href="#">Introduction</a></li>
    <li><a href="#">Features</a></li>
    <li><a href="#">Installation</a></li>
    <li><a href="#">Configuration</a></li>
    <li><a href="#">Usage</a></li>
    <li><a href="#">Contributing</a></li>
    <li><a href="#">License</a></li>
</ol>
<br>
<h2>Table of Contents</h2>
<br>
<p>The Ecommerce Website is a web application designed for selling products online. It provides a user-friendly
    interface for customers to browse and purchase items, as well as an administrative interface for managing products,
    orders, and users. The website utilizes various technologies to ensure a smooth and efficient shopping experience.
</p>
<br>
<h2>Features</h2>
<br>
<ul>
    <li>User authentication: Users can create accounts, log in, and manage their profiles.</li>
    <li>Product management: Admins can add, edit, and delete products.</li>
    <li>Cart functionality: Users can add items to their cart and proceed to checkout.</li>
    <li>Order management: Admins can view and process orders.</li>
    <li>Search and filtering: Users can search for products and filter results based on various criteria.</li>
    <li>Responsive design: The website is optimized for different screen sizes and devices.</li>
    <li>API endpoints: The Django REST Framework is used to provide API endpoints for external integrations.</li>
</ul>

<br>
<h2>Installation</h2>
<br>
<p>To install and set up the Ecommerce Website, follow these steps:</p>

<br>
1. Clone the repository:
  
```powershell 
git clone https://github.com/sheikhxzaheer/zCommerce.git
```

2. Navigate to the project directory:

    
```powershell 
cd ecommerce-website
```

3. Create a virtual environment:
    
```powershell 
python3 -m venv venv
```

4. Activate the virtual environment:

```powershell 
source venv/bin/activate
```

5. Install the required dependencies:

    
```powershell 
pip install -r requirements.txt
```

<br>
<h2>Configuration</h2>
<br>
<p>Before running the website, you need to configure the database settings. Follow these steps:</p>

<br>

1. Open the `ecommerce/settings.py` file.

2. Locate the `DATABASES` section and update the database settings according to your PostgreSQL configuration.

``` Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_host',
        'PORT': 'your_port',
    }
}
```

3. Save the changes.

<h2>Usage</h2>
To run the Ecommerce Website locally, execute the following command:

``` powershell
python manage.py runserver
```

Open your web browser and navigate to `http://localhost:8000` to access the website.

<h2>Contributing</h2>

Contributions to this project are welcome. To contribute, follow these steps:

<br>
1. Fork the repository.
2. Create a new branch:

``` powershell
git checkout -b my-feature
```

3. Make your changes and commit them:

``` powershell
git commit -m "Add my feature"
```

4. Push to the branch:

``` powershell
git push origin my-feature
```

5. Create a pull request detailing your changes.

<h2>License</h2>

This project is licensed under the MIT License. Feel free to modify and use the code according to your needs.

<<<<<<< HEAD
Please note that this readme file is written in HTML markup language to be used directly on your README.md file.
=======
Please note that this readme file is written in HTML markup language to be used directly on your README.md file.
>>>>>>> 16bb68dc83d4c4b9dcee0b1af0e9b07e91318759
