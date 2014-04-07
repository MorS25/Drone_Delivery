Drone Delivery System
=====================

This is my final project at Hackbright Academy, Spring 2014 class. As you may have guessed, the project idea was inspired by Amazon's press release of their intention to provide a drone delivery service. I came from the aviation industry and I love everything that flies - this is my vision of a drone delivery system. This project is intended to show the web-based aspect of the delivery system. It does not intend to include the hardware aspects, which would require much more time and resources than the allotted 4 week timeframe. However, for completeness, I have written 2 sections in this Readme that describe my ideas for the hardware and operational considerations of the delivery system.

How to run the code in this repository
======================================

1. Create a virtual environment and activate it in a terminal.
2. Run `model.py` to create the database schema. I am using PostgresSQL for the database so you need to have postgres installed    and running to run the app. My database is called `duckiestore_app`.
3. Once the database is up and running, run `seedDuckie.py` to seed the ducks table (my product table that stores my duckies    for sale).
4. With the Postgres database up and running and the ducks table seeded, the program can be run by running `foreman start`    in the terminal.

Note 1: The above instructions are for a Mac.
Note 2: The flight path will be generated only if the delivery address is within these <br/>coordinates, [37.800000, -122              .436000], [37.800000, -122.386000], [37.780000, -122.386000], [37.780000, -122.436000]. <br/>One of the sample                 addresses I used for demonstration is 198 5th Street, San Francisco, CA 94103, USA.

Overview
======

An online store has been set up to sell rubber duckies and some of the deliveries may be made by drones.  A customer may browse the products (duckies in this case), log in and place orders. If the delivery address provided by the customer is within the drone delivery area, a preferred flight path will be generated and the order will be delivered by a drone. The preferred flight path may be viewed in a 2D map or a 3D map on the website.

The Web Application
=========

The Model View Controller (MVC) software design pattern was used to build this web application. The framework is Flask with SQLAlchemy as a database toolkit, all written in Python. SQLite was used for the database during initial development but was switched to ProgresSQL in preparation for deploying onto Heroku. 

