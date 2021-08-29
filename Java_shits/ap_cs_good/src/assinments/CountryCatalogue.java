package assinments;


import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

import ap.e1.CS1027_Asn1.ThingToReadFile;

public class CountryCatalogue {
	int DEFAULT_SIZE=5;
	int NOT_FOUND=-1;
	Country[] catalogue;
	int numOfCountries=0;
	Set<String> continents;
	
	HashMap<String,String> cDict;
	/*-
country name -> continent
	 */
	
	public CountryCatalogue(String countryFile, String continentFile) {
		catalogue=new Country[DEFAULT_SIZE];
		continents=new HashSet<String>();
		cDict=new HashMap<String,String>();
		// read continent file
		ThingToReadFile read=new ThingToReadFile(continentFile);

		read.readLine();
		String line=null;
		do {
			line=read.readLine();
			String[] countryContinent=line.split(",");
			String countryName=countryContinent[0];
			String continent=countryContinent[1];
			
			continents.add(continent);
			cDict.put(countryName, continent);
		}while(!read.endOfFile());
		
		read.close();

		// read country file
		read=new ThingToReadFile("country.txt");
		read.readLine();
		do {
			line=read.readLine();
			String[] countryInfo=line.split(",");
			String name=countryInfo[0];
			int pop=Integer.parseInt(countryInfo[1]);
			double area=Double.parseDouble(countryInfo[2]);
			String continent=cDict.get(name);
			
			// create a country
			Country c=new Country(name,pop,area,continent);
			addCatalogue(c);
		} while (!read.endOfFile());		
		
	}
	
	private void addCatalogue(Country c) {
		catalogue[numOfCountries]=c;
		numOfCountries++;
		System.out.println(Arrays.toString(catalogue));
		System.out.println((numOfCountries));
		if (numOfCountries==catalogue.length) {
			expandCapacity();
		}
	}
	
	private void addCountry(Country c) {
		addCatalogue(c);
		continents.add(c.getContinent());
		cDict.put(c.getName(), c.getContinent());
	}
	private void expandCapacity() {
		Country[] newCatalogue=new Country[catalogue.length*2];
		for (int i=0; i<catalogue.length; i++) {
			newCatalogue[i]=catalogue[i];
		}
		catalogue=newCatalogue;
	}

	private Country getCountry(int index) {
		if (index>=0 && index<numOfCountries) {
			return catalogue[index];
		}
		return null;
	}
	
	public void printCountryCatalogue() {
		for (Country c: catalogue) {
			c.printCountryDetails();
		}
	}

	private void filterCountriesByContinent(String continent) {
		for (Country c: catalogue) {
			if (c!=null && c.getContinent().equals(continent)) {
				System.out.println(c);
			}
		}
	}

	public static void main(String[] args) {
		CountryCatalogue cc=new CountryCatalogue("country.txt", "continent.txt");

		System.out.println(cc.catalogue.length);
		
		cc.filterCountriesByContinent("Asia");
		
	}
	
}

