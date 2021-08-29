package assinments;

import ap.e1.CS1027_Asn1.ThingToWriteFile;

public class Country {
	private String name;
	private int population;
	private double area;
	private String continent;
	
	public Country(String name, int population,double area, String continent) {
		this.name=name;
		setPopulation(population);
		this.area=area;
		this.continent=continent;
	}
	
	//getter or accessor
	public String getName() {
		return name;
	}
	
	public int getPopulation() {
		return population;
	}
	
	public void setPopulation(int population) {
		this.population=population;
	}
	
	//setter or mutator
	public void setName(String name) {
		this.name=name;
	}

	public double getArea() {
		return area;
	}
	
	public String getContinent() {
		return continent;
	}
	
	public double getPopulationDensity() {
		return getPopulation()/getArea();
	}
	
	public void writeToFile(ThingToWriteFile writeFile) {
		String line=getName()+","+getContinent()+","+getPopulationDensity();
		writeFile.writeLine(line);
	}
	
	public void printCountryDetails() {
		System.out.println(getName()+" is located in "+getContinent()+" has a population of " +getPopulation()+" an area of "+ getArea()+" and has a population density of "+getPopulationDensity());
	}
	
	@Override
	public String toString() {
		return getName()+"in"+getContinent();
	}
	public static void main(String[] args) {
		Country c=new Country("China",10000,100,"Asian");
		c.printCountryDetails();
		ThingToWriteFile writeFile=new ThingToWriteFile("AP_project_file.txt");
		c.writeToFile(writeFile);
		writeFile.close();
	}
}

