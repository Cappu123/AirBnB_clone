# 0x00. AirBnB clone - The console
<code>Group project</code> <code>Python</code> <code>OOP</code><br>
By: Guillaume

<h2>Concepts</h2>

For this project, we expect you to look at these concepts
<ul><li><a href="https://intranet.alxswe.com/concepts/66">Python packages</a></li>
<li><a href="https://intranet.alxswe.com/concepts/74">AirBnB clone</a></li>
</ul>
<a href="https://ibb.co/zP5rmv1"><img src="https://i.ibb.co/L9P807M/hbnb.png" alt="hbnb" border="0"></a>
<h1>Background Context</h1>

Before starting, please read the <strong>AirBnB</strong> concept page.<br>

<h3>First step: Write a command interpreter to manage your AirBnB objects.</h3>
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what youbuild during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:<br>
<ul>
<li>put in place a parent class (called <code>BaseModel</code>)to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file<li>
<li>create all classes used for AirBnB ( <code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code> ...)that inherit from <code>BaseModel</code></li>
<li>create the first abstracted storage engine of the project: File storage.</li>
<li>create all unittests to validate all our classes and storage engine</li><br>
<h2>What’s a command interpreter?</h2>

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc…</li>
<li>Do operations on objects (count, compute stats, etc…)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>
<h1>Resources</h1>
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
<h1>Learning Objectives</h1>
At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/">explain to anyone</a> <strong>without the help of Google:</strong>

<h2>General</h2>
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

<h1>Requirements</h1>
<h2>Python Scripts</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version <code>2.8.\*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')</code></li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>
<h2>Python Unit Tests</h2>


<h2>Execution</h2>
The shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode like this:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: <code>$ echo "python3 -m unittest discover tests" | bash</code>

<a href="https://ibb.co/NTCs6Gm"><img src="https://i.ibb.co/kmBxgP9/webweb.png" alt="webweb" border="0"></a>

<h2>Tasks</h2>
<ol type=1>
<li>Be pycodestyle compliant!</li>
Write beautiful code that passes the pycodestyle checks.
<li>Unittests</li>
All your files, classes, functions must be tested with unit tests
<li>BaseModel</li>
<li>Create BaseModel from dictionary</li>
<li>Store first object</li>
<li>Console 0.0.1</li>
Write a program called console.py that contains the entry point of the command interpreter
<li>Console 0.1</li>
Update your command interpreter (console.py) to have these commands:
<ul>
<li><code>create</code>Creates a new instance of BaseModel, saves it (to the JSON file) and prints the <code>id</code></li>
<li><code>show</code>Prints the string representation of an instance based on the class name and <code>id</code></li>
<li><code>destroy</code>: Deletes an instance based on the class name and id (save the change into the JSON file).</li>
<li><code>all</code>Prints all string representation of all instances based or not on the class name.</li>
<li><code>update</code>: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).</li>
</ul>
<li>First User</li>
Write a class User that inherits from <code>BaseModel</code>
Update <code>FileStorage</code> to manage correctly serialization and deserialization of <code>User</code></li>
Update your command interpreter (<code>console.py</code>) to allow <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> used with <code>User</code>.
<li>More classes!</li>
Write all those classes that inherit from <code>BaseModel</code>:
<ul>
<li><code>State</code>(<code>models/state.py</code>)</li>
<li><code>City</code>(<code>models/city.py</code>)</li>
<li><code>Amenity</code>(<code>models/amenity.py</code>)</li>
<li><code>Place</code>(<code>models/place.py</code>)</li>
<li><code>Review</code>(<code>models/review.py</code>)</li>
</ul>
<li>Console1.0</li>
Update FileStorage to manage correctly serialization and deserialization of all our new classes: <code>Place</code>, <code>State</code>, <code>City</code>, <code>Amenity</code> and <code>Review</code>
Update your command interpreter (console.py) to allow those actions: <code>show</code>, <code>create</code>, <code>destroy</code>, <code>update</code> and <code>all</code> with all classes created previously.
</ol>
Enjoy your first console!

<strong><em>No unittests needed for the console</em></strong>
