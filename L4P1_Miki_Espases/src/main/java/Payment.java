import java.time.LocalDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name = "Payment")
public class Payment {
	
	@Id
	@Column(name = "id")
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int payment_id;
	
	@Column(name = "amount")
	private int amount;
	
	@Column(name = "payment_date")
	private LocalDate payment_date;
	
	@OneToOne(mappedBy = "payment_id")
	private Rental rental;
	
	public Payment() {
	
	}

	public Payment(int amount, LocalDate payment_date) {
		this.amount = amount;
		this.payment_date = payment_date;
	}

	public int getPayment_id() {
		return payment_id;
	}

	public void setPayment_id(int payment_id) {
		this.payment_id = payment_id;
	}

	public int getAmount() {
		return amount;
	}

	public void setAmount(int amount) {
		this.amount = amount;
	}

	public LocalDate getPayment_date() {
		return payment_date;
	}

	public void setPayment_date(LocalDate payment_date) {
		this.payment_date = payment_date;
	}

	public Rental getRental() {
		return rental;
	}

	public void setRental(Rental rental) {
		this.rental = rental;
	}

	@Override
	public String toString() {
		return "Payment [payment_id=" + payment_id + ", amount=" + amount + ", payment_date=" + payment_date
				+ ", rental=" + rental + "]";
	}
	
}
