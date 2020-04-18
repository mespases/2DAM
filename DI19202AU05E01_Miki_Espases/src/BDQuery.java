import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import com.mysql.cj.xdevapi.Statement;

public class BDQuery {
	
	private java.sql.Statement st;
	
	public BDQuery() throws ClassNotFoundException, SQLException {
		getMySQLConnection();
	}

	private void getMySQLConnection() throws SQLException,
	ClassNotFoundException {
		
		String hostName = "127.0.0.1";
		String dbName = "employees";
		String userName = "root";
		String password = "root";

		Class.forName("com.mysql.cj.jdbc.Driver");

		String connectionURL = "jdbc:mysql://" + hostName + ":3306/" + dbName;

		Connection conn = DriverManager.getConnection(connectionURL, userName,
				password);
		
		st = conn.createStatement();
		
	}
	
	public ArrayList<String> getDepartamentos() throws SQLException, ClassNotFoundException {
		String query = "select dept_name from departments";
		
		ResultSet rs = ((java.sql.Statement) st).executeQuery(query);
		
		ArrayList<String> departamentos = new ArrayList<String>();
		
		while (rs.next()) {
			departamentos.add(rs.getString("dept_name"));
		}
	
		return departamentos;
	}
	
	public ArrayList<Integer> getEmp_no() throws SQLException {
		String query = "select emp_no from employees";

		ResultSet rs = ((java.sql.Statement) st).executeQuery(query);

		ArrayList<Integer> emp_no = new ArrayList<Integer>();
		
		while (rs.next()) {
			emp_no.add(rs.getInt("emp_no"));
		}

		return emp_no;
	}
	
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		BDQuery bd = new BDQuery();
		bd.getDepartamentos();
	}
}
