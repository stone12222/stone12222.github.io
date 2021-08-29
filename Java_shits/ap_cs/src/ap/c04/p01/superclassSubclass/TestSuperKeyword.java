package ap.c04.p01.superclassSubclass;

public class TestSuperKeyword {

}

// Goat is-A animal
class Dog1 extends Animal {
	public boolean isVegetarian() {
		return super.isVegetarian();
	};
}
