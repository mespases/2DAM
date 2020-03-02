import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name = "Rental")
public class Rental {
	
	@Id
	@Column(name = "id")
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int rental_id;
	
	@Column(name = "rental_date")
	private LocalDate rental_date;
	
	@OneToMany(mappedBy = "rental", cascade = CascadeType.ALL)
	private List<Customer> customer = new ArrayList<Customer>();
	
	@OneToOne(cascade = {CascadeType.ALL})
	@JoinColumn(name = "film_id")
	private Film film_id;
	
	@OneToOne(cascade = {CascadeType.ALL})
	@JoinColumn(name = "cod_payment")
	private Payment payment_id;
	
	public Rental() {
	
	}

	public Rental(LocalDate rental_date) {
		this.rental_date = rental_date;
	}

	public int getRental_id() {
		return rental_id;
	}

	public void setRental_id(int rental_id) {
		this.rental_id = rental_id;
	}

	public LocalDate getRental_date() {
		return rental_date;
	}

	public void setRental_date(LocalDate rental_date) {
		this.rental_date = rental_date;
	}

	public List<Customer> getCustomer() {
		return customer;
	}

	public void setCustomer(List<Customer> customer) {
		this.customer = customer;
	}

	public Film getFilm_id() {
		return film_id;
	}

	public void setFilm_id(Film film_id) {
		this.film_id = film_id;
	}

	public Payment getPayment_id() {
		return payment_id;
	}

	public void setPayment_id(Payment payment_id) {
		this.payment_id = payment_id;
	}

	@Override
	public String toString() {
		return "Rental [rental_id=" + rental_id + ", rental_date=" + rental_date + ", customer=" + customer
				+ ", film_id=" + film_id + ", payment_id=" + payment_id + "]";
	}
	
}
