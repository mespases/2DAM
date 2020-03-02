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
@Table(name = "Film")
public class Film {
	
	@Id
	@Column(name = "id")
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int film_id;
	
	@Column(name = "title")
	private String title;
	
	@Column(name = "descripcion")
	private String description;
	
	@Column(name = "release_year")
	private int release_year;
	
	@Column(name = "lenguage")
	private String lenguage;
	
	@Column(name = "rental_duration")
	private double rental_duration;
	
	@Column(name = "lenth")
	private int lenth;
	
	@Column(name = "rating")
	private String rating;
	
	@OneToOne(mappedBy = "payment_id")
	private Rental rental;
	
	@OneToOne(cascade = {CascadeType.ALL})
	@JoinColumn(name = "category_id")
	private Category categoriy_id;
	
	@OneToMany(mappedBy = "film", cascade = CascadeType.ALL)
	private List<Actor> actor = new ArrayList<Actor>();
	
	public Film() {
	
	}

	public Film(String title, String description, int release_year, String lenguage,
			double rental_duration, int lenth, String rating) {	
		this.title = title;
		this.description = description;
		this.release_year = release_year;
		this.lenguage = lenguage;
		this.rental_duration = rental_duration;
		this.lenth = lenth;
		this.rating = rating;
	}

	public int getFilm_id() {
		return film_id;
	}

	public void setFilm_id(int film_id) {
		this.film_id = film_id;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public int getRelease_year() {
		return release_year;
	}

	public void setRelease_year(int release_year) {
		this.release_year = release_year;
	}

	public String getLenguage() {
		return lenguage;
	}

	public void setLenguage(String lenguage) {
		this.lenguage = lenguage;
	}

	public double getRental_duration() {
		return rental_duration;
	}

	public void setRental_duration(double rental_duration) {
		this.rental_duration = rental_duration;
	}

	public int getLenth() {
		return lenth;
	}

	public void setLenth(int lenth) {
		this.lenth = lenth;
	}

	public String getRating() {
		return rating;
	}

	public void setRating(String rating) {
		this.rating = rating;
	}

	public Rental getRental() {
		return rental;
	}

	public void setRental(Rental rental) {
		this.rental = rental;
	}

	public Category getCategoriy_id() {
		return categoriy_id;
	}

	public void setCategoriy_id(Category categoriy_id) {
		this.categoriy_id = categoriy_id;
	}

	public List<Actor> getActor() {
		return actor;
	}

	public void setActor(List<Actor> actor) {
		this.actor = actor;
	}

	@Override
	public String toString() {
		return "Film [film_id=" + film_id + ", title=" + title + ", description=" + description + ", release_year="
				+ release_year + ", lenguage=" + lenguage + ", rental_duration=" + rental_duration + ", lenth=" + lenth
				+ ", rating=" + rating + ", rental=" + rental + ", categoriy_id=" + categoriy_id + ", actor=" + actor
				+ "]";
	}
	
	
}