Geographic information was obtained from three APIs - [Mapbox](http://www.mapbox.com), [Google Maps](http://maps.google.com) and [Google Earth](http://earth.google.com).  

The chosen drone delivery area is downtown San Francisco. The fictitious delivery center is at the Ferry Building. A 2D map of San Francisco with all the tall buildings (those over 400 feet) identified is produced and imported through the Mapbox API. The preferred flight path, from the delivery center (the Ferry Building) to the delivery address is generated by using an A* pathfinding algorithm. The flight path will avoid all buildings over 400 feet. (Note: Drones are prohibited to fly above 400 feet, a current FAA restriction). The preferred flight path can be viewed on two html pages. The 2D path is displayed on the Mapbox map and the 3D path is displayed on Google Earth with a Google Earth plug-in. This part of the project is written in Javascript on the html pages so that it is integrated seamlessly with the webapp. The generated preferred flight path is an array of coordinates that may be changed easily into a suitable format (e.g. a Node.js program for a NodeBot) to program a delivery drone. I used the term "preferred flight path" here because, for operational reasons, the delivery drone must have the ability to override this pre-programed preferred flight path in order to avoid collision with any obstacle in its way (e.g. a tall crank, a 400 ft.+ building under construction or other flying objects).

A unit test (`testsuite.html`) was written to check all the coordinate conversion calculations used in the `SFmapping.html` page. 
Note: The calculations live in the `calculations.js` files.

Technologies used:

1. Front-end: Javascript, jQuery, Jinja2, HTML, CSS, Bootstrap
2. Back-end: Python, Flask, SQLAlchemy, PostgreSQL, SQLite.
3. GIS-related: Mapbox API, Google maps API, Google Earth API, GeoJSON.

![2D flight path](https://raw.githubusercontent.com/cathylouie/Drone_Delivery/b4ad5c2eed0587e97f9597e735ea03ff3100bc70/static/img/2DPath.png)

![3D flight path](https://raw.githubusercontent.com/cathylouie/Drone_Delivery/master/static/img/3DPath.png)

Further Improvements
============

The following areas would benefit from further improvement.

1. The A* path finding algorithm currently used requires the start point and end point to be "walkable", i.e. these cannot be obstacles. Therefore, if the delivery address is one of the high buildings that has been classified as an obstacle, the path finding algorithm will not calculate a path. This may be resolved by putting restrictions in the new customer registration form when they input their delivery address. This could also be put in an algorithm that will select one of the nodes closest to the tall buildings as the end point. 

2. Improve user experience by showing the drone delivery area up front so that customers may register a different delivery address that allows for drone delivery.

3. Add the 'Touring' feature into the 3D Google Earth page. This would allow the user to 'fly' the flight path of the drone that was generated. This can be achieved by replacing the 2D map from Mapbox to a 2D map from Google Maps. Google Maps exports coordinate information in the Keyhole Markup Language (KML) format, which is the only format Google Earth will support to enable the 'Touring' feature. 

Hardware Considerations
=============

The following criteria should be considered during the development of the drone specification. Other requirements may also emerge during the development process.

1. Size of the delivery area - This will determine flight range capability and the engine/motor output and battery requirements  
2. Payload weight -  This will also affect the engine/motor and battery selection.
3. Location system - There should be an onboard GPS system for flight navigation. 
4. Collision avoidance - The drone should have collision avoidance capability to ensure a safe flight. This may be achieved by using an array of sonar type sensors that will give a 360 degree coverage of the drone.
5. Altitude sensing - This would ensure the FAA restriction is observed.
6. High resolution camera - This will be used to realize a landing procedure that will be described in the following section.
7. Overall control system - There should be some form of programable control system to execute navigation instructions, continued monitoring of in flight conditions to maintain safe flight (e.g. collision avoidance) and execute the landing procedure (see the next section for a proposed landing procedures).

Operation Considerations
=============

There are many challenges that would affect drone delivery operations. The following are some of the issues that would need to be considered.

1. Regulatory  Requirements - The current FAA regulations do not allow for commercial use of drones. This would obviously be a very big obstacle for a drone delivery system. However, there are signs that the FAA may relax their rules. FAA regulations exist to ensure safe flight and operations of aircraft of all types and it follows that if it is possible to demonstrate safe flight and operations of a drone, it would be possible to development regulations to allow commercial use of drones.

2. One of the concerns for safe operation of a drone would be the reliability of the hardware. It obviously will not be very safe if it crashes regularly. Therefore, there should be some form of control system in place to ensure that a drone is designed and maintained to achieve an acceptable failure rate. One would have to reach agreement with the regulatory authority concerning this failure rate. The failure modes and failure effects (i.e. consequences of a failure) will also need to be discussed with the authority.

3. The route / flight path of the drone will also affect the acceptability of the failure effects. For example, it will be more acceptable for the drone to crash into an empty field instead of a busy street. Control airspace, in particular, airspace near airports and airfields will need to be avoided. This would also affect the acceptable hardware reliability as the drone will need to be more reliable if it needs to fly over heavily populated areas.  Again, one would need to reach agreement with the regulatory authority concerning routing and flight paths.

4. Security of the drone should also be considered carefully. After a drone arrives at the delivery address coordinates, there should be a way to ensure that there is a suitable landing area and that the correct customer is there to receive the delivery. The following is a vision of my landing procedure. The use of a Quick Response (QR) code for a landing pad was inspired by the numerous return shipping labels (with QR codes) I had to print out for my husband's shoes.

  4.1 Prior to despatch of the drone, a phone call, email or message (or all three communication methods) indicating that the dispatch has occurred and estimated time of arrival (ETA) will be sent to the customer.

  4.2 A QR code will be emailed to the customer, which the customer will print out to use as a landing pad.  Instructions will be provided to the customer as to the optimal placement of the QR landing pad (i.e., no power lines, trees, etc.  that may interfere with the drone's flight path).

  4.3 Shortly before the ETA, the customer will receive an email or message indicating that the drone will be arriving shortly and that the customer needs to place the QR landing pad in an appropriate location and wait for the drone to   arrive.

  4.4 Upon arrival at the delivery address coordinates, the drone will seek out the QR code landing pad with its onboard high resolution camera.  If the drone sees the correct QR code, it will complete its landing on the QR landing pad and the customer can unload the product (rubber duckies).  However, if the drone cannot detect the right QR code or cannot locate the QR code, then it will fly in a circular search pattern for 3 minutes.  After 3 minutes, if it cannot detect the QR code, then it will return to the delivery center and an email or text indicating a missed delivery will be sent to the customer.
  
  Note: Emails, messages and phone calls to the customer may be automated by integrating services provided by companies such as Twilio.com
