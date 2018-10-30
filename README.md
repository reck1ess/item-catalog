# Item Catalog

The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.

## Requirements

> **Note: If you already have a vagrant machine installed from previous Udacity courses skip to the 'Fetch the Source Code and VM Configuration' section**

### Git

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On `Windows`, Git will provide you with a Unix-style terminal and shell (Git Bash).

On `Mac` or `Linux` systems you can use the regular terminal program.

You will need Git to install the configuration for the VM. If you'd like to learn more about Git, [take a look at our course about Git and Github](http://www.udacity.com/course/ud775).

### VirtualBox

`VirtualBox` is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads) Install the _platform package_ for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

> **Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

### Vagrant

`Vagrant` is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

> **Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Fetch the Source Code and VM Configuration

> **Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.
> **Other systems:** Use your favorite terminal program.

From the terminal, run:

```bash
git clone https://github.com/udacity/fullstack-nanodegree-vm
```

This will give you a directory named **vagrant** complete with the source code for the flask application.

## Run the virtual machine!

Using the terminal, change directory to vagrant

```bash
cd vagrant
```

And then,

```bash
vagrant up
```

to launch your virtual machine.

## Running the Item Catalog App

Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt. To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.

Now that you have Vagrant up and running type **vagrant ssh** to log into your VM. change to the /vagrant directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.

Type **ls** to look `catalog` directory and replace it with the contents of this respository

-   To install some libraries:

```bash
pip install -r requirements.txt
```

-   To initialize the database:

```bash
python database_setup.py
```

-   To populate the database with catalog items:

```bash
python seed.py
```

-   To run the Flask web server:

```bash
python application.py
```

Visit **http://localhost:5000** to view the catalog item app!

You should be able to view many catalog items, and after login you can edit, delete items which you have made.

## JSON Endpoints

**The following endpoints are accesible:**

#### Catalog JSON

```
/catalog/JSON
```

> Displays the whole catalog. Categories and all items.

#### Category JSON

```
/catalog/<int:catalog_id>/JSON
/catalog/<int:catalog_id>/items/JSON
```

> Displays items for a specific category

#### Category Item JSON

```
/catalog/<int:catalog_id>/<path:item_name>/JSON
```

> Displays a specific category item.
