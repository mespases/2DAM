import java.time.LocalDate;
import java.util.List;
import java.util.Scanner;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.Query;
import javax.persistence.QueryHint;

public class menu {
	
	private static EntityManagerFactory emf;
	private static EntityManager em;
	private Scanner sc = new Scanner(System.in);
	
	public menu() {
		emf = Persistence.createEntityManagerFactory("L4P1_Miki_Espases");
		em = emf.createEntityManager();
		
		elegirMenu();
	}
	
	private void elegirMenu() {
		System.out.print("1)Añadir \n2) Mostrar\n>");
		int opcion = sc.nextInt();
		
		if (opcion == 1) {
			System.out.println("Insertar:");
			System.out.print("1) Pelicula \n2) Categoria \n3) Actor \n4) Rental \n5) Payment \n6) Customer \n>");
			int insertar = sc.nextInt();
			
			insertar(insertar);
			
		} else if (opcion == 2) {
			System.out.println("Mostrar:");
			System.out.print("1) Peliculas por nombre de cliente \n2) Peliculas de una categoria "
					+ "\n3) Dinero recaudado \n4) Alquileres en un periodo de tiempo "
					+ "\n5) Muestra a los actores de la ultima pelicula \n>");
			int mostrar = sc.nextInt();
			
			mostrar(mostrar);
			
		}
	}
	
	private void insertar(int opcion) {
		switch (opcion) {
			case 1:
				insertFilm();
				break;
	
			case 2:
				insertCategory();
				break;
	
			case 3:
				insertActor();
				break;
	
			case 4:
				insertRental();
				break;
	
			case 5:
				insertPayment();
				break;
	
			case 6:
				insertCustomer();
				break;
			default:
				break;
		}
	}
	
	private void mostrar(int opcion) {
		switch (opcion) {
			case 1:
				showFilmsByClientName();
				break;
	
			case 2:
				showFilmsOfCategory();
				break;
	
			case 3:
				showMoney();
				break;
	
			case 4:
				showRentsOfDate();
				break;
	
			case 5:
				showActorsOfLastFilm();
				break;
			default:
				break;
		}

	}
	
	private void insertFilm() {
		System.out.println("Titulo: Titanic");
		String titulo = "Titanic";
		
		System.out.println("Descripcion: Barco se hunde");
		String descripcion = "Barco se hunde";
		
		System.out.println("Ano: 1999");
		int ano = 1999;
		
		System.out.println("Idioma: es");
		String idioma = "es";
		
		System.out.println("Duracion del alquiler: 19.4");
		double rental_duration = 19.4;
		
		System.out.println("Duracion: 52");
		int duracion = 52;
		
		System.out.println("Clasificacion: r");
		String rating = "r";
		
		Film f1 = new Film(titulo, descripcion, ano, idioma, rental_duration, duracion, rating);
		
		em.getTransaction().begin();
		em.persist(f1);
		em.getTransaction().commit();
		
		em.close();
	}
	
	private void insertActor() {
		System.out.println("Nombre: Pepe");
		String nombre = "Pepe";
		
		System.out.println("Apellido: Lomana");
		String apellido = "Lomana";
		
		Actor a1 = new Actor(nombre, apellido);
		
		em.getTransaction().begin();
		em.persist(a1);
		em.getTransaction().commit();
		
		em.close();
	}
	
	private void insertCategory() {
		System.out.println("Nombre: Accion");
		String nombre = "Accion";
		
		Category c1 = new Category(nombre);
		
		em.getTransaction().begin();
		em.persist(c1);
		em.getTransaction().commit();
		
		em.close();
	}
	
	private void insertCustomer() {
		System.out.println("Nombre: Manuel");
		String nombre = "Manuel";
		
		System.out.println("Apellido: Duan");
		String apellido = "Duan";
		
		System.out.println("Email: mduan@gmail.com");
		String email = "mduan@gmail.com";
		
		System.out.println("Active: true");
		boolean active = true;
		
		System.out.println("Año: 2000");
		int ano = 2000;
		
		System.out.println("Mes: 07");
		int mes = 07;
		
		System.out.println("Dia: 15");
		int dia = 15;
		
		Customer c1 = new Customer(nombre, apellido, email, LocalDate.of(ano, mes, dia), active);
		
		em.getTransaction().begin();
		em.persist(c1);
		em.getTransaction().commit();
		
		em.close();
	}
	
	private void insertPayment() {
		System.out.println("Amount: 15");
		int amount = 15;
		
		System.out.println("Año: 2000");
		int ano = 2000;
		
		System.out.println("Mes: 07");
		int mes = 07;
		
		System.out.println("Dia: 15");
		int dia = 15;
		
		Payment p1 = new Payment(amount, LocalDate.of(ano, mes, dia));
		
		em.getTransaction().begin();
		em.persist(p1);
		em.getTransaction().commit();
		
		em.close();
	}
	
	private void insertRental() {
		System.out.println("Año: 2000");
		int ano = 2000;
		
		System.out.println("Mes: 07");
		int mes = 07;
		
		System.out.println("Dia: 15");
		int dia = 15;
		
		Rental r1 = new Rental(LocalDate.of(ano, mes, dia));
		
		em.getTransaction().begin();
		em.persist(r1);
		em.getTransaction().commit();
		
		em.close();
	}
	
	private void showFilmsByClientName() {
		Query qry = em.createNativeQuery("select A.title from film as A inner join customer as B on A.id = B.cod_rental");
	
		List<Object[]> results = qry.getResultList();
		
//		@SuppressWarnings("unchecked")
//		List<Film> lc = qry.getResultList();
//		for (Film f : lc) {
//			System.out.println(f.toString());
//		}
	}
	
	private void showFilmsOfCategory() {
		Query qry = em.createQuery("FROM Actor");
		@SuppressWarnings("unchecked")
		List<Actor> lc = qry.getResultList();
		for (Actor c : lc) {
			System.out.println(c.toString());
		}
	}
	
	private void showMoney() {
		Query qry = em.createQuery("FROM Payment");
		@SuppressWarnings("unchecked")
		List<Payment> lc = qry.getResultList();
		for (Payment c : lc) {
			System.out.println(c.toString());
		}
	}
	
	private void showRentsOfDate() {
		
	}
	
	private void showActorsOfLastFilm() {
		
	}
	
	public static void main(String[] args) {
		menu m = new menu();
	}
}
