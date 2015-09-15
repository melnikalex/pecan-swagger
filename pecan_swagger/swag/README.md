# pecan-swagger-REST
swagger generator for pecan RestController APIs

## How to use

1. Place pecan-swagger into your installed project directory.
2. Run swag.py with 3 command-line arguments 

        python swag.py pathtocontroller name version
        e.g.
        python swag.py test_project.controllers.root.Rootcontroller test_project 1.2.3

3. Decorate any _lookup functions in your project with @methodroute. The first argument
is the parameter passed to _lookup, and the 2nd argument is the Controller to route to. Like so
        
        @methodroute('car_model', 'CarController')
        _lookup(self, primary_key, *remainder):
            car = getcar(primary_key)
                return CarController(car), remainder


4. Collect swagger from output or pipe it wherever you want!
