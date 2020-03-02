import java.time.LocalDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

@Entity
@Table(name = "Customer")
public class Customer {
	
	@Id
	@Column(name = "id")
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int customer_id;
	
	@Column(name = "first_name")
	private String first_name;
	
	@Column(name = "last_name")
	private String last_name;
	
	@Column(name = "email")
	private String email;
	
	@Column(name = "create_date")
	private LocalDate create_date;
	
	@Column(name = "active")
	private boolean active;
	
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "cod_rental")
	private Rental rental;
	
	public Customer() {
	
	}

	public Customer(String first_name, String last_name, String email, LocalDate create_date,
			boolean active) {
		this.first_name = first_name;
		this.last_name = last_name;
		this.email = email;
		this.create_date = create_date;
		this.active = active;
	}

	public int getCustomer_id() {
		return customer_id;
	}

	public void setCustomer_id(int customer_id) {
		this.customer_id = customer_id;
	}

	public String getFirst_name() {
		return first_name;
	}

	public void setFirst_name(String first_name) {
		this.first_name = first_name;
	}

	public String getLast_name() {
		return last_name;
	}

	public void setLast_name(String last_name) {
		this.last_name = last_name;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public LocalDate getCreate_date() {
		return create_date;
	}

	public void setCreate_date(LocalDate create_date) {
		this.create_date = create_date;
	}

	public boolean isActive() {
		return active;
	}

	public void setActive(boolean active) {
		this.active = active;
	}

	public Rental getRental() {
		return rental;
	}

	public void setRental(Rental rental) {
		this.rental = rental;
	}

	@Override
	public String toString() {
		return "Customer [customer_id=" + customer_id + ", first_name=" + first_name + ", last_name=" + last_name
				+ ", email=" + email + ", create_date=" + create_date + ", active=" + active + ", rental=" + rental
				+ "]";
	}
	
}
