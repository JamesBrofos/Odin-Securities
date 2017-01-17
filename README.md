# Odin-Securities 1.0

A master database of securities data for use with the Odin algorithmic trading platform. The database includes information on historical stock prices, on corporate actions, and includes dividend and stock-split adjusted prices and volumes.

This software is provided under the MIT license.

## Setup & Installation

It is recommended that you read all of these instructions before beginning to install the Odin Securities database. Please ensure that the Odin's `requirements.txt` file has been installed.

### Postgres

You will first need to install Postgres. Instructions on installing Postgres can be found on the [official site](https://www.postgresql.org/). From there, you will need to create a database called `securities_master` and a user called `securities`. This can be achieved by the commands:

```
CREATE DATABASE securities_master;
CREATE USER securities;
```

To allow Python to interface with Postgres, the execute the following three commands to install packages.

```
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
```

To initialize the tables in the Odin Securities database, navigate to the `odin_securities` directory and execute `make`. This will instruct Postgres to construct a database in its default configuration. In the event that you need to start over from scratch, simply execute `make` again (if the command appears to hang, execute `make restart` and try again).


### Data Vendors

Odin leverages both Yahoo! Finance and Quandl to provide price and volume data. To leverage Quandl as a data vendor, you will require a Quandl API key. This can be obtained by signing up at their website: [Quandl.com](https://www.quandl.com/). With this in hand, edit the file `./odin_securities/vendors/quandl/quandl_init.py` to specify your particular API key. Please ensure that this is done before you install Odin Securities itself; if you already installed Odin Securities, you will have to reinstall it.


### Installing Odin Securities and Building the Database

To install Odin Securities itself, execute the command:

```
python3 setup.py install
```

Installation, however, is not as important as constructing the database itself. For this purpose, refer to the file `./constructor/constructor.py`, which will both attempt to build the database from scratch and keep it updated with the latest price data. To build or update Odin Securities, navigate into the `constructor` directory and run:

```
python3 constructor.py
```

**Though this command takes a very long time to execute.** Therefore, it is recommended instead to build a smaller version of the database with Alphabet's, Facebook, and Amazon's stock prices with the command:

```
python3 constructor.py GOOG FB AMZN
```

