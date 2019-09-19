## Smart City Dynamic Wagon Application Model - Object Diagram

The Dynamic Wagon Application Simulation is intended to be an discrete event simulation. At each timestep, the system will create a random number of passangers that will be added to the platform, awaiting transportation. The range of the random number will be depending on the type of time. There are three possible types:
* Normal: The random number will be within normal limits
* Rushhour: A high amount of passengers will be added
* Quiet: A smaller number then normal will be added

The platform will then send a request for a train, transmitting the current amount of passengers waiting. The train will be initialized accordingly and pick up passengers on the next timestep.

The system's output is the amount of people waiting for transportation / the wait time. A good system will have only few passangers waiting with wait times not longer then a certain amout of timesteps. Furthermore, the train capacity should not be too high, as empty trains will produce higher costs. My intention is to develop a system that will provide a good throughput and also anticipate the amount of passengers that may enter the system on the next timestep, considering the type of time.
