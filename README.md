# StarterPack
A pack of files and folders that gives you everything you need to get Apitax up and running. Use this as a starting point to integrate Apitax into your application or build your own application around Apitax.

StarterPack Benefits and Features:
* A complete set of working files to bring up Apitax with a single command
* Integrates Apitax/Core, Apitax/Drivers, Apitax/Scripts, and Apitax/CLI out of the box to give you a great experience
* Provides options to launch Apitax/Dashboard as well
* Completely customizable as if you were trying to use the raw Apitax code yourself
* Every service launches in Docker in one swift motion

##### Notes:
* StarterPack utilizes Pip and Docker to build the application. For this reason, an internet connection is required on the machine you use to build these images.

## Launching
`docker-compose up --build`
* `allow-cors` in config should be set to false unless you are using this application locally, for tests, or for development
