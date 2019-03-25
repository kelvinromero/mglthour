# MGLT in HOURS

This code fetches starships data from SWAPI.CO (Star Wars API), indexes to an Elastic Search Docker Container and shows a single web page, which upon, you can input an integer number representing MGLT (MegaLights) and in return, you receive a list of the ships and aside, the number of hours it would take to travel (if it where real, and made any sense at all..).

## Dependencies
- Docker version 18.06.1-ce
- Docker-compose version 1.17.1
- Docker-machine version 0.16.0,

Usually on ubuntu is just a matter of doing like so:
```bash
$ sudo apt install docker-compose
```


## How to setup
```bash
$ sudo docker-compose up
```

