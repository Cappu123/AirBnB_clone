# 0x00. AirBnB clone - The console
<code>Group project</code> <code>Python</code> <code>OOP</code>
By: Guillaume

## Concepts

For this project, we expect you to look at these concepts
	* [Python packages] (https://intranet.alxswe.com/concepts/66)
	* [AirBnB clone] (https://intranet.alxswe.com/concepts/74)
![hbnb](<a href="https://ibb.co/zP5rmv1"><img src="https://i.ibb.co/L9P807M/hbnb.png" alt="hbnb" border="0"></a>)

# Background Context
## Welcome to the AirBnB clone project!
Before starting, please read the <strong>AirBnB</strong> concept page.
### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:
	* put in place a parent class (called <code>BaseModel</code>)to take care of the initialization, serialization and deserialization of your future instances
	* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
	* create all classes used for AirBnB ( <code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code> ...)that inherit from <code>BaseModel</code>
	* create the first abstracted storage engine of the project: File storage.
	* create all unittests to validate all our classes and storage engine
## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc…</li>
<li>Do operations on objects (count, compute stats, etc…)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>
# Resources
<strong>Read or watch:</strong>
<ul>
<li>
<a href="https://docs.python.org/3.8/library/cmd.html">cmd module</a>
</li>
<li>
<a href="http://pymotw.com/2/cmd/">cmd module in depth</a></li>
<li>packages concept page</li>
<li>
<a href="https://docs.python.org/3.8/library/uuid.html">uuid module</a></li>
<li>
<a href="https://docs.python.org/3.8/library/datetime.html">datetime</a></li>
<li>
<a href="https://docs.python.org/3.8/library/unittest.html#module-unittest">unittest module</a></li>
<li><a href="https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/">args/kwargs</a></li>
<li><a href="https://www.pythonsheets.com/notes/python-tests.html">args/kwargs</a></li>
<li><a href="https://wiki.python.org/moin/CmdModule">cmd module wiki page</a></li>
<li><a href="htps://realpython.com/python-testing/">python unittest</a></li>
</ul>
# Learning Objectives
At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/">explain to anyone</a> <strong>without the help of Google:</strong>

## General
<ul>
<li>How to create a Python package</li>
<li>How to create a command interpreter in Python using the <code>cmd</code> module</li>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>How to manage <code>datetime</code></li>
<li>What is an UUID</li>
<li>What is <code>\*args</code> and how to use it</li>
<li>What is <code>\*\*kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
