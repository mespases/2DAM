
public class SP19201AU02E01_Miki_Espases {
	
	
	static class Bany {
		
		Boolean ocupado = false;
		
		synchronized public void esperar() {
			try {
				wait();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		synchronized public void salirDelBanyo() {
			notify();
		}
	}
	
	
	static class Persona extends Thread {
		
		private String nombre;
		Bany bany;
		
		public Persona(String nombre, Bany bany) {
			this.nombre = nombre;
			this.bany = bany;
		}
		
		public void esperar_turno() {
			try {
				sleep((int)Math.random()*5000+3000);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		public void run() {
			this.esperar_turno();
			System.out.println(nombre + ": entro en el bany");
			
			while(this.bany.ocupado) {
				System.out.println(this.nombre + ": estoy esperando, te falta mucho ?");
				this.bany.esperar();
			}
			
			this.bany.ocupado = true;
			System.out.println(nombre + ": estoy en el bany");
			this.esperar_turno();
			this.bany.ocupado = false;
			System.out.println(this.nombre + ": Ahora salgo");
			this.bany.salirDelBanyo();
		}
	}
	
	public static void main(String[] args) {
		try {
			Bany bany = new Bany();
			Persona Tofol = new Persona("Tofol", bany);
			Persona Biel = new Persona("Biel", bany);
			Persona Andreu = new Persona("Andreu", bany);
			Thread t = new Thread(Tofol);
			t.start();
			
			Thread b = new Thread(Biel);
			b.start();
			Thread a = new Thread(Andreu);
			a.start();

		} catch (Exception e) {
			e.printStackTrace();
		}
		
		
	}
}
