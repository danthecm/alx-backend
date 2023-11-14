# 0x03. Queuing System in JS

Explore Redis using the CLI
External programs talk to Redis using a TCP socket and a Redis specific protocol. This protocol is implemented in the Redis client libraries for the different programming languages. However to make hacking with Redis simpler Redis provides a command line utility that can be used to send commands to Redis. This program is called redis-cli.

The first thing to do in order to check if Redis is working properly is sending a PING command using redis-cli:

$ redis-cli ping
PONG
Running redis-cli followed by a command name and its arguments will send this command to the Redis instance running on localhost at port 6379. You can change the host and port used by redis-cli - just try the --help option to check the usage information.

Another interesting way to run redis-cli is without arguments: the program will start in interactive mode. You can type different commands and see their replies.

$ redis-cli
redis 127.0.0.1:6379> ping
PONG
redis 127.0.0.1:6379> set mykey somevalue
OK
redis 127.0.0.1:6379> get mykey
"somevalue"
At this point you are able to talk with Redis. It is the right time to pause a bit with this tutorial and start the fifteen minutes introduction to Redis data types in order to learn a few Redis commands. Otherwise if you already know a few basic Redis commands you can keep reading.

Securing Redis
By default Redis binds to all the interfaces and has no authentication at all. If you use Redis in a very controlled environment, separated from the external internet and in general from attackers, that's fine. However if an unhardened Redis is exposed to the internet, it is a big security concern. If you are not 100% sure your environment is secured properly, please check the following steps in order to make Redis more secure, which are enlisted in order of increased security.

Make sure the port Redis uses to listen for connections (by default 6379 and additionally 16379 if you run Redis in cluster mode, plus 26379 for Sentinel) is firewalled, so that it is not possible to contact Redis from the outside world.
Use a configuration file where the bind directive is set in order to guarantee that Redis listens on only the network interfaces you are using. For example only the loopback interface (127.0.0.1) if you are accessing Redis just locally from the same computer, and so forth.
Use the requirepass option in order to add an additional layer of security so that clients will require to authenticate using the AUTH command.
Use spiped or another SSL tunneling software in order to encrypt traffic between Redis servers and Redis clients if your environment requires encryption.
Note that a Redis instance exposed to the internet without any security is very simple to exploit, so make sure you understand the above and apply at least a firewall layer. After the firewall is in place, try to connect with redis-cli from an external host in order to prove yourself the instance is actually not reachable.

Use Redis from your application
Of course using Redis just from the command line interface is not enough as the goal is to use it from your application. In order to do so you need to download and install a Redis client library for your programming language. You'll find a full list of clients for different languages in this page.

Redis persistence
You can learn how Redis persistence works on this page, however what is important to understand for a quick start is that by default, if you start Redis with the default configuration, Redis will spontaneously save the dataset only from time to time (for instance after at least five minutes if you have at least 100 changes in your data), so if you want your database to persist and be reloaded after a restart make sure to call the SAVE command manually every time you want to force a data set snapshot. Otherwise make sure to shutdown the database using the SHUTDOWN command:

$ redis-cli shutdown
This way Redis will make sure to save the data on disk before quitting. Reading the persistence page is strongly suggested in order to better understand how Redis persistence works.
