class Vehicle
{
    
    private String make;
    private String model;
    private int year;

    public Vehicle()
    {
        System.out.println("\nInside vehicle default constructor.");
        make = "My Make";
        model = "My Model";
        year = 1970;
    }

    //parameterized constructor

    public Vehicle(String make, String model, int year)
    {
        System.out.println("\nInside vehicle constructor with par");
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public String getMake()
    {
        return make;
    }

    public void setMake(String mk)
    {
        //set instance variable value to parameter value
        make= mk;
    }

    public String getModel()
    {
        return model;
    }

    public void setModel(String md)
    {
        //set instance variable value to parameter value
        model = md;
    }

    public int getYear()
    {
        return year;
    }

    public void setYear(int y)
    {
        //set instance variable value to parameter value
        year= y;
    }

    public void print()
    {
        System.out.print("Make: " + make + ", Model: " + model + ", Year: " + year);
    }
}